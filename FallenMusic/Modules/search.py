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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch
from urllib.parse import parse_qs, urlparse

from FallenMusic import app


def convert_youtube_link(original_link):
    parsed_url = urlparse(original_link)
    video_id = parse_qs(parsed_url.query).get('v')

    if video_id:
        return f"https://www.youtube.com/watch?v={video_id[0]}"
    else:
        return None


@app.on_message(filters.command(["search"]))
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    try:
        if len(message.command) < 2:
            return await message.reply_text("» Give some text to search baby!")
        
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("🔎")
        
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        
        while i < 4:
            title = results[i]['title']
            duration = results[i]['duration']
            views = results[i]['views']
            channel = results[i]['channel']
            
            link = convert_youtube_link(f"https://youtube.com{results[i]['url_suffix']}")
            
            if link:
                text += f"title : {title}\n"
                text += f"duration : `{duration}`\n"
                text += f"views : `{views}`\n"
                text += f"channel : {channel}\n"
                text += f"link : {link}\n\n"
            
            i += 1
        
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="close",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    
    except Exception as e:
        await message.reply_text(str(e))
