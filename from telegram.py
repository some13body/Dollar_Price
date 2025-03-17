from telethon.sync import TelegramClient , events
from telethon.tl.types import PeerChannel
import asyncio
from google import genai

api_id = 20193597
api_hash = 'beed6014d49d681f7cc9fa5d730738b8'
session_name = 'amirmahdi_session'
chat = 'me'
pchid = 1557160311
bchid = 'justtestingsheet'

client = TelegramClient(session_name, api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats = [pchid]))
async def main(event):
    print(event.text)

client.run_until_disconnected()   
















"""
# Get Chat Messages
messages = client.get_messages(chat)
for message in client.iter_messages(chat):
    print(message.sender_id, ':', message.text )


# Get Private Channel Messages
messages = client.get_messages(PeerChannel(channel_id=pchid))
for message in client.iter_messages(PeerChannel(channel_id=pchid)):
    print(message.sender_id, ':', message.text)

# Get Public Channel Messages
messages = client.get_messages('justtestingsheet', limit=2)
for message in client.iter_messages('justtestingsheet'):
    print(message.sender_id, ':', message.text)

"""

"""
old_signal = []
messages = client.get_messages('justtestingsheet')
for message in client.iter_messages('justtestingsheet', reverse=True):
    old_signal.append(message.text)

for i in old_signal:
    print("OLD MESSAGE IS => ",i)
"""

"""
def sigre(new):
    print("THE NEW MESSAGE IS : => ",new)
    response = client.models.generate_content(
    model="gemini-2.0-flash", contents=new)
    print("Javab Gemini :",response.text)
    return response.text
"""

#27143428
# fdd048ef51e72f7bac61db87f4592284 
"""

149.154.167.40:443
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAyMEdY1aR+sCR3ZSJrtztKTKqigvO/vBfqACJLZtS7QMgCGXJ6XIR
yy7mx66W0/sOFa7/1mAZtEoIokDP3ShoqF4fVNb6XeqgQfaUHd8wJpDWHcR2OFwv
plUUI1PLTktZ9uW2WE23b+ixNwJjJGwBDJPQEQFBE+vfmH0JP503wr5INS1poWg/
j25sIWeYPHYeOrFp/eXaqhISP6G+q2IeTaWTXpwZj4LzXq5YOpk4bYEQ6mvRq7D1
aHWfYmlEGepfaYR8Q0YqvvhYtMte3ITnuSJs171+GDqpdKcSwHnd6FudwGO4pcCO
j4WcDuXc2CTHgH8gFTNhp/Y8/SpDOhvn9QIDAQAB
-----END RSA PUBLIC KEY-----

"""
"""
149.154.167.50:443
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g
5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO
62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/
+aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9
t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs
5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB
-----END RSA PUBLIC KEY-----
"""