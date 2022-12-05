import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16051908"))
    API_HASH = os.environ.get("API_HASH", "abf9b83f9ca40cf9f5ba9bf6e6afaa8b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5704393118:AAF19yThpqsMWyh3ngpCzolITtW-MQnocqE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "ENABLE")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TDNMUSICBOT")
    SUPPORT = os.environ.get("SUPPORT", "TDN_CHAT") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "THE_DRAGON_NETWORK_OFFICIAL") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/ead6fd17a560203a28f0c.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5486649568")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
