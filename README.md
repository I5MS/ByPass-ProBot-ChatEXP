# ChatEXP-ProBot

## Disclaimer: 
This project breaks Discord’s rules and may get your account banned. 

## Warning: 
Don’t share your Discord token with anyone, as it lets them access your account, including bypassing two-factor authentication (2FA) and your password.

## Features

- Reads messages from a text file.
- Sends messages to a specified Discord channel.
- Allows scheduling of message sending at defined intervals.
- Automatically cycles through the list of messages.

## Requirements

- Python 3.x
- `requests` library
- `schedule` library

## Setup

### 1. Install Dependencies

Make sure you have `requests` and `schedule` installed. You can install them using pip:

```bash
pip install requests requests
pip install requests schedule
```

### 2. Configure the Script

1. **Get Your Discord Token**: Follow the [How to Find Your Discord Token](https://www.youtube.com/watch?v=YEgFvgg7ZPI) to get your discord account token.

2. **Get Channel ID**: You need to have the channel ID where the messages will be sent. You can get it by enabling Developer Mode in Discord and right-clicking on the channel.

3. **Prepare the Text File**: Create a text file named `messages.txt` in the same directory as the script. Each line in this file should contain a message that you want to send.

4. **Update Script Variables**:
   - Replace `YOUR_DISCORD_TOKEN` with your actual Discord token.
   - Replace `YOUR_CHANNEL_ID` with the ID of the channel you want to send messages to.
   - Ensure `TEXT_FILE_PATH` points to your `messages.txt` file.

   Example:
   ```python
   TOKEN = 'YOUR_DISCORD_TOKEN'
   CHANNEL_ID = 'YOUR_CHANNEL_ID'
   TEXT_FILE_PATH = 'messages.txt'
   ```

### 3. Run the Script

Execute the script using Python:

```bash
python main.py
```

## How It Works

1. The script reads messages from `messages.txt`.
2. It sends a message to the specified Discord channel using the bot token and channel ID.
3. The script schedules the message sending to occur every 2 minutes.
4. It automatically cycles through the list of messages.

## Customization

- **Interval**: Adjust the scheduling interval by modifying the `every(2).minutes.do(send_message)` line to suit your needs.

## Troubleshooting

- **No Messages Found**: Ensure `messages.txt` is in the correct format and located in the same directory as the script.
- **Authorization Errors**: Verify your bot token and channel ID are correct and that the bot has the necessary permissions to send messages in the channel.
