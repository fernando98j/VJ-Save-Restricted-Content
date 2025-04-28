import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7742372929:AAEfO6m6CZcXn6BXtIgcu1tio4_TWjG7t7o")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "6937183461"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b791f1476bd9946490ad4f561eb86295")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ferdomunus:DWfNFy89kOuyI3dk@cluster0.cudc28l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
