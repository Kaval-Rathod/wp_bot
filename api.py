from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from wp_bot import send_whatsapp_message_auto, SENDER_NUMBER

app = Flask(__name__)
CORS(app)

@app.route('/check-sender', methods=['GET'])
def check_sender():
    """Check if sender number is ready"""
    try:
        return jsonify({
            'sender_number': SENDER_NUMBER,
            'status': 'active',
            'ready': True
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/send-whatsapp', methods=['POST'])
def send_message():
    """Send WhatsApp message endpoint - simple version"""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Validate required fields
        required = ['phone_number', 'message']
        if not all(field in data for field in required):
            return jsonify({'error': 'Missing required fields: phone_number and message'}), 400

        # Send message directly
        success = send_whatsapp_message_auto(data['phone_number'], data['message'])
        
        return jsonify({
            'success': success,
            'sender': SENDER_NUMBER,
            'receiver': data['phone_number'],
            'message': data['message'],
            'status': 'sent' if success else 'failed'
        })

    except Exception as e:
        logging.error(f"API Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/send-otp', methods=['POST'])
def send_otp():
    """Send OTP message endpoint - for OTP specific messages"""
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Validate required fields
        required = ['phone_number', 'otp', 'brand_name']
        if not all(field in data for field in required):
            return jsonify({'error': 'Missing required fields: phone_number, otp, brand_name'}), 400

        # Create OTP message
        from wp_bot import create_otp_message
        message = create_otp_message(
            otp_code=data['otp'],
            brand_name=data['brand_name']
        )
        
        success = send_whatsapp_message_auto(data['phone_number'], message)
        
        return jsonify({
            'success': success,
            'sender': SENDER_NUMBER,
            'receiver': data['phone_number'],
            'status': 'sent' if success else 'failed'
        })

    except Exception as e:
        logging.error(f"API Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Clear any existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    # Setup logging
    logging.basicConfig(level=logging.INFO)
    print(f"Starting WhatsApp Bot API - Sender: {SENDER_NUMBER}")
    print("Available endpoints:")
    print("  GET  /check-sender")
    print("  POST /send-whatsapp (phone_number, message)")
    print("  POST /send-otp (phone_number, otp, brand_name)")
    app.run(debug=True, port=5000)
