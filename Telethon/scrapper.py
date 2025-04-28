from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import os

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")

client = TelegramClient('sesion_name', api_id, api_hash)

async def join_channel(client, channel_link):
    try:
        await client(JoinChannelRequest(channel_link))
        print(f"Successfull joined the Channel {channel_link}")
    except:
        print(f"Failed to join the Channel {channel_link}")

async def scrape_message(client, channel, limit = 100):
    messages = []  # <-- IMPORTANT: Define messages list here!

    async for message in client.iter_messages(channel, limit):
        if message.text:
            #print(message)
            #print(message.stringify())
            print(message.text)
            print("-"*40)


            # Store in list
            messages.append(message.text)
            messages.append("-" * 40)

    # After collecting messages, write them into file
    with open("messages.txt", "w", encoding="utf-8") as f:
        for msg in messages:
            f.write(msg + "\n")

'''
async def main():
    await client.send_message('me', 'Hello Snehodeep')
'''

async def main():
    channel_link = 'https://t.me/+NvKywrEbznRlMGY9'
    #channel_link = 'https://t.me/Hackingbotprooo'
    await join_channel(client, channel_link)

    await scrape_message(client, channel_link, 100)

with client:
    client.loop.run_until_complete(main())