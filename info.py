import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '2229357'))
API_HASH = environ.get('API_HASH', '31f183a5a075fd4996cb8ad59e7b794f')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://te.legra.ph/file/adf86e15ab3ca523c1a45.jpg https://te.legra.ph/file/135037671067393008d51.jpg https://te.legra.ph/file/fd08afd67c52b118b1fda.jpg https://te.legra.ph/file/7034913b54265276b8b33.jpg https://te.legra.ph/file/c009bc7f71bd3f0e90d91.jpg https://te.legra.ph/file/9e35ede2d9b7bffcadd13.jpg https://te.legra.ph/file/c87d6aa97c29096d3b0f2.jpg  https://te.legra.ph/file/f6389cd23eff57753227b.jpg https://te.legra.ph/file/e214c8972725c377c6534.jpg https://te.legra.ph/file/e214c8972725c377c6534.jpg  https://te.legra.ph/file/7c30e62257be4f45a937f.jpg https://te.legra.ph/file/80aba901626d015f3ff2e.jpg https://te.legra.ph/file/4c9468ba84b3fff28292e.jpg https://te.legra.ph/file/586cb2f3fb5f4b4dd15b2.jpg https://te.legra.ph/file/9b287f3beb74be51d3e31.jpg https://te.legra.ph/file/9e9ffe63964839ef04f6a.jpg https://te.legra.ph/file/fada2609719f354084c55.jpg https://te.legra.ph/file/029ed97a0035e12df883d.jpg https://te.legra.ph/file/bd7b8dec9707bdfa9684a.jpg https://te.legra.ph/file/130aa04cc73692b473b85.jpg https://te.legra.ph/file/5b078a0fbd493e5dfe64e.jpg https://te.legra.ph/file/cb96aa590c9a5cccb1127.jpg https://te.legra.ph/file/ed2b5a28880357b1b86e1.jpg https://te.legra.ph/file/f23eb6239acf00757765a.jpg https://te.legra.ph/file/1b92a0ed03f31a98b25f9.jpg https://te.legra.ph/file/dfe55f9e41dbdc5384dc0.jpg https://te.legra.ph/file/273152d981d795f1ce8fb.jpg https://te.legra.ph/file/5ccf81ce5ea0ab1b7af7f.jpg https://te.legra.ph/file/fae5defe1927b8171c536.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/7f3118e54b78c82b05a39.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://te.legra.ph/file/364204ddcd64180a7c7dc.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/229b746a9efacb4245b53.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '794968418').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001503756494').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '794968418 5290038359').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', "")
reqst_channel = environ.get('REQST_CHANNEL_ID', "")
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others

VERIFY = bool(environ.get('VERIFY', True))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'easysky.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'c0c9fb160a5d33bb141ce117e2cce939a36a9682')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '').split()]
PORT = environ.get("PORT", "8080")
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+CuTT-clY8GQ5ZWE9')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/TVSeriesCW')
MOVIE_GRP = environ.get('MOVIE_GRP', 'https://telegram.me/+jARBFU1eMxk1YmY1')
SERIES_GRP = environ.get('SERIES_GRP', 'https://telegram.me/+6q0f6-TYbA85ZjM1')
DC_CHNL = environ.get('DC_CHNL', 'https://telegram.me/Arrowverse24Hour')
MARVEL_CHNL = environ.get('MARVEL_CHNL', 'https://telegram.me/+5PhM9DHUi_djMDU1')
MAIN_CHNL = environ.get('MAIN_CHNL', 'https://telegram.me/TVSeriesCW')
HOW_VERIFY = environ.get('HOW_VERIFY', 'https://t.me/TVSeriesCW')
MSG_ALRT = environ.get('MSG_ALRT', '🚩 @TVSeriesCW Best Channel In Telegram')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001500025641'))
REQUEST_LOGS = int(environ.get('REQUEST_LOGS', '-1001820924316'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'tvseriescw_group')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", "4")
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001500025641')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
