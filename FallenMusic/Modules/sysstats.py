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

import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from FallenMusic import BOT_NAME, SUDOERS, app
from FallenMusic.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"getting {BOT_NAME} system stats, it'll take a while..."
    )
    try:
        await message.delete()
    except:
        pass
    SUDOERS = len(SUDOERS)
    mod = len(ALL_MODULEs)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " gb"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ghz"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}mhz"
    except:
        cpu_freq = "failed to fetch"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
➻ <u>**{BOT_NAME} system stats**</u>

**python :** {pyver.split()[0]}
**pyrogram :** {pyrover}
**py-tgcalls :** {pytgver}
**SUDOERS :** `{SUDOERS}`
**modules :** `{mod}`

**ip :** {ip_address}
**mac :** {mac_address}
**hostname :** {hostname}
**platform :** {sp}
**processor :** {processor}
**architecture :** {architecture}
**platform release :** {platform_release}
**platform version :** {platform_version}

        <b><u>storage</b><u/>
**available :** {total[:4]} gib
**used :** {used[:4]} gib
**free :** {free[:4]} gib

**ram :** {ram}
**physical cores :** {p_core}
**total cores :** {t_core}
**cpu frequency :** {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="close",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )
