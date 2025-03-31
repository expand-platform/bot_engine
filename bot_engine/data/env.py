from os import getenv

if getenv("ENVIRONMENT") == "testing":
    from utils.Dotenv import Dotenv

else:
    from bot_engine.utils.Dotenv import Dotenv


dotenv = Dotenv()

ENVIRONMENT = dotenv.get("ENVIRONMENT") 
PORT = dotenv.get("PORT")

BOT_TOKEN = dotenv.get("BOT_TOKEN")
MONGODB_TOKEN = dotenv.get("MONGODB_TOKEN")

#? Dear admins, don't forget to start a chat with your bot (/start) 
ADMIN_IDS = dotenv.get("ADMIN_IDS")
USER_IDS = dotenv.get("USER_IDS")
SUPER_ADMIN_ID = int(dotenv.get("SUPER_ADMIN_ID"))
