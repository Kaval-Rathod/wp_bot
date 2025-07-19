# wp_bot.py
import pywhatkit
import time
import logging

# --- Configuration ---
SENDER_NUMBER = "+917984219838"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_whatsapp_message(receiver_number: str, message: str):
    """Sends WhatsApp message using static sender number"""
    try:
        if not receiver_number.startswith('+'):
            raise ValueError("Phone number must start with '+'")
        
        logging.info(f"Sending from {SENDER_NUMBER} to: {receiver_number}")
        
        # Send message with proper timing
        pywhatkit.sendwhatmsg_instantly(
            phone_no=receiver_number,
            message=message,
            wait_time=15,      # Wait time before sending
            tab_close=True,    # Close tab after sending
            close_time=3       # Time to wait before closing
        )
        
        # Wait for message to be sent
        time.sleep(3)
        logging.info("Message sent successfully!")
        return True

    except Exception as e:
        logging.error(f"WhatsApp Error: {e}")
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

    logging.info("--- Starting WhatsApp Bot ---")
    success = send_whatsapp_message(recipient_phone_number, custom_message)

    if success:
        logging.info("--- Bot finished its task successfully. ---")
    else:
        logging.error("--- Bot failed to send the message. Please check the logs above. ---")
