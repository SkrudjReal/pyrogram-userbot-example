from pyrogram import Client, filters, enums
from pyrogram.types import Message

from core.settings import settings
from core.data.tricks.tricks import tricks, ucfg
from core.data import triggers as trg
from core.functions import base_func

import re

async def infect(app: Client, msg: Message):
    
    msgt = msg.text
    regular_ex = ucfg.prefix + r'\s' + trg.re_link_sup
    
    if msg.from_user.id != settings.user_id or not re.fullmatch(regular_ex, msgt, re.IGNORECASE):
        return
    
    id = base_func.link_getter(msg.text)
    text = f'заразить @{id}'
    
    await msg.reply(text, quote=False)

