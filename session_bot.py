import os
from telethon import TelegramClient, events

API_ID = int(os.getenv('API_ID', '35412080'))
API_HASH = os.getenv('API_HASH', 'e1c8db6c4e56c1253b1b51ecf41d255c')
BOT_TOKEN = os.getenv('BOT_TOKEN')

client = TelegramClient('bot_session', API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply(
        "🔐 **String Session Generator**\n\n"
        "📱 Send phone: +919876543210"
    )

if __name__ == '__main__':
    print("🤖 Bot Running!")
    client.start(bot_token=BOT_TOKEN)
    client.run_until_disconnected()
