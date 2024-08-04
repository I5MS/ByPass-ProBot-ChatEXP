import requests
import schedule
import time

TOKEN = ''
CHANNEL_ID = ''
TEXT_FILE_PATH = 'messages.txt'


# Read messages from the file
def read_messages():
    with open(TEXT_FILE_PATH, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]


# Initialize messages and current index
messages = read_messages()
current_index = 0


# Function to send a message to Discord
def send_message():
    global current_index
    if messages:
        message = messages[current_index]
        url = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
        headers = {
            'Authorization': f'{TOKEN}',
            'Content-Type': 'application/json'
        }
        data = {
            'content': message
        }
        response = requests.post(url, headers=headers, json=data)
        print(f'Sent: {message}')
        print(f'Status Code: {response.status_code}')
        print(response.json())

        # Move to the next message, cycling back to the start if at the end
        current_index = (current_index + 1) % len(messages)
    else:
        print("No messages found in the file.")


# Schedule the message to be sent every minute
schedule.every(2).minutes.do(send_message)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(2)
