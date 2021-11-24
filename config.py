import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SOURCE_CODE = getenv("SOURCE_CODE")
OWNER_NAME = getenv("OWNER_NAME", "piroXpower")
ALIVE_NAME = getenv("ALIVE_NAME", "VideoPlayer")
BOT_USERNAME = getenv("BOT_USERNAME", "VcVideoRoBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Decode_Assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DeCodeSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DeecodeBots")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/3230fb4f2943318939118.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "190"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/5ff61ffe0eca274832c4d.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/e9e5bda48b8860839c0c5.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/5fb958c4ab51f49edd1e9.jpg")
