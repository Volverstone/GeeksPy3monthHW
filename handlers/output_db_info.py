from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import buttons
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import db_main

class FSM_store(StatesGroup):
    save = State()


async def fsm_start(message: types.Message):
    await message.answer(text='Введите айди товара(не артикул): ',
                         reply_markup=buttons.cancel)
    await FSM_store.save.set()

async def save(message: types.Message,state: FSMContext):
    await message.answer(db_main.sql_get_info(id=message.text))

    await state.finish()


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено!')


def db_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True),
                                                    state="*")

    dp.register_message_handler(fsm_start, commands=['db_out'])
    dp.register_message_handler(save, state=FSM_store.save)


