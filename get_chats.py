from keys import API_ID, API_HASH
from pyrogram import Client
import asyncio

async def get_chats():
    #запуск сессии
    client=Client(name='my_session', api_id=API_ID, api_hash=API_HASH)
    await client.start()

    #вывод всех чатов и их id
    async for dialog in client.get_dialogs():
        if dialog.chat.type.value == 'channel':
            print(dialog.chat.first_name or dialog.chat.title, dialog.chat.id)


if __name__ == '__main__':
 asyncio.run(get_chats())