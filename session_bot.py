import os
import asyncio
from telethon import TelegramClient, events

API_ID = int(os.getenv('TELEGRAM_API_ID', '35412080'))
API_HASH = os.getenv('TELEGRAM_API_HASH', 'e1c8db6c4e56c1253b1b51ecf41d255c')
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def main():
    client = TelegramClient('bot_session', API_ID, API_HASH)
    
    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.reply("🔐 Send phone: +919876543210")
    
    async with client:
        await client.start(bot_token=BOT_TOKEN)
        print("🤖 Bot Running!")
        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
