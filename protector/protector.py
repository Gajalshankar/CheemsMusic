from pyrogram import Client
from config import API_HASH, API_ID, STRING1 as SESSION_NAME


# Client For PM Protection
client = Client(SESSION_NAME, API_ID, API_HASH)
