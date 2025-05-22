# -*- coding: utf-8 -*- v.lamboni version 0.0.1
import asyncio
from telegram import Bot


async def main():
    bot = Bot("7401386745:AAFX9qPnXAj9clvE7-z3gxIjRdrXt4haz0s")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())