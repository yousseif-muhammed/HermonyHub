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

from FallenMusic import BOT_NAME

PM_sTART_TExT = """
Hi {0}, This is {1}
- A Fast And Powerful Music Player Bot.
"""

sTART_TExT = """
Hi {0}, {1} can now play songs in {2}.

──────────────────
- For getting help about me or if you wanna ask something, you can join my [support chat]({3}).

"""

HELP_TExT = f"""
- Available Commands for Users in {BOT_NAME} :

/play: starts streaming the requested track on video chat.

/pause: Pauses the current playing stream.

/resume: Resumes the paused stream.

/skip: skips the current playing stream and starts streaming the next track in the queue.

/end: Clears the queue and ends the current playing stream.

/ping: shows the ping and system stats of the bot.

/sudolist: shows the list of sudo users of the bot.

/song: Downloads the requested song and sends it to you.

/search: searches the given query on YouTube and shows you the result.
"""

HELP_sUDO = f"""
- sudo Commands in {BOT_NAME} :

/activevc: shows the list of currently active voice chats.

/eval or /sh: Runs the given code on the bot's terminal.

/speedtest: Runs a speed test on the bot's server.

/sysstats: shows the system stats of the bot's server.

/setname [Text or reply to a text]: Change the assistant account name.

/setbio [Text or reply to a text]: Change the bio of the assistant account.

/setpfp [Reply to a photo]: Change the profile picture of the assistant account.

/delpfp: Delete the current profile picture of the assistant account.
"""

HELP_DEV = f"""
- Owner Commands in {BOT_NAME} :

/config: To get all configuration variables of the bot.

/broadcast [message or reply to a message]: Broadcast the message to served chats of the bot.

/rmdownloads: Clears the cache files downloaded on the bot's server.

/leaveall: Orders the assistant account to leave all chats.

/addsudo [Username or reply to a user]: Add the user to the sudo users list.

/rmsudo [Username or reply to a user]: Remove the user from sudo users list.
"""
