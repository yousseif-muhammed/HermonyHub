from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://i.ibb.co/j3gQ0zw/channels4-profile.jpg")
START_IMG = getenv("START_IMG", "https://i.ibb.co/j3gQ0zw/channels4-profile.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/HermonyHubGroup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ZEDTOOL")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6538268369").split()))


FAILED = "https://i.ibb.co/j3gQ0zw/channels4-profile.jpg"
