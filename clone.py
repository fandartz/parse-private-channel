from keys import API_ID, API_HASH
from pyrogram import Client
from typing import AsyncGenerator, List
from pyrogram.types import Message
import asyncio
import time

#откуда копировать
copy_channel_id=-1002129007381
#куда отправлять
paste_channel_id=-1002059509671


#функция замены местами сообщений (чтобы сообщения шли в том порядке, в котором они в канале)
async def reverse_msg (messages: AsyncGenerator):
   reverse_message = [message async for message in messages]
   return reverse_message[::-1]

#функция запуска копирования сообщений
async def clone (copy_channel_id: int, paste_channel_id: int):
 #запуск сессии
   client=Client(name='my_session', api_id=API_ID, api_hash=API_HASH)
   await client.start()

   while True:
      try:
         #получение сообщений с канала 
         messages: AsyncGenerator[Message, None] = client.get_chat_history(chat_id=copy_channel_id)
 
         #вызов функции замены сообщений местами
         reversed_messages: List[Message] = await reverse_msg(messages=messages)


         #цикл отправки всех сообщений
         for message in reversed_messages:
            last_id=13
            if (message.id > last_id):
               #отправка фото
               if message.photo:
                  if message.caption:
                     photo = await message.download(in_memory=True)
                     await client.send_photo(chat_id=paste_channel_id, photo=photo, caption=message.caption.html)
                  else:
                     photo = await message.download(in_memory=True)
                     await client.send_photo(chat_id=paste_channel_id, photo=photo)
               #отправка видео
               elif message.video:
                  if message.caption:
                     video = await message.download(in_memory=True)
                     await client.send_video(chat_id=paste_channel_id, video=video, caption=message.caption.html)
                  else:
                     video = await message.download(in_memory=True)
                     await client.send_video(chat_id=paste_channel_id, video=video)
               #отправка кружочков
               elif message.video_note:
                  if message.caption:
                     video_note = await message.download(in_memory=True)
                     await client.send_video_note(chat_id=paste_channel_id, video_note=video_note, caption=message.caption.html)
                  else:
                     video_note = await message.download(in_memory=True)
                     await client.send_video_note(chat_id=paste_channel_id, video_note=video_note)
               #отправка аудио
               elif message.audio:
                  if message.caption:
                     audio = await message.download(in_memory=True)
                     await client.send_audio(chat_id=paste_channel_id, audio=audio, caption=message.caption.html)
                  else:
                     audio = await message.download(in_memory=True)
                     await client.send_audio(chat_id=paste_channel_id, audio=audio)
               #отправка гс
               elif message.voice:
                  if message.caption:
                     voice = await message.download(in_memory=True)
                     await client.send_voice(chat_id=paste_channel_id, voice=voice, caption=message.caption.html)
                  else:
                     voice = await message.download(in_memory=True)
                     await client.send_voice(chat_id=paste_channel_id, voice=voice)
               #отправка текста
               elif message.text:
                  await client.send_message(chat_id=paste_channel_id, text=message.text)
         time.sleep(1)
      except:
         pass
 
      

if __name__ == '__main__':
   asyncio.run(clone(copy_channel_id, paste_channel_id))