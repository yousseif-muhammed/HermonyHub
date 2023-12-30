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

import speedtest
from pyrogram import filters

from FallenMusic import SUDOERS, app


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ running download speedtest...**")
        test.download()
        m = m.edit("**⇆ running upload speedtest...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ sharing speedtest results...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spt"]) & SUDOERS)
async def speedtest_function(_, message):
    m = await message.reply_text("**» running speedtest...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **speedtest results** ✯
    
<u>**❥͜͡client :**</u>
**» __isp :__** {result['client']['isp']}
**» __country :__** {result['client']['country']}
  
<u>**❥͜͡server :**</u>
**» __name :__** {result['server']['name']}
**» __country :__** {result['server']['country']}, {result['server']['cc']}
**» __sponsor :__** {result['server']['sponsor']}
**» __latency :__** {result['server']['latency']}  
**» __ping :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
