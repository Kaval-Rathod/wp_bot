import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import subprocess
import sys
import os
import webbrowser
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import queue

class WhatsAppBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Bot API Server")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Server variables
        self.server_thread = None
        self.server_running = False
        self.app = None
        
        # Create GUI
        self.create_widgets()
        
        # Import WhatsApp functions
        try:
            from wp_bot import send_whatsapp_message_auto, SENDER_NUMBER
            self.SENDER_NUMBER = SENDER_NUMBER
            self.send_whatsapp_message_auto = send_whatsapp_message_auto
        except Exception as e:
            self.log_message(f"Error importing WhatsApp functions: {e}")
            self.SENDER_NUMBER = "+917984219838"
            self.send_whatsapp_message_auto = None
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="📱 WhatsApp Bot API Server", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Server Status", padding="10")
        status_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status indicator
        self.status_label = ttk.Label(status_frame, text="⭕ Server Stopped", font=("Arial", 12))
        self.status_label.grid(row=0, column=0, sticky=tk.W)
        
        # Control buttons
        button_frame = ttk.Frame(status_frame)
        button_frame.grid(row=0, column=1, padx=(20, 0))
        
        self.start_button = ttk.Button(button_frame, text="Start Server", command=self.start_server)
        self.start_button.grid(row=0, column=0, padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="Stop Server", command=self.stop_server, state="disabled")
        self.stop_button.grid(row=0, column=1, padx=(0, 10))
        
        self.open_whatsapp_button = ttk.Button(button_frame, text="Open WhatsApp Web", command=self.open_whatsapp)
        self.open_whatsapp_button.grid(row=0, column=2)
        
        # Info frame
        info_frame = ttk.LabelFrame(main_frame, text="API Information", padding="10")
        info_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        info_text = f"""
Sender Number: {getattr(self, 'SENDER_NUMBER', '+917984219838')}
API URL: http://localhost:5000
Endpoints:
  • GET  /check-sender
  • POST /send-whatsapp (phone_number, message)
  • POST /send-otp (phone_number, otp, brand_name)

Test Command:
curl -X POST http://localhost:5000/send-whatsapp -H "Content-Type: application/json" -d "{{\\"phone_number\\": \\"+917984219838\\", \\"message\\": \\"Hello from API!\\"}}"
        """
        
        info_label = ttk.Label(info_frame, text=info_text, justify=tk.LEFT, font=("Consolas", 9))
        info_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Log frame
        log_frame = ttk.LabelFrame(main_frame, text="Server Logs", padding="10")
        log_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Log text area
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, width=70, font=("Consolas", 9))
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure log frame grid weights
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        # Test frame
        test_frame = ttk.LabelFrame(main_frame, text="Quick Test", padding="10")
        test_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Test inputs
        ttk.Label(test_frame, text="Phone:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.test_phone = ttk.Entry(test_frame, width=20)
        self.test_phone.insert(0, "+917984219838")
        self.test_phone.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
        
        ttk.Label(test_frame, text="Message:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5))
        self.test_message = ttk.Entry(test_frame, width=30)
        self.test_message.insert(0, "Hello from Windows App!")
        self.test_message.grid(row=0, column=3, sticky=tk.W, padx=(0, 10))
        
        self.test_button = ttk.Button(test_frame, text="Send Test Message", command=self.send_test_message)
        self.test_button.grid(row=0, column=4)
    
    def log_message(self, message):
        """Add message to log"""
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def start_server(self):
        """Start the API server"""
        if self.server_running:
            return
        
        self.log_message("Starting WhatsApp Bot API Server...")
        
        # Start server in separate thread
        self.server_thread = threading.Thread(target=self.run_server, daemon=True)
        self.server_thread.start()
        
        # Update UI
        self.status_label.config(text="🟢 Server Running")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.server_running = True
        
        self.log_message("Server started successfully!")
        self.log_message("API available at: http://localhost:5000")
    
    def stop_server(self):
        """Stop the API server"""
        if not self.server_running:
            return
        
        self.log_message("Stopping server...")
        
        # Update UI
        self.status_label.config(text="⭕ Server Stopped")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.server_running = False
        
        self.log_message("Server stopped.")
    
    def run_server(self):
        """Run the Flask server"""
        try:
            # Create Flask app
            self.app = Flask(__name__)
            CORS(self.app)
            
            # Setup logging
            logging.basicConfig(level=logging.INFO)
            
            @self.app.route('/check-sender', methods=['GET'])
            def check_sender():
                try:
                    return jsonify({
                        'sender_number': self.SENDER_NUMBER,
                        'status': 'active',
                        'ready': True
                    })
                except Exception as e:
                    return jsonify({'error': str(e)}), 500
            
            @self.app.route('/send-whatsapp', methods=['POST'])
            def send_message():
                try:
                    data = request.json
                    if not data:
                        return jsonify({'error': 'No JSON data provided'}), 400

                    required = ['phone_number', 'message']
                    if not all(field in data for field in required):
                        return jsonify({'error': 'Missing required fields: phone_number and message'}), 400

                    if self.send_whatsapp_message_auto:
                        success = self.send_whatsapp_message_auto(data['phone_number'], data['message'])
                    else:
                        return jsonify({'error': 'WhatsApp functions not available'}), 500
                    
                    return jsonify({
                        'success': success,
                        'sender': self.SENDER_NUMBER,
                        'receiver': data['phone_number'],
                        'message': data['message'],
                        'status': 'sent' if success else 'failed'
                    })

                except Exception as e:
                    self.log_message(f"API Error: {str(e)}")
                    return jsonify({'error': str(e)}), 500
            
            @self.app.route('/send-otp', methods=['POST'])
            def send_otp():
                try:
                    data = request.json
                    if not data:
                        return jsonify({'error': 'No JSON data provided'}), 400

                    required = ['phone_number', 'otp', 'brand_name']
                    if not all(field in data for field in required):
                        return jsonify({'error': 'Missing required fields: phone_number, otp, brand_name'}), 400

                    from wp_bot import create_otp_message
                    message = create_otp_message(
                        otp_code=data['otp'],
                        brand_name=data['brand_name']
                    )
                    
                    if self.send_whatsapp_message_auto:
                        success = self.send_whatsapp_message_auto(data['phone_number'], message)
                    else:
                        return jsonify({'error': 'WhatsApp functions not available'}), 500
                    
                    return jsonify({
                        'success': success,
                        'sender': self.SENDER_NUMBER,
                        'receiver': data['phone_number'],
                        'status': 'sent' if success else 'failed'
                    })

                except Exception as e:
                    self.log_message(f"API Error: {str(e)}")
                    return jsonify({'error': str(e)}), 500
            
            # Run server
            self.app.run(debug=False, host='0.0.0.0', port=5000)
            
        except Exception as e:
            self.log_message(f"Server error: {e}")
    
    def open_whatsapp(self):
        """Open WhatsApp Web"""
        try:
            webbrowser.open('https://web.whatsapp.com')
            self.log_message("Opening WhatsApp Web...")
        except Exception as e:
            self.log_message(f"Error opening WhatsApp Web: {e}")
    
    def send_test_message(self):
        """Send a test message"""
        if not self.server_running:
            messagebox.showerror("Error", "Server is not running!")
            return
        
        phone = self.test_phone.get()
        message = self.test_message.get()
        
        if not phone or not message:
            messagebox.showerror("Error", "Please enter phone number and message!")
            return
        
        self.log_message(f"Sending test message to {phone}...")
        
        # Send test message in separate thread
        test_thread = threading.Thread(target=self._send_test_message, args=(phone, message), daemon=True)
        test_thread.start()
    
    def _send_test_message(self, phone, message):
        """Send test message in background"""
        try:
            import requests
            
            response = requests.post('http://localhost:5000/send-whatsapp', 
                                   json={'phone_number': phone, 'message': message},
                                   headers={'Content-Type': 'application/json'})
            
            result = response.json()
            
            if result.get('success'):
                self.log_message("✅ Test message sent successfully!")
            else:
                self.log_message(f"❌ Test message failed: {result.get('error', 'Unknown error')}")
                
        except Exception as e:
            self.log_message(f"❌ Test message error: {e}")

def main():
    root = tk.Tk()
    app = WhatsAppBotApp(root)
    
    # Handle window close
    def on_closing():
        if app.server_running:
            if messagebox.askokcancel("Quit", "Server is running. Do you want to stop it and quit?"):
                app.stop_server()
                root.destroy()
        else:
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 