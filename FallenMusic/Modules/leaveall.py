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

import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import ASS_MENTION, sUNAME, app, app2


@app.on_message(filters.command(["leaveall", "assleaveall"]) & filters.user(OWNER_ID))
async def ASS_leaveall(_, message: Message):
    lear = await message.reply_text(f"» {ASS_MENTION} started leaving chats...")
    left = 0
    failed = 0
    chats = []
    async for dialog in app2.get_dialogs():
        chats.append(int(dialog.chat.id))
    schat = (await app.get_chat(sUNAME)).id
    for i in chats:
        if i in (-1001686672798, int(schat)):
            continue
        try:
            await app2.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
            failed += 1
    try:
        await lear.edit_text(
            f"<u>**» {ASS_MENTION} successfully left chats :**</u>\n\n**left :** `{left}`\n**failed :** `{failed}`"
        )
    except:
        await message.reply_text(
            f"<u>**» {ASS_MENTION} successfully left chats :**</u>\n\n**left :** `{left}`\n**failed :** `{failed}`"
        )
