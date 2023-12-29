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

from FallenMusic import Ass_MENTION, LOGGER, sUDOERs, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) & sUDOERs)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("Changing assistant's profile pic...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"{Ass_MENTION} Profile pic changed successfully."
            )
        except:
            return await fuk.edit_text("Failed to change assistant's profile pic.")
    else:
        await message.reply_text(
            "Reply to a photo for changing assistant's profile pic."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & sUDOERs)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "successfully deleted assistant's profile pic."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("Failed to delete assistant's profile pic.")


@app.on_message(filters.command(["assbio", "setbio"]) & sUDOERs)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"{Ass_MENTION} Bio changed successfully."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"{Ass_MENTION} Bio changed successfully.")
    else:
        return await message.reply_text(
            "Reply to a message or give some text to set it as assistant's bio."
        )


@app.on_message(filters.command(["assname", "setname"]) & sUDOERs)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"{Ass_MENTION} Name changed successfully."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"{Ass_MENTION} Name changed successfully.")
    else:
        return await message.reply_text(
            "Reply to a message or give some text to set it as assistant's new name."
        )
