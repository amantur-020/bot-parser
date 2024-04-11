from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
from functions import parse
from keyboards import reply
from .state import Form
from functions import parse
from aiogram import Router
import asyncio
from functions.parse import stop_parser


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f'Приветствую {message.from_user.first_name} !', reply_markup=reply.search_kb)

@router.message(F.text == '🔍 Начать поиск')
async def start_search(message: Message, state: FSMContext):
    await state.set_state(Form.city)
    await message.answer('Введите (город-район):', reply_markup=reply.cancel_kb)

@router.message((F.text == 'Остановить') | (F.text == 'Отменить'))
async def cancel_process(message:Message,state:FSMContext):
    with open('count.txt', 'w') as file:
        file.write("0")
    stop_parser()
    await state.clear()
    await message.answer('Вы вышли в главную страницу',reply_markup=reply.search_kb)

@router.message(Form.city)
async def add_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text.replace(' ', '-').lower())
    await state.set_state(Form.type_ads)
    await message.answer('Выберите тип(аренда, продажа):', reply_markup=reply.type_kb)


@router.message(Form.type_ads)
async def add_type(message: Message, state: FSMContext):
    if message.text == 'Аренда':
        await state.update_data(type_ads='izdavanje')
    elif message.text == 'Продажа':
        await state.update_data(type_ads='prodaja')
    await state.set_state(Form.type_housing)
    await message.answer('Выберите тип недвижимости:', reply_markup=reply.type_housing_kb)

@router.message(Form.type_housing)
async def add_type_housing(message: Message, state: FSMContext):
    if message.text == 'Квартира':
        await state.update_data(type_housing='stanova')
    elif message.text == 'Комната':
        await state.update_data(type_housing='soba')
    elif message.text == 'Дом':
        await state.update_data(type_housing='kuca')
    elif message.text == 'Гараж':
        await state.update_data(type_housing='garaza')
    elif message.text == 'Земля':
        await state.update_data(type_housing='zemljista')
    elif message.text == 'Местный':
        await state.update_data(type_housing='lokala')
    elif message.text == 'Офис/Комерческое помещение':
        await state.update_data(type_housing='kancelarijskog-prostora')
    elif message.text == 'Бизнес-Здание':
        await state.update_data(type_housing='poslovnih-zgrada')
    elif message.text == 'Зал':
        await state.update_data(type_housing='hala')
    elif message.text == 'Склад':
        await state.update_data(type_housing='magacina')
    elif message.text == 'Объект общественного питание':
        await state.update_data(type_housing='ugostiteljskih-objekata')
    elif message.text == 'Киоск':
        await state.update_data(type_housing='kioska')
    elif message.text == 'Склад':
        await state.update_data(type_housing='stovarista')
    await state.set_state(Form.price_from)
    await message.answer('Введите цену от:', reply_markup=reply.cancel_kb)

@router.message(Form.price_from)
async def add_price_from(message: Message, state: FSMContext):
    await state.update_data(price_from=message.text)
    await state.set_state(Form.price_to)
    await message.answer('Введите цену до:', reply_markup=reply.cancel_kb)

@router.message(Form.price_to)
async def add_price_to(message: Message, state: FSMContext):
    await state.update_data(price_to=message.text)
    data = await state.get_data() 
    chat_id = message.chat.id
    asyncio.create_task(parse.parser(chat_id=chat_id, **data))   

   

