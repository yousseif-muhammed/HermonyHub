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
import importlib
import os

from pyrogram import idle

from FallenMusic import (
    Ass_ID,
    Ass_NAME,
    Ass_UsERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_UsERNAME,
    LOGGER,
    sUNAME,
    app,
    app2,
    pytgcalls,
)
from FallenMusic.Modules import ALL_MODULEs


async def fallen_startup():
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULEs:
        importlib.import_module("FallenMusic.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULEs)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")

    try:
        await app.send_message(
            sUNAME,
            f"✯ fallen music bot ✯\n\n𖢵 id : `{BOT_ID}`\n𖢵 name : {BOT_NAME}\n𖢵 username : @{BOT_UsERNAME}",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} failed to send message at @{sUNAME}, please go & check."
        )

    try:
        await app2.send_message(
            sUNAME,
            f"✯ fallen music ass ✯\n\n𖢵 id : `{Ass_ID}`\n𖢵 name : {Ass_NAME}\n𖢵 username : @{Ass_UsERNAME}",
        )
    except:
        LOGGER.error(
            f"{Ass_NAME} failed to send message at @{sUNAME}, please go & check."
        )

    await app2.send_message(BOT_UsERNAME, "/start")

    LOGGER.info(f"[•] Bot started As {BOT_NAME}.")
    LOGGER.info(f"[•] Assistant started As {Ass_NAME}.")

    LOGGER.info(
        "[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e"
    )
    await pytgcalls.start()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(fallen_startup())
    LOGGER.error("Fallen Music Bot stopped.")
