from aiogram import Router
from aiogram.fsm.state import State, StatesGroup


router = Router()

class Form(StatesGroup):
    city = State()
    type_ads = State()
    type_housing = State()
    price_from = State()
    price_to = State()



