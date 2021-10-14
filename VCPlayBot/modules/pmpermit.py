
from pyrogram import Client
import asyncio
from VCPlayBot.config import SUDO_USERS
from VCPlayBot.config import PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from VCPlayBot.services.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Hello😇❤️ There,\n\n **This is a 💞🎧MUSIC & VIDEO W🌍RLD™🎧💞 Owner service** .\n\n **❗️ Rules**:-\n\n   - අනවශ්‍ය කතාබස් කිරීමට අවසර නැත🔇.\n   - No spam allowed🔇 \n\n 💢🌀👉 **Please pay attention🙃.**\n\n 💢🌀  **ඔබ මෙතැන් සිට N.Anuja Supulsara වෙත,\n පණිවිඩයක්💬 යවනවා නම් එයින් අදහස් වන්නේ N.Anuja Supulsara ඔබේ පණිවිඩය දැක කතාබස් කිරීමට සම්බන්ධ වන බවයි.**\n\n    **- ⚠️Don't add this N.A.Supulsara to secret groups.**\n\n- **ස්තූතී 😇❤️**  \n\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pmpermit turned off")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("...")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("Approoved to PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("Dispprooved to PM")
        return
    message.continue_propagation()
    
