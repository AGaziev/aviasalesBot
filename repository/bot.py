from aiogram import Dispatcher, Bot
from config_reader import config
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()