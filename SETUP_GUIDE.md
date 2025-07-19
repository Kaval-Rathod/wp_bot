# 📱 WhatsApp Bot Setup Guide

Complete step-by-step guide to set up and run your WhatsApp Bot API Server.

## 🚀 **Method 1: Windows App (Recommended)**

### **Step 1: Download/Clone Project**
```bash
# If you have the files already, skip this step
# If cloning from git:
git clone <your-repo-url>
cd bot
```

### **Step 2: Install Python Dependencies**
```bash
# Install all required packages
pip install -r requirements.txt
```

### **Step 3: Run the Windows App**
```bash
# Method A: Direct Python command
python whatsapp_bot_app.py

# Method B: Using batch file
# Double-click "WhatsApp Bot.bat"

# Method C: Using PowerShell
# Right-click "WhatsApp Bot.ps1" → "Run with PowerShell"
```

### **Step 4: Use the App**
1. **Click "Start Server"** - Starts the API
2. **Click "Open WhatsApp Web"** - Opens WhatsApp Web
3. **Login to WhatsApp Web** if needed
4. **Use Quick Test** to send test messages
5. **Use API endpoints** with curl commands

---

## 🔧 **Method 2: Command Line API**

### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 2: Start API Server**
```bash
python api.py
```

### **Step 3: Test API**
```bash
# Test 1: Check sender status
curl -X GET http://localhost:5000/check-sender

# Test 2: Send message
curl -X POST http://localhost:5000/send-whatsapp \
  -H "Content-Type: application/json" \
  -d "{\"phone_number\": \"+917984219838\", \"message\": \"Hello from API!\"}"
```

---

## 🤖 **Method 3: Direct Bot (No API)**

### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 2: Run Bot Directly**
```bash
python wp_bot.py
```

---

## 📋 **Complete Setup Checklist**

### **Prerequisites:**
- ✅ Python 3.8+ installed
- ✅ pip package manager
- ✅ Internet connection
- ✅ WhatsApp account

### **Files Required:**
- ✅ `requirements.txt` - Dependencies
- ✅ `wp_bot.py` - WhatsApp bot functions
- ✅ `api.py` - API server
- ✅ `whatsapp_bot_app.py` - Windows GUI app
- ✅ `WhatsApp Bot.bat` - Batch shortcut
- ✅ `WhatsApp Bot.ps1` - PowerShell shortcut

### **Setup Steps:**
1. ✅ **Install Python** (if not installed)
2. ✅ **Open command prompt** in project folder
3. ✅ **Install dependencies**: `pip install -r requirements.txt`
4. ✅ **Login to WhatsApp Web** in browser
5. ✅ **Run the app** using any method above

---

## 🎯 **Quick Start (5 Minutes)**

### **For Beginners:**
1. **Double-click** `WhatsApp Bot.bat`
2. **Click "Start Server"** in the app
3. **Click "Open WhatsApp Web"**
4. **Login to WhatsApp** if needed
5. **Use Quick Test** to send a message

### **For Developers:**
1. **Run**: `python api.py`
2. **Test**: `curl -X GET http://localhost:5000/check-sender`
3. **Send**: Use curl or your application

---

## 🔍 **Troubleshooting**

### **Common Issues:**

**1. "Module not found" error:**
```bash
pip install -r requirements.txt
```

**2. "WhatsApp Web not logged in":**
- Open https://web.whatsapp.com
- Scan QR code with your phone

**3. "Port 5000 already in use":**
- Close other applications using port 5000
- Or change port in the code

**4. "Virtual environment not found":**
- The app will use system Python automatically
- Or create virtual environment: `python -m venv venv`

**5. "Batch file not working":**
- Make sure you're in the correct directory
- Check if Python is in your PATH

---

## 📱 **API Usage Examples**

### **JavaScript (Website):**
```javascript
// Send WhatsApp message
fetch('http://localhost:5000/send-whatsapp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        phone_number: '+917984219838',
        message: 'Hello from website!'
    })
})
.then(response => response.json())
.then(data => console.log(data));
```

### **Python:**
```python
import requests

response = requests.post('http://localhost:5000/send-whatsapp', 
    json={
        'phone_number': '+917984219838',
        'message': 'Hello from Python!'
    },
    headers={'Content-Type': 'application/json'}
)

print(response.json())
```

### **cURL:**
```bash
curl -X POST http://localhost:5000/send-whatsapp \
  -H "Content-Type: application/json" \
  -d "{\"phone_number\": \"+917984219838\", \"message\": \"Hello from cURL!\"}"
```

---

## ✅ **Success Indicators**

### **When Everything Works:**
- ✅ **Windows App**: Shows "🟢 Server Running"
- ✅ **API**: Returns `{"ready": true, "status": "active"}`
- ✅ **WhatsApp**: Message appears in recipient's WhatsApp
- ✅ **Logs**: Show "Message sent successfully!"

### **API Endpoints Working:**
- ✅ `GET /check-sender` - Returns sender status
- ✅ `POST /send-whatsapp` - Sends any message
- ✅ `POST /send-otp` - Sends OTP message

---

## 🎉 **You're Ready!**

Your WhatsApp Bot is now fully functional and can:
- ✅ Send messages automatically
- ✅ Work with any website/app
- ✅ Handle multiple requests
- ✅ Run as a Windows service
- ✅ Integrate with any system

**Choose your preferred method and start sending WhatsApp messages!** 🚀 