import logging
import os
import json

from telethon import TelegramClient

from os import getenv
from RAUSHAN.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = getenv("API_ID", "21803165")
API_HASH = getenv("API_HASH", "05e5e695feb30e25bef47484cc006da7")
CMD_HNDLR = getenv("CMD_HNDLR", default=".")

# Remove Heroku-specific variables
HEROKU_APP_NAME = None
HEROKU_API_KEY = None

# Bot Tokens
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

# SUDO_USERS configuration with file-based storage
SUDO_FILE = "sudo_users.json"

def load_sudo_users():
    """Load sudo users from file or environment variable"""
    try:
        # Try to load from file first
        if os.path.exists(SUDO_FILE):
            with open(SUDO_FILE, 'r') as f:
                data = json.load(f)
                return data.get("sudo_users", [])
    except Exception as e:
        logging.error(f"Error loading sudo users from file: {e}")
    
    # Fallback to environment variable
    try:
        env_sudo = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7403621976").split()))
        # Save to file for future use
        save_sudo_users(env_sudo)
        return env_sudo
    except:
        return [7403621976]  # Ultimate fallback

def save_sudo_users(sudo_list):
    """Save sudo users to file"""
    try:
        with open(SUDO_FILE, 'w') as f:
            json.dump({"sudo_users": sudo_list}, f, indent=4)
        return True
    except Exception as e:
        logging.error(f"Error saving sudo users: {e}")
        return False

def add_sudo_user(user_id):
    """Add a user to sudo list"""
    sudo_list = load_sudo_users()
    if user_id not in sudo_list:
        sudo_list.append(user_id)
        return save_sudo_users(sudo_list)
    return False

def remove_sudo_user(user_id):
    """Remove a user from sudo list"""
    sudo_list = load_sudo_users()
    if user_id in sudo_list:
        sudo_list.remove(user_id)
        return save_sudo_users(sudo_list)
    return False

# Load initial sudo users
SUDO_USERS = load_sudo_users()

# Add ALTRON users and OWNER_ID
for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)

try:
    OWNER_ID = int(getenv("OWNER_ID", default="7456681709"))
except:
    OWNER_ID = 7456681709

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# Remove duplicates and save final list
SUDO_USERS = list(set(SUDO_USERS))
save_sudo_users(SUDO_USERS)

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
logging.info(f"👑 Sudo users loaded: {len(SUDO_USERS)} users")

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
