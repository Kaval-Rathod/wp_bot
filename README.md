# WhatsApp OTP Bot

A Flask API that sends WhatsApp OTP messages automatically using the pywhatkit library.

## Features

- ✅ **Fully Automatic** - No manual intervention required
- ✅ **Auto-close WhatsApp** - Closes only the WhatsApp tab, not the entire browser
- ✅ **RESTful API** - Easy integration with frontend
- ✅ **CORS enabled** - Cross-origin requests supported
- ✅ **Error Handling** - Robust error handling and logging

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you're logged into WhatsApp Web in your browser

3. Update the sender number in `wp_bot.py` if needed

## Usage

### Start the API server:
```bash
python api.py
```

The server will start on `http://localhost:5000`
cmd command
curl -X GET http://localhost:5000/check-sender
-try message
   curl -X POST http://localhost:5000/send-whatsapp -H "Content-Type: application/json" -d "{\"phone_number\": \"+917984219838\", \"message\": \"Your message here\"}"

### Test the bot directly:
```bash
python wp_bot.py
```

### API Endpoints

#### Check Sender Status
```
GET /check-sender
```
Returns the sender number and status.

#### Send WhatsApp Message
```
POST /send-whatsapp
Content-Type: application/json

{
    "phone_number": "+1234567890",
    "otp": "123456",
    "brand_name": "Your Brand"
}
```

## How It Works

1. **Opens WhatsApp Web** in a new browser tab
2. **Types the message** automatically
3. **Sends the message** using Enter key
4. **Closes only the WhatsApp tab** (not the entire browser)
5. **Returns success/failure status**

## Important Notes

⚠️ **Before Running**:
- You must be logged into WhatsApp Web in your browser
- Ensure stable internet connection
- Phone numbers must include country code (e.g., +1234567890)

⚠️ **During Operation**:
- The bot will open WhatsApp Web automatically
- It will type the message and send it
- Only the WhatsApp tab will close, your browser stays open
- Don't interfere with the browser during operation

## Files

- `api.py` - Flask API server
- `wp_bot.py` - WhatsApp bot functionality
- `requirements.txt` - Python dependencies
- `PyWhatKit_DB.txt` - Message history log

## Troubleshooting

1. **Message not sending**: Check if WhatsApp Web is logged in
2. **Browser issues**: Make sure no other WhatsApp tabs are open
3. **Timing issues**: The bot uses optimized timing for reliability
4. **Tab not closing**: The bot only closes the WhatsApp tab, not the entire browser 