import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, ALIVE_PIC, OWNER_ID
from RiZoeLXSpam.plugins.help import *


RIZ_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/6e92103071aa47ee7023e.mp4"

Riz_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/nightfighter0")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
RizX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/taitanoffice"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/nightfighter0")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://me/taitangamer")
        ]
        ]
        
        
#USERS 


@Riz.on(events.NewMessage(outgoing=True))
@Riz2.on(events.NewMessage(outgoing=True))
@Riz3.on(events.NewMessage(outgoing=True))
@Riz4.on(events.NewMessage(outgoing=True))
@Riz5.on(events.NewMessage(outgoing=True))
@Riz6.on(events.NewMessage(outgoing=True))
@Riz7.on(events.NewMessage(outgoing=True))
@Riz7.on(events.NewMessage(outgoing=True))
@Riz8.on(events.NewMessage(outgoing=True))
@Riz9.on(events.NewMessage(outgoing=True))
@Riz10.on(events.NewMessage(outgoing=True))
async def start(event):              
    if event.is_private:
       RizBot = await event.client.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [TAITAN 𝐗](https://t.me/taitangamamer)**"
       if event.sender_id not in SUDO_USERS:
            await event.client.send_file(TheRiZoeL,
                  RIZ_IMG,
                  caption=usermsg, 
                  buttons=RizX_Button)
                

