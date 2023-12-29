from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HAsH = getenv("API_HAsH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID","5356545108"))

PING_IMG = getenv("PING_IMG", "https://i.ibb.co/j3gQ0zw/channels4-profile.jpg")
sTART_IMG = getenv("sTART_IMG", "https://i.ibb.co/j3gQ0zw/channels4-profile.jpg")

sEssION = getenv("sEssION", None)

sUPPORT_CHAT = getenv("sUPPORT_CHAT", "https://t.me/HermonyHubGroup")
sUPPORT_CHANNEL = getenv("sUPPORT_CHANNEL", "https://t.me/ZEDTOOL")

sUDO_UsERs = list(map(int, getenv("sUDO_UsERs", "6538268369").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
