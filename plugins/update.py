from pyrogram.types import Message
from pyrogram import Client, filters
from info import CHANNELS, LOG_CHANNEL

@Client.on_message(filters.channel)
async def update(_: Client, msg: Message):
    if msg is None:
        return

    channel_id = msg.chat.id
    suc = await db.is_data_channel(channel_id)
    if not suc:
        return

    if msg.media and msg.media.type in ["video", "document"]:
        movie_name = msg.caption or msg.document.file_name
        if movie_name:
            message = f"{movie_name} has been added to **Bot**."
            await _.send_message(chat_id=LOG_CHANNEL, text=message)
