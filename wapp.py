import pywhatkit as kit
import pywhatkit as kit
import time
from datetime import datetime, timedelta

def send_bulk_messages(phone_numbers, message, delay=10):
    for phone in phone_numbers:
        try:
            # Get the current time
            now = datetime.now()
            # Set the time to send the message (20 seconds later)
            # send_time = now + timedelta(seconds=20)
            send_time = now + timedelta(minutes=1)
           
            # Extract hours and minutes
            hour = send_time.hour
            minute = send_time.minute
           
            # Send the message
            kit.sendwhatmsg(phone, message, hour, minute)
            print(f"Message sent to {phone} at {hour}:{minute}")
           
            # Delay between messages to avoid spamming WhatsApp Web
            time.sleep(delay)
        except Exception as e:
            print(f"Failed to send message to {phone}: {e}")

# List of phone numbers (use country code, e.g., "+1234567890") or excel or csv file
phone_numbers = ["Phone numbers","Phone numbers"]


# The message you want to send
message = """ Hello this is an auto generated email. Please ignore this message. """

# Send messages
send_bulk_messages(phone_numbers, message)
