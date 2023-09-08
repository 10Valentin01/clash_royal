from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN: str = '6655338084:AAGjpfRsKbejABHrV7EMIjadFydTQrfB7k4'


bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    btn_1 = InlineKeyboardButton(text='Shop', web_app=WebAppInfo(url='https://10valentin01.github.io/clash_royal/'))
    kb = InlineKeyboardMarkup(inline_keyboard=[[btn_1]])

    await message.answer('Привет!\nМеня зовут бот магазин!\nЗаходи!', reply_markup=kb)


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)