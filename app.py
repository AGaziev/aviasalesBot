import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

import senders
from repository import dp, bot


async def main():
    logging.basicConfig(level=logging.INFO)
    scheduler = AsyncIOScheduler()
    senders.register_senders(scheduler)
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())