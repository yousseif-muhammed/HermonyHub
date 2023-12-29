import asyncio

from pyrogram import Client, __version__ as ver


API_ID = input("\nEnter Your API ID :\n > ")
API_HAsH = input("\nEnter Your API HAsH :\n > ")

print("\n\nEnter the phone number associated with your telegram account when asked.\n\n")

fallen = Client("Fallen", api_id=API_ID, API_HAsH=API_HAsH, in_memory=True)


async def main():
    await fallen.start()
    sess = await fallen.export_session_string()
    txt = f"Here is your Pyrogram {ver} string session\n\n<code>{sess}</code>\n\nDon't share it with anyone.\nDon't forget to join @FallenAssociation"
    ok = await fallen.send_message("me", txt)
    print(f"Here is your Pyrogram {ver} string session\n{sess}\nDouble click to copy.") 


asyncio.run(main())
