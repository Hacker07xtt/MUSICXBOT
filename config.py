from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("27266473"))
API_HASH = getenv("3455697a8c977355bdf136d80cf8b145")

BOT_TOKEN = getenv("6052374952:AAG7nuIrbZFBPWXG7f8XkZ2j0mIJAXsLxYs", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("2070450796"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MUSICxcRobot")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5852269476").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
