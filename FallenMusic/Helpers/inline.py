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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_UsERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="Close", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▶️", callback_data="resume_cb"),
            InlineKeyboardButton(text="⏸️", callback_data="pause_cb"),
            InlineKeyboardButton(text="⏭️", callback_data="skip_cb"),
            InlineKeyboardButton(text="⛔️", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="Add Me To Your Group",
            url=f"https://t.me/{BOT_UsERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="Help", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="Channel", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="support Chat", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(text="Owner", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="Add Me To Your Group",
            url=f"https://t.me/{BOT_UsERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="Channel", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="support Chat", url=config.SUPPORT_CHAT),
    ],
    [

        InlineKeyboardButton(text="Developer", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="User Command",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="sudo Command", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="Owner Command", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="Back", callback_data="fallen_home"),
        InlineKeyboardButton(text="Close", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="support Chat", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="Back", callback_data="fallen_help"),
        InlineKeyboardButton(text="Close", callback_data="close"),
    ],
]
