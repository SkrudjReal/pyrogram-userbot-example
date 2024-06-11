from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

from core.data import triggers as trg
from core.filters.is_user import is_user

from .main_skills import infect

async def setup_handlers(app: Client):
    # Main skills
    app.add_handler(MessageHandler(infect, filters.text & is_user), group=0)

