# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "28729738"))
   API_HASH = os.getenv("API_HASH", "4b90907301682db77050967fc89806e9")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6855917642:AAHgbUmlcr1zx3Az7IRokAJRCeG2YYt8xws")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "NezrinMafiaBot")
   BOT_NAME = os.environ.get("BOT_NAME", "Nezrin 𝚃𝚊𝚐𝚐𝚎𝚛")
   OWNER_ID = int(os.environ.get("OWNER_ID","6634423600"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "thagiyev") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://qenberismayilzade005:natiq.3169@cluster0.wna0quv.mongodb.net/?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002140637128"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "GtaMusicPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002140637128"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002140637128"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "c7c2f4ed-e8c3-46e8-ae9a-bfd0ed6b1a69")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Natiq")
   CHANNEL = os.environ.get("CHANNEL", "GtaResmiKanal")
   SUPPORT = os.environ.get("SUPPORT", "GtaSupportKanal")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/d27c837b5d6b7fec54c06.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/d27c837b5d6b7fec54c06.jpg")
