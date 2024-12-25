import asyncio
import crud_functions as cf
from aiogram import (Bot,
                     Dispatcher,
                     executor,
                     types)
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import (State,
                                              StatesGroup)
from aiogram.dispatcher import FSMContext
from aiogram.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           ReplyKeyboardMarkup,
                           KeyboardButton,
                           ReplyKeyboardRemove)


api = "7726405232:AAGizj4ox2RWHbJCid76XWZQlg-SkbIJxcg"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# cf .initiate_db() # Пункт для инциализации бд

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = 'Рассчитать'),
            KeyboardButton(text = 'Информация')
        ],
        [
            KeyboardButton(text = 'Купить')
        ],
        [
            KeyboardButton(text = 'Регистрация')
        ]
            ],
    resize_keyboard = True)

ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Product1', callback_data = 'sales'),
            InlineKeyboardButton(text = 'Product2', callback_data = 'sales'),
            InlineKeyboardButton(text = 'Product3', callback_data = 'sales'),
            InlineKeyboardButton(text = 'Product4', callback_data = 'sales')
        ]
    ],
    resize_keyboard = True
    )


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f"Привет! Я бот помогающий твоему здоровью. Выберите опцию: ", reply_markup = kb)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer("10 х вес(кг) + 6.25 х рост(см) - 5 х возраст(лет) + 5")


@dp.message_handler(text=['Регистрация'])
async def sign_up(message):
    await message.answer(f"Введите имя пользователя:", reply_markup = ReplyKeyboardRemove())
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if cf.is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer(f"Введите свой email:", reply_markup = ReplyKeyboardRemove())
        await RegistrationState.email.set()
    else:
        await message.answer(f"Пользователь существует, введите другое имя: ", reply_markup = kb)
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer(f"Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_reg_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    cf.add_users(data["username"], data["email"], int(data["age"]))
    await message.answer(f"Пользователь {data['username']} зарегестрирован", reply_markup=kb)
    await state.finish()


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer(f"Введите свой возраст:", reply_markup = ReplyKeyboardRemove())
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f"Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f"Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5
    await message.answer(f"{result}", reply_markup = kb)
    await state.finish()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i in range(1,5):
        with open (f'{i}.png', "rb") as product:
            await message.answer_photo(
                product,
                f"{cf.get_all_products(i)}",
                reply_markup=ReplyKeyboardRemove()
            )
    await message.answer("Выберите продукт для покупки: ", reply_markup = ikb)


@dp.callback_query_handler(text = 'sales')
async def sales(call):
    await call.message.answer("Вы успешно приобрели продукт!", reply_markup = kb)
    await call.answer()

@dp.message_handler()
async def all_messages(message):
    await message.answer(f"Введите команду /start, чтобы начать общение.'.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)