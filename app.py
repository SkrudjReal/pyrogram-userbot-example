from pyrogram import Client, idle
from pyrogram.handlers import MessageHandler

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.sql import text

from core.settings import settings
from core.handlers import setup_handlers

import asyncio
import uvloop
import logging


async def loop_tasks(app: Client):
    tasks = [
        setup_handlers(app)
    ]
    await asyncio.gather(*tasks)

async def main():
    
    logging.basicConfig(level=logging.ERROR,
                        format = '%(asctime)s - [%(levelname)s] - %(name)s - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    engine = create_async_engine(url=settings.db_url.get_secret_value(), echo=True, isolation_level='AUTOCOMMIT')
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    
    app = Client(
        str(settings.user_id) + '_session',
        settings.api_id.get_secret_value(),
        settings.api_hash.get_secret_value(),
        phone_number=settings.phone_number.get_secret_value()
    )
    

    asyncio.create_task(loop_tasks(app))
    
    try:
        print('Started successfully')
        await app.start()
        await idle()
    finally:
        await app.stop()


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    uvloop.run(main())