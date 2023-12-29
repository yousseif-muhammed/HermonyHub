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
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import sUDOERs, app


@app.on_message(filters.command(["addsudo"]) & filters.user(OWNER_ID))
async def sudoadd(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "» reply to a user's message or give username/user id."
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) in sUDOERs:
            return await message.reply_text(f"» {user.mention} is already a sudo user.")
        try:
            sUDOERs.add(int(user.id))
            await message.reply_text(f"added {user.mention} in sudo users list.")
        except:
            return await message.reply_text("failed to add user in sudoers.")

    if message.reply_to_message.from_user.id in sUDOERs:
        return await message.reply_text(
            f"» {message.reply_to_message.from_user.mention} is already a sudo user."
        )
    try:
        sUDOERs.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            f"added {message.reply_to_message.from_user.mention} in sudo users list."
        )
    except:
        return await message.reply_text("failed to add user in sudoers.")


@app.on_message(filters.command(["delsudo", "rmsudo"]) & filters.user(OWNER_ID))
async def sudodel(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "» reply to a user's message or give username/user id."
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) not in sUDOERs:
            return await message.reply_text(
                f"» {user.mention} is not in sudo users list."
            )
        try:
            sUDOERs.remove(int(user.id))
            return await message.reply_text(
                f"» removed {user.mention} from sudo users list."
            )
        except:
            return await message.reply_text(f"failed to remove user from sudoers.")
    else:
        user_id = message.reply_to_message.from_user.id
        if int(user_id) not in sUDOERs:
            return await message.reply_text(
                f"» {message.reply_to_message.from_user.mention} is not in sudo users list."
            )
        try:
            sUDOERs.remove(int(user_id))
            return await message.reply_text(
                f"» removed {message.reply_to_message.from_user.mention} from sudo users list."
            )
        except:
            return await message.reply_text(f"failed to remove user from sudoers.")


@app.on_message(filters.command(["sudolist", "sudoers", "sudo"]))
async def sudoers_list(_, message: Message):
    hehe = await message.reply_text("» getting sudo users list...")
    text = "<u>🥀 **owner :**</u>\n"
    count = 0
    user = await app.get_users(OWNER_ID)
    user = user.first_name if not user.mention else user.mention
    count += 1
    text += f"{count}➤ {user}\n"
    smex = 0
    for user_id in sUDOERs:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n<u>✨ **sudoers :**</u>\n"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("» no sudo users found.")
    else:
        await hehe.edit_text(text)
