# wp_bot.py
import pywhatkit
import time
import logging
import pyautogui

# --- Configuration ---
SENDER_NUMBER = "+917984219838"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configure pyautogui for automation
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.5

def send_whatsapp_message(receiver_number: str, message: str):
    """Sends WhatsApp message automatically without manual intervention"""
    try:
        if not receiver_number.startswith('+'):
            raise ValueError("Phone number must start with '+'")
        
        logging.info(f"Sending from {SENDER_NUMBER} to: {receiver_number}")
        
        # Send message with automatic features
        pywhatkit.sendwhatmsg_instantly(
            phone_no=receiver_number,
            message=message,
            wait_time=10,      # Reduced wait time for faster automation
            tab_close=True,    # Close tab after sending
            close_time=2       # Reduced close time
        )
        
        # Additional automation: Ensure message is sent
        time.sleep(2)
        try:
            # Press Enter to send the message
            pyautogui.press('enter')
            logging.info("Message sent automatically!")
        except Exception as e:
            logging.warning(f"Could not press enter: {e}")
        
        # Wait for message to be sent
        time.sleep(2)
        logging.info("Message sent successfully!")
        return True

    except Exception as e:
        logging.error(f"WhatsApp Error: {e}")
        return False

def send_whatsapp_message_auto(receiver_number: str, message: str):
    """Enhanced automatic sending with multiple attempts"""
    try:
        if not receiver_number.startswith('+'):
            raise ValueError("Phone number must start with '+'")
        
        logging.info(f"Sending from {SENDER_NUMBER} to: {receiver_number}")
        
        # Method 1: Try instant sending
        try:
            pywhatkit.sendwhatmsg_instantly(
                phone_no=receiver_number,
                message=message,
                wait_time=8,
                tab_close=True,
                close_time=2
            )
            time.sleep(2)
            pyautogui.press('enter')
            logging.info("Message sent via instant method!")
            return True
        except Exception as e:
            logging.warning(f"Instant method failed: {e}")
        
        # Method 2: Try scheduled sending (next minute)
        try:
            from datetime import datetime
            current_time = datetime.now()
            hour = current_time.hour
            minute = current_time.minute + 1
            
            if minute >= 60:
                minute = 0
                hour += 1
            
            pywhatkit.sendwhatmsg(
                phone_no=receiver_number,
                message=message,
                time_hour=hour,
                time_min=minute,
                wait_time=10,
                tab_close=True
            )
            logging.info("Message scheduled for next minute!")
            return True
        except Exception as e:
            logging.error(f"Scheduled method also failed: {e}")
            return False

    except Exception as e:
        logging.error(f"All methods failed: {e}")
        return False

def create_otp_message(otp_code: str, brand_name: str) -> str:
    """Creates a formatted OTP message"""
    return (
        f"Your OTP for {brand_name} login is: {otp_code}. "
        "Please do not share this OTP with anyone."
    )

# Example usage when run directly
if __name__ == "__main__":
    recipient_phone_number = "+917984219838"
    otp_code = "123456"
    your_brand_name = "Kharidi Karlo"

    custom_message = create_otp_message(otp_code, your_brand_name)

    logging.info("--- Starting WhatsApp Bot (Auto Mode) ---")
    success = send_whatsapp_message_auto(recipient_phone_number, custom_message)

    if success:
        logging.info("--- Bot finished its task successfully. ---")
    else:
        logging.error("--- Bot failed to send the message. Please check the logs above. ---")
