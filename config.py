# yooo guiz Herox 
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAJqZ97OoewSKWlU05svC2a6sVAGDcULGNRIVgWjzOyU7YEbLlU794K1hYPFkQC8l9Rou4r6tSO77NH0RvAMzgtDCW_gZ1l5eI-JpRQx5idYdktyNI-1Pk6hv4b57x3Cxsbw4lR3xNsDAhMdgBSwGkE7A2hhvhd17WyYa-FZlZOF1yW9bAABgld_pbHdPQVsgEkw4Y9-OEVAf1GqNiybpBOt_WugP6oqUHhv4N3hMF3md8TIbkNB4B7mpbAe0Q9eTiDvU33ChX3ZGG4qh0pZNVeHjW0Z6AFkDJ8oOOeaNKRD_N_KPO37PYKv-iz8rbShRosoZzgnckPKxhJ8V1GmyQpf0N3SgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5253002724:AAHvqxxpWE-fvmQe5F8DBvRE7OQC_6J5Um0")
BOT_NAME = getenv("BOT_NAME", "Osmani-Music")
API_ID = int(getenv("API_ID", "14547608"))
API_HASH = getenv("API_HASH", "c6c5e34f44bc5dd80dd2a4b894c7bcff")
OWNER_NAME = getenv("OWNER_NAME", "ribajosmani")
ALIVE_NAME = getenv("ALIVE_NAME", "Ribaj Osmani")
BOT_USERNAME = getenv("BOT_USERNAME", "Mss_Rosan_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ribmusic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "osmanigroupbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "teamosmani")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1008271006").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a44453181ceccc246cffd.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Ribaj")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/af674fcfde30dab8680b2.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")

