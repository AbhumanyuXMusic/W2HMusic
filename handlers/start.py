from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hᴇʏ I'ᴀᴍ {bn}, "Cᴀɴᴅʏ" Tʜᴀᴛ Lᴇᴛs Yᴏᴜ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ Gʀᴏᴜᴘs.Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ @Candy_626.\n\n Tʜᴇ Assɪsᴛᴀɴᴛ Mᴜsᴛ Bᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Pʟᴀʏ Mᴜsɪᴄ Iɴ Tʜᴇ Vᴏɪᴄᴇ Cʜᴀᴛ Oғ Yᴏᴜʀ Gʀᴏᴜᴘ.\n\n /Hᴇʟᴘ Tᴏ Kɴᴏᴡ Mʏ Cᴏᴍᴍᴀɴᴅs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ⚡️", url="https://t.me/AlishaSupport"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Cʀᴇᴀᴛᴏʀ⚡️", url="https://t.me/Candy_626"
                    ),
                    InlineKeyboardButton(
                        "Uᴘᴅᴀᴛᴇs⚡️", url="https://t.me/Pubglovers_shayri_lovers"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Gʀᴏᴜᴘ Mᴇ ʟᴇ Jᴀᴏ⚡️", url="https://t.me/CandyMusic_Robot?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
