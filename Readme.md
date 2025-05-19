# Telegram Server Status Bot

A simple Telegram bot that monitors up to 50 servers via their IP addresses using `ping`.

## Features

- Sends status updates for each server via commands like `/server1`, `/server2`, etc.
- Automatically reads server IPs from `ips.txt`
- Tells if the server is online or down
- Easily scalable by editing the `ips.txt` file

## Setup & Usage

```bash
# Clone the repo
git clone https://your-repo-url && cd your-folder

# (Optional) Create a virtual environment
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip install python-telegram-bot ping3

# Create ips.txt with one IP per line
echo -e "1.2.3.4\n5.6.7.8\n9.10.11.12" > ips.txt

# Edit main.py and replace BOT_TOKEN with your token from BotFather

# Run the bot
python main.py

# Usage inside Telegram:
# Send /server1 -> Bot replies with status of first IP
# Send /server2 -> Bot replies with status of second IP
# Add up to 50 IPs in ips.txt and the bot will auto-detect them
