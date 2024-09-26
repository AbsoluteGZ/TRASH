"""
Нужно установить:
pip install aiogram aiohttp

"""

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import aiohttp
import asyncio

API_TOKEN = "8080300418:AAH94GZJP5KrrS5NenT74n9wZ3Xu2_ofdC8"


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
# Хэндлер на команду /start
async def cmd_start(message: types.Message):
    await message.answer("Добрый день. Как вас зовут?")
    
    
@dp.message(F.text)
async def process_name(message: types.Message):
    name = message.text
    usd_rate = await get_usd_exchange_rate()  # Получение курса доллара
    await message.answer(f"Привет, {name}! Рад с вами познакомиться. Курс доллара сегодня - {usd_rate}₽")

    
async def get_usd_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                usd_rate = data['rates']['RUB']  # Пример для получения курса USD к RUB
                return usd_rate
            else:
                raise Exception(f"Failed to fetch exchange rate: {response.status}")
    
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())