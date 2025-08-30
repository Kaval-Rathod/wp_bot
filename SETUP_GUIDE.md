# 📱 WhatsApp Bot Setup Guide

Complete step-by-step guide to set up and run your WhatsApp Bot API Server. This guide covers all methods to use the bot, from beginner-friendly GUI to advanced API integration.

## � Prerequisites

Before starting, ensure you have the following:

### **System Requirements:**
- ✅ **Operating System**: Windows 10/11 (recommended), or any OS with Python support
- ✅ **Internet Connection**: Stable connection required for WhatsApp Web
- ✅ **WhatsApp Account**: Active WhatsApp account on your phone
- ✅ **Browser**: Chrome, Firefox, or Edge (for WhatsApp Web)

### **Python Installation:**
1. **Check if Python is installed:**
   ```bash
   python --version
   ```
   - If you see "Python 3.8+" (e.g., Python 3.10.5), you're good!
   - If not installed or version is too old, download from [python.org](https://python.org)

2. **During installation:**
   - ✅ Check "Add Python to PATH"
   - ✅ Install for all users (recommended)

3. **Verify pip is installed:**
   ```bash
   pip --version
   ```

### **Project Files:**
Your project should contain these files:
- `wp_bot.py` - Core WhatsApp bot functionality
- `api.py` - Flask API server
- `whatsapp_bot_app.py` - GUI application for Windows
- `requirements.txt` - Python dependencies
- `WhatsApp Bot.bat` - Windows batch launcher
- `WhatsApp Bot.ps1` - PowerShell launcher
- `PyWhatKit_DB.txt` - Message history log (auto-created)
- `README.md` - Project documentation

---

## 🚀 Quick Start (5 Minutes)

### **For Beginners (GUI Method):**
1. **Double-click** `WhatsApp Bot.bat`
2. **Click "Start Server"** in the GUI window
3. **Click "Open WhatsApp Web"** to login
4. **Scan QR code** with your phone's WhatsApp
5. **Use "Quick Test"** to send a test message

### **For Developers (API Method):**
1. **Install dependencies:** `pip install -r requirements.txt`
2. **Start server:** `python api.py`
3. **Test:** `curl -X GET http://localhost:5000/check-sender`

---

## 🔧 Detailed Setup Methods

### **Method 1: Windows GUI App (Easiest)**

Perfect for users who prefer a graphical interface.

#### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 2: Run the GUI App**
Choose one of these methods:

**Option A: Batch File (Recommended)**
- Double-click `WhatsApp Bot.bat`
- The app will start automatically

**Option B: PowerShell Script**
- Right-click `WhatsApp Bot.ps1`
- Select "Run with PowerShell"

**Option C: Direct Python**
```bash
python whatsapp_bot_app.py
```

#### **Step 3: Use the GUI**
1. **Start Server**: Click the "Start Server" button
2. **Open WhatsApp Web**: Click to open browser and login
3. **Login**: Scan QR code with WhatsApp on your phone
4. **Test**: Use the quick test feature to send a message
5. **API Info**: View available endpoints and test commands

---

### **Method 2: API Server Only**

For developers who want to integrate with other applications.

#### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 2: Start the API Server**
```bash
python api.py
```
Server starts on `http://localhost:5000`

#### **Step 3: Test the API**
```bash
# Check if sender is ready
curl -X GET http://localhost:5000/check-sender

# Send a message
curl -X POST http://localhost:5000/send-whatsapp \
  -H "Content-Type: application/json" \
  -d "{\"phone_number\": \"+917984219838\", \"message\": \"Hello from API!\"}"
```

---

### **Method 3: Direct Bot (No Server)**

For simple, one-time message sending without API.

#### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 2: Run the Bot**
```bash
python wp_bot.py
```
*Note: This will prompt for phone number and message interactively*

---

### **Method 4: Virtual Environment (Advanced)**

Recommended for development to avoid dependency conflicts.

#### **Step 1: Create Virtual Environment**
```bash
python -m venv venv
```

#### **Step 2: Activate Environment**
```bash
# Windows
venv\Scripts\activate

# PowerShell
venv\Scripts\Activate.ps1
```

#### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 4: Run as Usual**
```bash
python whatsapp_bot_app.py
# or
python api.py
```

---

## 📱 API Usage Examples

### **JavaScript/Node.js:**
```javascript
const response = await fetch('http://localhost:5000/send-whatsapp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        phone_number: '+917984219838',
        message: 'Hello from JavaScript!'
    })
});
const result = await response.json();
console.log(result);
```

### **Python Requests:**
```python
import requests

response = requests.post('http://localhost:5000/send-whatsapp', 
    json={
        'phone_number': '+917984219838',
        'message': 'Hello from Python!'
    }
)
print(response.json())
```

### **cURL:**
```bash
curl -X POST http://localhost:5000/send-whatsapp \
  -H "Content-Type: application/json" \
  -d "{\"phone_number\": \"+917984219838\", \"message\": \"Hello from cURL!\"}"
```

### **HTML Form:**
```html
<form action="http://localhost:5000/send-whatsapp" method="POST">
    <input name="phone_number" placeholder="+1234567890" required>
    <input name="message" placeholder="Your message" required>
    <button type="submit">Send WhatsApp</button>
</form>
```

---

## 🔍 Troubleshooting

### **Common Issues & Solutions:**

#### **1. "Python not recognized"**
**Problem:** Python is not in PATH
**Solution:**
```bash
# Check Python installation
where python

# If not found, reinstall Python with "Add to PATH" checked
# Or use full path:
"C:\Python310\python.exe" whatsapp_bot_app.py
```

#### **2. "Module not found" errors**
**Problem:** Dependencies not installed
**Solution:**
```bash
pip install -r requirements.txt

# If using virtual environment:
venv\Scripts\activate
pip install -r requirements.txt
```

#### **3. "WhatsApp Web not logged in"**
**Problem:** Browser not logged into WhatsApp Web
**Solution:**
- Open https://web.whatsapp.com
- Scan QR code with WhatsApp on your phone
- Keep browser open during bot operation

#### **4. "Port 5000 already in use"**
**Problem:** Another application using port 5000
**Solution:**
```bash
# Find what's using port 5000
netstat -ano | findstr :5000

# Kill the process (replace XXXX with PID)
taskkill /PID XXXX /F

# Or change port in api.py (line ~15)
```

#### **5. "Browser automation failed"**
**Problem:** PyAutoGUI can't control browser
**Solution:**
- Run as administrator
- Make sure browser window is not minimized
- Disable browser extensions that might interfere
- Try different browser (Chrome recommended)

#### **6. "Batch/PowerShell script not working"**
**Problem:** Wrong directory or permissions
**Solution:**
- Ensure scripts are in the same folder as Python files
- Run as administrator
- Check execution policy (PowerShell):
  ```powershell
  Set-ExecutionPolicy RemoteSigned
  ```

#### **7. "Virtual environment issues"**
**Problem:** venv not activating
**Solution:**
```bash
# Create new environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (PowerShell)
venv\Scripts\Activate.ps1
```

#### **8. "Message not sending"**
**Problem:** Various timing or automation issues
**Solution:**
- Ensure WhatsApp Web is logged in
- Check internet connection
- Wait a few seconds between messages
- Verify phone number format (+country code)

---

## 📁 File Explanations

- **`wp_bot.py`**: Core bot logic using PyWhatKit and PyAutoGUI
- **`api.py`**: Flask server providing REST API endpoints
- **`whatsapp_bot_app.py`**: Tkinter GUI for easy Windows usage
- **`requirements.txt`**: List of Python packages needed
- **`WhatsApp Bot.bat`**: Windows batch script to launch GUI
- **`WhatsApp Bot.ps1`**: PowerShell script to launch GUI
- **`PyWhatKit_DB.txt`**: Log file created by PyWhatKit (safe to delete)
- **`README.md`**: Basic project information

---

## ✅ Success Indicators

### **When Everything Works:**
- ✅ **GUI App**: Shows "🟢 Server Running" and green status
- ✅ **API Server**: Responds to `http://localhost:5000/check-sender`
- ✅ **WhatsApp Web**: Browser opens and stays logged in
- ✅ **Message Sending**: Recipient receives WhatsApp message
- ✅ **Logs**: Show "Message sent successfully!"

### **API Endpoints:**
- ✅ `GET /check-sender` - Returns `{"ready": true, "status": "active"}`
- ✅ `POST /send-whatsapp` - Sends custom messages
- ✅ `POST /send-otp` - Sends OTP with brand formatting

---

## 🎯 Advanced Configuration

### **Changing Sender Number:**
Edit `wp_bot.py` line 6:
```python
SENDER_NUMBER = "+1234567890"  # Your WhatsApp number
```

### **Changing Server Port:**
Edit `api.py` line ~15:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

### **Custom Message Templates:**
Modify functions in `wp_bot.py` for custom formatting.

---

## 🎉 You're Ready!

Your WhatsApp Bot is now fully set up and can:
- ✅ Send automated WhatsApp messages
- ✅ Work with websites and applications
- ✅ Handle multiple message types (text, OTP)
- ✅ Run as Windows service or API server
- ✅ Integrate with any programming language

**Choose your preferred method and start automating WhatsApp messages!** 🚀

---

*Last updated: August 30, 2025* 