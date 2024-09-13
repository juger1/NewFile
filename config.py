from operator import add
import os
import logging

#import dotenv
#dotenv.load_dotenv()

from logging.handlers import RotatingFileHandler

# TRUE or FALSE
U_S_E_P = True if (True if os.environ.get('U_S_E_P', "FALSE") == "TRUE" else False) and USE_SHORTLINK else False
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "FALSE") == "TRUE" else False
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "TRUE") == "TRUE" else False
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "TRUE") == "TRUE" else False 
USE_PAYMENT = True if (True if os.environ.get("USE_PAYMENT", "TRUE") == "TRUE" else False) and USE_SHORTLINK else False

PHOTO_URL = os environ.get("PHOTO_URL","https://graph.org/file/fd1487021734ee86c78b4.jpg")


# Read configuration from environment variables
REQUEST1 = os.environ.get("REQUEST1", "https://t.me/+4_XXp0Yxets4YTY9")  # Use default link if no button
REQUEST2 = os.environ.get("REQUEST2", "")

# Force user to join your backup channel, leave 0 if you don't need.
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001878910741"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))

# Ensure FORCE_SUB_CHANNEL is greater than FORCE_SUB_CHANNEL2
if FORCE_SUB_CHANNEL < FORCE_SUB_CHANNEL2:
    FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2 = FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL

# Bot token, API ID, and hash
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7453211392:AAGU0HOcv7lbPmIf1E4WKXiCyycMNoZnPro") 
APP_ID = int(os.environ.get("APP_ID", "25695562"))
API_HASH = os.environ.get("API_HASH", "0b691c3e86603a7e34aae0b5927d725a")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001732352061"))
OWNER_ID = int(os.environ.get("OWNER_ID", "1895952308"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002117941809"))

# Other bot configurations
PORT = os.environ.get("PORT", "8080")
DB_URL = os.environ.get("DB_URL", "mongodb+srv://pabagav476aersmcom:pabagav476aersmcom@cluster0.5jd4dlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "filestorebot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "60"))
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link. 💾")
OWNER_TAG = os.environ.get("OWNER_TAG", "stupidBoi")
TIME = int(os.environ.get("TIME", "60"))

# Shortlink configuration
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "modijiurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "a0c51b7b2b16924757c1e2eb6ca27096f9df7208")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "86400"))
TUT_VID = os.environ.get("TUT_VID", "https://t.me/How_to_Download_7x/32")

# Payment to remove token system
UPI_ID = os.environ.get("UPI_ID", "https://t.me/StupidBoi69")
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://t.me/StupidBoi69")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/{OWNER_TAG}")
PRICE1 = os.environ.get("PRICE1", "30 rs")
PRICE2 = os.environ.get("PRICE2", "110 rs")
PRICE3 = os.environ.get("PRICE3", "299 rs")
PRICE4 = os.environ.get("PRICE4", "550 rs")
PRICE5 = os.environ.get("PRICE5", "999 rs")

# Force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_MSG", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b> 🥺")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Admins
ADMINS = os.environ.get("ADMINS", "").split()
ADMINS.append(OWNER_ID)

# Logging configuration
LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
