from telethon.sync import TelegramClient , events
from telethon.tl.types import PeerChannel
import asyncio
from google import genai

api_id = 20193597
api_hash = 'beed6014d49d681f7cc9fa5d730738b8'
session_name = 'amirmahdi_session'
chat = 'me'
pchid = 1102518155
bchid = 'justtestingsheet'

cli = genai.Client(api_key="AIzaSyBhgm9yc4fZeitQwWO6uAJO9Gs0ynP-l68")
client = TelegramClient(session_name, api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats = [bchid]))
async def main(event):
    response = cli.models.generate_content(model="gemini-2.0-flash", contents=f'{event.text}')
    await event.reply(response.text)
    print(event.text)

client.run_until_disconnected()   
asyncio.run(main())
