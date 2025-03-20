# 📩 WhatsApp Bulk Message Sender

## 📌 Overview  
This Python script automates sending bulk messages on WhatsApp using the `pywhatkit` library. It schedules messages to be sent via WhatsApp Web at a specified time and ensures a delay between messages to avoid spamming. This script is useful for sending reminders, notifications, or automated messages to multiple contacts.

## 🚀 Features  
✔ Sends automated messages to multiple phone numbers  
✔ Schedules messages 1 minute ahead of the current time  
✔ Adds a delay between messages to prevent rapid sending  
✔ Uses `pywhatkit` to open WhatsApp Web and send messages  
✔ Simple and easy-to-use script for message automation  

## 📦 Requirements  

Before running the script, ensure the following requirements are met:  

✅ **Python 3.x** (recommended)  
✅ **Required Library:** Install using:  
```bash
pip install pywhatkit
✅ A stable internet connection
✅ WhatsApp Web should be logged in on your default browser

⚙ How It Works
1️⃣ The script takes a list of phone numbers (including country codes).
2️⃣ It sets the message and schedules it 1 minute ahead of the current time.
3️⃣ pywhatkit opens WhatsApp Web, selects the contact, and sends the message.
4️⃣ A delay is added between messages to avoid sending them too quickly.

🛠 Usage
🔹 Clone the Repository
git clone https://github.com/your-username/whatsapp-bulk-message-sender.git
cd whatsapp-bulk-message-sender
🔹 Modify the Script
Open whatsapp_bulk_sender.py and update:
phone_numbers list with the recipients' phone numbers
message variable with the text you want to send
🔹 Run the Script
python whatsapp_bulk_sender.py
The script will automatically send the message to each contact at the scheduled time.

🔔 Notes
📌 Ensure that WhatsApp Web remains open and active while the script is running.
📌 The script schedules messages slightly ahead of time to ensure delivery.
📌 The delay between messages can be adjusted in the send_bulk_messages function.

⚠ Disclaimer
This script is intended for educational and personal use. Automating WhatsApp messages in bulk may violate WhatsApp’s terms of service. Use at your own discretion.

Let me know if you need any modifications! 🚀🔥



This script is intended for educational and personal use. Automating WhatsApp messages in bulk may violate WhatsApp's terms of service. Use at your own discretion.

