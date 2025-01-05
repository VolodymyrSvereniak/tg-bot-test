from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove


import app.database.requests as rq
import app.keyboards as kb


router = Router()


# class Register(StatesGroup):
#     name = State()
#     age = State()
#     number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer("Welcome to shoes shop", reply_markup=kb.main)


@router.message(F.text == "Catalog")
async def catalog(message: Message):
    await message.answer("Catalog:", reply_markup=ReplyKeyboardRemove())
    await message.answer("Choose category", reply_markup=await kb.categories())


@router.callback_query(F.data.startswith("category_"))
async def category(callback: CallbackQuery):
    await callback.answer("You choosed category")
    await callback.message.answer(
        "Choose item by category",
        reply_markup=await kb.items(callback.data.split("_")[1]),
    )


@router.callback_query(F.data.contains("to_main"))
async def category(callback: CallbackQuery):
    await callback.answer("Home page")
    await callback.message.answer("Choose category", reply_markup=kb.main)


# @router.message(Command("help"))
# async def cmd_help(message: Message):
#     await message.answer("Help")


# @router.message(F.text == "Catalog")
# async def catalog(message: Message):
#     await message.answer("Choose category", reply_markup=kb.catalog)


# @router.callback_query(F.data == "shoes")
# async def shoes(callback: CallbackQuery):
#     await callback.answer("You choosed shoes")
#     await callback.message.answer("You choosed shoes")


# @router.message(Command("register"))
# async def register(message: Message, state: FSMContext):
#     await message.answer("Enter your name")
#     await state.set_state(Register.name)


# @router.message(Register.name)
# async def register_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("Enter your age")
#     await state.set_state(Register.age)


# @router.message(Register.age)
# async def register_age(message: Message, state: FSMContext):
#     await state.update_data(age=message.text)
#     await message.answer("Enter your number", reply_markup=kb.user_number)
#     await state.set_state(Register.number)


# @router.message(Register.number, F.contact)
# async def register_number(message: Message, state: FSMContext):
#     await state.update_data(number=message.contact.phone_number)
#     await message.answer("Registration completed")
#     data = await state.get_data()
#     await message.answer(
#         f"Name: {data['name']}\nAge: {data['age']}\nNumber: {data['number']}",
#         reply_markup=kb.main,
#     )
#     await state.clear()
