import os

API_ID = os.environ.get('API_ID', '26305247')
API_HASH = os.environ.get('API_HASH', '20ca7e6687c281e11782856c7efd0ff7')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5918078029:AAE84fJsHoGcZkU4ReKxMrYYD3piFUoB4no')
OWNER_ID = int(os.environ.get("OWNER_ID", "5791145987"))
ADMINS = (
    [int(i) for i in os.environ.get("ADMINS", "5791145987").split(" ")]
    if os.environ.get("ADMINS")
    else []
)
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)
MONGODB = os.environ.get('MONGODB', 'mongodb+srv://Dipanshu_021:ad8920@cluster0.f7migc1.mongodb.net/?retryWrites=true&w=majority')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'Cluster0')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'link1db')
CHANNELS = os.environ.get('CHANNELS', "False")
CHANNELS_LIST = (
    [int(i) for i in os.environ.get("CHANNELS_LIST").split(" ")]
    if os.environ.get("CHANNELS_LIST")
    else []
)
FORCESUB = os.environ.get('FORCESUB', "True")

# Other Settings
UPDATE_CHANNEL =  int(os.environ.get('UPDATE_CHANNEL', '-1001740189478'))
USERNAME = os.environ.get('USERNAME', 'film_update_official')
HOWTO = os.environ.get('HOWTO', 'film_update_official')
RESULTS_COUNT = int(os.environ.get('RESULT_COUNTS', 10))
AUTO_DELETE = os.environ.get('AUTO_DELETE', True)
AUTO_DELETE_TIME = int(os.environ.get('AUTO_DELETE_TIME', 300))
IMDB_TEMPLATE = os.environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
MAX_LIST_ELM = os.environ.get("MAX_LIST_ELM", None)
WELCOME_IMAGE = os.environ.get('WELCOME_IMAGE', 'https://bit.ly/3y8miWu')
RESULTS_IMAGE = os.environ.get('RESULTS_IMAGE', 'https://static.wikia.nocookie.net/ideas/images/e/e4/Movie_night.jpg')
MDISK_API=os.environ.get('')
SHORTENER_API = os.environ.get('SHORTENER_API', '1a4f5e855065095e9ed1ba714976f27571f4162f')
SHORTENER_WEBSITE = os.environ.get('SHORTENER_WEBSITE', 'sheralinks.com')
OMDB_API=os.environ.get('OMDB_API')
CUSTOM_CAPTION=os.environ.get('CUSTOM_CAPTION', '{caption}')
#  Replit Config
REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))
USE_OMDB = os.environ.get("USE_OMDB", False)
SONU_PIC = os.environ.get('SONU_PIC', 'https://graph.org/file/fd4a9342da2c0f60a6434.jpg')
