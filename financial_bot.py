import asyncio
import random

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
import sqlite3
import aiohttp
import logging
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()











async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())