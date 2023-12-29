# MIT License
#
# Copyright (c) 2023 Anonymousx1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "software"), to deal
# in the software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the software, and to permit persons to whom the software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the software.
#
# THE sOFTWARE Is PROVIDED "As Is", WITHOUT WARRANTY OF ANY KIND, ExPREss OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIEs OF MERCHANTABILITY,
# FITNEss FOR A PARTICULAR PURPOsE AND NONINFRINGEMENT. IN NO EVENT sHALL THE
# AUTHORs OR COPYRIGHT HOLDERs BE LIABLE FOR ANY CLAIM, DAMAGEs OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWIsE, ARIsING FROM,
# OUT OF OR IN CONNECTION WITH THE sOFTWARE OR THE UsE OR OTHER DEALINGs IN THE
# sOFTWARE.

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from FallenMusic import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>**{BOT_NAME} config variables :**</u>

**api_id :** `{config.API_ID}`
**API_HAsH :** `{config.API_HAsH}`

**bot_token :** `{config.BOT_TOKEN}`
**duration_limit :** `{config.DURATION_LIMIT}`

**owner_id :** `{config.OWNER_ID}`
**sudo_users :** `{config.sUDO_UsERs}`

**ping_img :** `{config.PING_IMG}`
**start_img :** `{config.sTART_IMG}`
**support_chat :** `{config.sUPPORT_CHAT}`

**session :** `{config.sEssION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("» failed to send the config variables.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "» please check your pm, i've sent the config variables there."
        )
