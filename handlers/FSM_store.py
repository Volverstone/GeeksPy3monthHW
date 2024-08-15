from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
kb = types.ReplyKeyboardRemove()
class FSM_store(StatesGroup):
    product = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    out = State()


async def fsm_start(message: types.Message):
    await message.answer(text='Здравствуйте, вы перешли в раздел покупок \n'
                              'Введите название товара:\n\n'
                              'Для возвращения назад/отмены,\n '
                              'нажмите на "Отмена"!', reply_markup=buttons.cancel)
    await FSM_store.product.set()


async def load_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите свой размер:'
                         ,reply_markup=buttons.size_panel)


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите категорию:',
                         reply_markup=buttons.cancel)


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите цену товара:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await FSM_store.next()
    await message.answer(text='Отправьте фотографию желаемого товара:')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await message.answer_photo(photo=data['photo'])
    await FSM_store.next()
    await message.answer(text='Верны ли данные?:',
                        reply_markup=buttons.question)

async def out(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pass
    answ = message.text



    if answ == "Да":
        await message.answer_photo(photo=data['photo'],
                                   caption=f"Ваше товар - {data['product']}\n"
                                           f"размер - {data['size']}\n"
                                           f"категория - {data['category']}\n"
                                           f"цена - {data['price']}\n"

                                   )
        await message.answer(text='Данные сохранены', reply_markup=kb)
        await state.finish()
    elif answ == "Нет":
        await message.answer(text='Данные не сохранены, сброс', reply_markup=kb)
        await state.finish()





async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено!',
                             reply_markup=kb)


def register_fsm_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True),
                                                 state="*")

    dp.register_message_handler(fsm_start, commands=['store'])
    dp.register_message_handler(load_product, state=FSM_store.product)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_photo, state=FSM_store.photo,
                                content_types=['photo'])
    dp.register_message_handler(out,state=FSM_store.out)
