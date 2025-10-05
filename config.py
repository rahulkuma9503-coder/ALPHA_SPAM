import logging
import os

from telethon import TelegramClient

from os import getenv
from RAUSHAN.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = getenv("API_ID", "21803165")
API_HASH = getenv("API_HASH", "05e5e695feb30e25bef47484cc006da7")
CMD_HNDLR = getenv("CMD_HNDLR", default=".")

# Remove Heroku-specific variables or set them to None
HEROKU_APP_NAME = None
HEROKU_API_KEY = None

# Bot Tokens - using getenv with None as default for safety
BOT_TOKEN = getenv("BOT_TOKEN", default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2", default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3", default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4", default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5", default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6", default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7", default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8", default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9", default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10", default=None)

# SUDO_USERS configuration
try:
    SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7403621976").split()))
except:
    SUDO_USERS = [7403621976]  # Fallback if environment variable parsing fails

# Add ALTRON users and OWNER_ID
for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)

try:
    OWNER_ID = int(getenv("OWNER_ID", default="7456681709"))
except:
    OWNER_ID = 7456681709  # Fallback if environment variable parsing fails

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# Remove duplicates
SUDO_USERS = list(set(SUDO_USERS))

# Validate essential variables
if not API_ID or not API_HASH:
    logging.error("❌ API_ID or API_HASH is missing! Bot cannot start.")
    exit(1)

# Check if at least one bot token is provided
bot_tokens = [BOT_TOKEN, BOT_TOKEN2, BOT_TOKEN3, BOT_TOKEN4, BOT_TOKEN5, 
              BOT_TOKEN6, BOT_TOKEN7, BOT_TOKEN8, BOT_TOKEN9, BOT_TOKEN10]
active_bots = [token for token in bot_tokens if token is not None]

if not active_bots:
    logging.error("❌ No bot tokens provided! Please set at least one BOT_TOKEN environment variable.")
    exit(1)

logging.info(f"🤖 Starting {len(active_bots)} bot(s)...")


# ------------- CLIENTS -------------
# Initialize only the bots that have tokens
clients = []

if BOT_TOKEN:
    X1 = TelegramClient('X1', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN)
    clients.append(X1)
else:
    X1 = None

if BOT_TOKEN2:
    X2 = TelegramClient('X2', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN2)
    clients.append(X2)
else:
    X2 = None

if BOT_TOKEN3:
    X3 = TelegramClient('X3', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN3)
    clients.append(X3)
else:
    X3 = None

if BOT_TOKEN4:
    X4 = TelegramClient('X4', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN4)
    clients.append(X4)
else:
    X4 = None

if BOT_TOKEN5:
    X5 = TelegramClient('X5', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN5)
    clients.append(X5)
else:
    X5 = None

if BOT_TOKEN6:
    X6 = TelegramClient('X6', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN6)
    clients.append(X6)
else:
    X6 = None

if BOT_TOKEN7:
    X7 = TelegramClient('X7', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN7)
    clients.append(X7)
else:
    X7 = None

if BOT_TOKEN8:
    X8 = TelegramClient('X8', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN8)
    clients.append(X8)
else:
    X8 = None

if BOT_TOKEN9:
    X9 = TelegramClient('X9', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN9)
    clients.append(X9)
else:
    X9 = None

if BOT_TOKEN10:
    X10 = TelegramClient('X10', int(API_ID), API_HASH).start(bot_token=BOT_TOKEN10)
    clients.append(X10)
else:
    X10 = None

logging.info(f"✅ {len(clients)} bot client(s) initialized successfully!")
