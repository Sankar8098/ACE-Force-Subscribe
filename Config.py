import os

class Config():
  # Bot Token (Use @BotFather)
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "5982258454:AAEXP0egJ19NNJWijmIZa2LHka0fekH-XRQ")

  # Bot Updates Channel Username (without @)
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "SK_MoviesOffl")

  # PostgresSQL DB URL (Use ElephantSQL)
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Test:1234@cluster0.2bzsp0q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

  # API & HASH (Use my.telegram.org)
  APP_ID = os.environ.get("APP_ID","23990433")
  API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")

  # Sudo users (Put your User ID)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "5821871362").split()))
  SUDO_USERS.append(5821871362)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**🤖 SK - Force Subscribe Bot**\n\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**⚙️ Setup**\n\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**🎲 Commmands**\n\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n/source_code - To get bot source code😍\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
       "**👨‍💻 Developed By @Sankar2k02**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
