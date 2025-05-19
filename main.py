from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from ping3 import ping

BOT_TOKEN = "YOUR_BOT_TOKEN"

# Load IPs from file
def load_servers():
    servers = {}
    try:
        with open("ips.txt", "r") as f:
            for i, line in enumerate(f):
                ip = line.strip()
                if ip:
                    servers[f"server{i+1}"] = ip
    except Exception as e:
        print(f"Error reading ips.txt: {e}")
    return servers

# Check server status
async def check_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    servers = load_servers()
    command = update.message.text.strip().lower().replace("/", "")

    if command not in servers:
        await update.message.reply_text("Unknown server. Check your command or update ips.txt.")
        return

    ip = servers[command]
    status = ping(ip, timeout=2)

    if status:
        await update.message.reply_text(f"{command.title().replace('server', 'Server ')} is online\nand working smooth")
    else:
        await update.message.reply_text(f"{command.title().replace('server', 'Server ')} is **Down**\nMaintenance Req!\nLogon to server to check logs", parse_mode="Markdown")

# Start bot
def main():
    servers = load_servers()
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    for server_cmd in servers.keys():
        app.add_handler(CommandHandler(server_cmd, check_server))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
