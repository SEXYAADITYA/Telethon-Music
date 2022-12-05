import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16051908"))
    API_HASH = os.environ.get("API_HASH", "abf9b83f9ca40cf9f5ba9bf6e6afaa8b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5704393118:AAF19yThpqsMWyh3ngpCzolITtW-MQnocqE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu5Y3w8WuEmnSC8KkrLpKhssJxlp8dzq_VBJ-YpttwAPjoOfxirROewQrELi6af9uze3GZDUfi0Xun4z9IfEmuSBSw7TerXquN--mMooG62jKlpUAb6FBbK3t--SJ9_RdCEXCl43xlIoUGQh_eCifbgw2OJNpiV4rKHoI55CZVgDYye3J1i2PhKojffliWE-dfSAvnp6r7PRWXIJfzjwk9OydcLtK5n_tTgGJLPGNRaXza0a-LXs7a6sUJvD7IxRpI5i6Ujwrmgzwab8COBfkMq8IVYFXki8zB0QC_5Ui7CkvuMdXffPe6i4cN-p8MmWUdSAhIDqAt0xSxnYN6q3p9PQ=")
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
