# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "16869866"))
API_HASH = os.environ.get("API_HASH", "b6defd08178346ef6d0539e4db127acf")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5876962148:AAG9PsU6fPkDrN8zlsJEr9SeBI06YbvesPE")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Yukkukk:<lamichhanegamer>@cluster0.1v8hcjs.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1889791911")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1864553525")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "linktoearnsitegroup") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
