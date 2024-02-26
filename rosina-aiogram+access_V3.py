import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6938380868:AAFiOIDWXdhDph53Y5Y-jlmziNf7Mrpo7Bo'  # Replace with your API token

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

sys_admin = '507891763'  # Replace with your admin Telegram ID

# List to store user IDs with full access
full_access_users = [507891763, 422964228]

# клавиатуры demo access
# клавиатуры demo access
# клавиатуры demo access

kb = InlineKeyboardMarkup(row_width=1)
btn_vacancy = InlineKeyboardButton(text='- Хто я?', callback_data='whoami_first')
kb.add(btn_vacancy)

kb0 = InlineKeyboardMarkup(row_width=1)
btn_question_1 = InlineKeyboardButton(text='Для кого підійде навчання?', callback_data='question_1')
btn_question_2 = InlineKeyboardButton(text='У якому форматі відбувається навчання?', callback_data='question_2')
btn_question_3 = InlineKeyboardButton(text='Чи підійде мені навчання, якщо я маю захворювання?', callback_data='question_3')
btn_question_4 = InlineKeyboardButton(text='Що якщо я не отримаю жодних результатів?', callback_data='question_4')
btn_question_5 = InlineKeyboardButton(text='У мене є розлад харчової поведінки, це навчання підійде для мене?', callback_data='question_5')
btn_buy = InlineKeyboardButton(text='BUY COURCE', callback_data='buy')
kb0.add(btn_question_1, btn_question_2, btn_question_3, btn_question_4, btn_question_5, btn_buy)

kb0_1 = InlineKeyboardMarkup(row_width=1)
btn_back = InlineKeyboardButton(text='◀️ Повернутись до запитань', callback_data='whoami')
kb0_1.add(btn_back)

kb0_2 = InlineKeyboardMarkup(row_width=1)
btn_buy_confirm = InlineKeyboardButton(text='перевірити оплату', callback_data='buy_check')
kb0_2.add(btn_buy_confirm)

# клавиатуры full access
# клавиатуры full access
# клавиатуры full access

# клавиатуры зміст

kb1_0_0 = InlineKeyboardMarkup(row_width=1)
kb1_0_1 = InlineKeyboardButton(text='Вступ', callback_data='start_course')
kb1_0_2 = InlineKeyboardButton(text='ЧАСТИНА 1. Основа', callback_data='to_chapter_1')
kb1_0_3 = InlineKeyboardButton(text='ЧАСТИНА 2. ДЕФІЦИТ КАЛОРІЙ.', callback_data='to_chapter_2')
kb1_0_4 = InlineKeyboardButton(text='ЧАСТИНА 3. БІЛОК', callback_data='to_chapter_3')
kb1_0_5 = InlineKeyboardButton(text='ЧАСТИНА 4. ЯК СКЛАСТИ СВІЙ РАЦІОН', callback_data='to_chapter_4')
kb1_0_6 = InlineKeyboardButton(text='ЧАСТИНА 5. СИТІСТЬ. ЧАС ЗАЛЕЖИТЬ ВІД ХАРАКТЕРУ ЇЖІ', callback_data='to_chapter_5')
kb1_0_7 = InlineKeyboardButton(text='ЧАСТИНА 6. ЧОМУ ТЯГНЕ НА СОЛОДКЕ?', callback_data='to_chapter_6')
kb1_0_8 = InlineKeyboardButton(text='ЧАСТИНА 7. ЦУКОР, ПРИХОВАНИЙ ЦУКОР І ПП ДЕСЕРТИ', callback_data='to_chapter_7')
kb1_0_9 = InlineKeyboardButton(text='ЧАСТИНА 8. ЯК ВТРИМАТИ СВОЮ ВАГУ НА ДОВГІ РОКИ', callback_data='to_chapter_8')
kb1_0_0.add(kb1_0_1, kb1_0_2, kb1_0_3, kb1_0_4, kb1_0_5, kb1_0_6, kb1_0_7, kb1_0_8, kb1_0_9)

# клавиатуры вступ

kb1_0 = InlineKeyboardMarkup(row_width=1)
start_course = InlineKeyboardButton(text='Почати', callback_data='start_course')
kb1_0.add(start_course)

kb1_1 = InlineKeyboardMarkup(row_width=1)
to_message_1_2 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_2')
kb1_1.add(to_message_1_2)

kb1_2 = InlineKeyboardMarkup(row_width=2)
start_course = InlineKeyboardButton(text='Повернутись', callback_data='start_course')
to_message_1_3 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_3')
kb1_2.add(start_course, to_message_1_3)

kb1_3 = InlineKeyboardMarkup(row_width=2)
to_message_1_2 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_2')
to_message_1_4 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_4')
kb1_3.add(to_message_1_2, to_message_1_4)

kb1_4 = InlineKeyboardMarkup(row_width=2)
to_message_1_3 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_3')
to_message_1_5 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_5')
kb1_4.add(to_message_1_3, to_message_1_5)

kb1_5 = InlineKeyboardMarkup(row_width=2)
to_message_1_4 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_4')
to_message_1_6 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_6')
kb1_5.add(to_message_1_4, to_message_1_6)

kb1_6 = InlineKeyboardMarkup(row_width=2)
to_message_1_5 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_5')
to_message_1_7 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_7')
kb1_6.add(to_message_1_5, to_message_1_7)

kb1_7 = InlineKeyboardMarkup(row_width=2)
to_message_1_6 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_6')
to_message_1_8 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_8')
kb1_7.add(to_message_1_6, to_message_1_8)

kb1_8 = InlineKeyboardMarkup(row_width=2)
to_message_1_7 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_7')
to_message_1_9 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_9')
kb1_8.add(to_message_1_7, to_message_1_9)

kb1_9 = InlineKeyboardMarkup(row_width=2)
kb1_9_case_1 = InlineKeyboardButton(text='Приклад 1', callback_data='1_9_case_1')
kb1_9_case_2 = InlineKeyboardButton(text='Приклад 2', callback_data='1_9_case_2')
to_message_1_8 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_8')
to_message_1_10 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_10')
kb1_9.add(kb1_9_case_1)
kb1_9.add(kb1_9_case_2)
kb1_9.add(to_message_1_8, to_message_1_10)

kb1_9_case = InlineKeyboardMarkup(row_width=1)
to_message_1_9 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_9')
kb1_9_case.add(to_message_1_9)

kb1_10 = InlineKeyboardMarkup(row_width=2)
to_message_1_9 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_9')
to_message_1_11 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_11')
kb1_10.add(to_message_1_9, to_message_1_11)

kb1_11 = InlineKeyboardMarkup(row_width=2)
to_message_1_10 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_10')
to_message_1_12 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_12')
kb1_11.add(to_message_1_10, to_message_1_12)

kb1_12 = InlineKeyboardMarkup(row_width=2)
to_message_1_11 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_11')
to_message_1_13 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_13')
kb1_12.add(to_message_1_11, to_message_1_13)

kb1_13 = InlineKeyboardMarkup(row_width=2)
to_message_1_12 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_12')
to_message_1_14 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_14')
kb1_13.add(to_message_1_12, to_message_1_14)

kb1_14 = InlineKeyboardMarkup(row_width=2)
to_message_1_13 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_13')
to_message_1_15 = InlineKeyboardButton(text='Далі', callback_data='to_message_1_15')
kb1_14.add(to_message_1_13, to_message_1_15)

kb1_15 = InlineKeyboardMarkup(row_width=2)
to_message_1_14 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_1_14')
to_chapter_1 = InlineKeyboardButton(text='Перейти до наступної глави', callback_data='to_chapter_1')
kb1_15.add(to_message_1_14, to_chapter_1)

# клавиатуры ЧАСТИНА 1. Основа

kb2_1 = InlineKeyboardMarkup(row_width=1)
to_message_2_1 = InlineKeyboardButton(text='Далі', callback_data='to_message_2_2')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb2_1.add(to_message_2_1, contents)

kb2_2 = InlineKeyboardMarkup(row_width=2)
to_message_2_1 = InlineKeyboardButton(text='Повернутись', callback_data='to_chapter_1')
to_message_2_3 = InlineKeyboardButton(text='Далі', callback_data='to_message_2_3')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb2_2.add(to_message_2_1, to_message_2_3, contents)

kb2_3 = InlineKeyboardMarkup(row_width=2)
to_message_2_2 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_2_2')
to_chapter_2 = InlineKeyboardButton(text='Далі', callback_data='to_chapter_2')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb2_3.add(to_message_2_2, to_chapter_2, contents)

# клавиатуры ЧАСТИНА 2. ДЕФІЦИТ КАЛОРІЙ.

kb3_1 = InlineKeyboardMarkup(row_width=2)
to_message_2_3 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_2_3')
to_message_3_2 = InlineKeyboardButton(text='Далі', callback_data='to_message_3_2')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb3_1.add(to_message_2_3, to_message_3_2, contents)

kb3_2 = InlineKeyboardMarkup(row_width=2)
to_chapter_2 = InlineKeyboardButton(text='Повернутись', callback_data='to_chapter_2')
to_message_3_3 = InlineKeyboardButton(text='Далі', callback_data='to_message_3_3')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb3_2.add(to_chapter_2, to_message_3_3, contents)

kb3_3 = InlineKeyboardMarkup(row_width=2)
to_message_3_2 = InlineKeyboardButton(text='Далі', callback_data='to_message_3_2')
to_message_3_4 = InlineKeyboardButton(text='Далі', callback_data='to_message_3_4')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb3_3.add(to_message_3_2, to_message_3_4, contents)

kb3_4 = InlineKeyboardMarkup(row_width=2)
kb3_4_case_1 = InlineKeyboardButton(text='Приклад', callback_data='3_4_case_1')
to_message_3_3 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_3_3')
to_message_3_5 = InlineKeyboardButton(text='Далі', callback_data='to_message_3_5')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb3_4.add(kb3_4_case_1)
kb3_4.add(to_message_3_3, to_message_3_5)
kb3_4.add(contents)

kb3_4_case_1 = InlineKeyboardMarkup(row_width=1)
to_message_3_4 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_3_4')
kb3_4_case_1.add(to_message_3_4)

kb3_5 = InlineKeyboardMarkup(row_width=2)
to_message_3_4 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_3_4')
to_message_3_6 = InlineKeyboardButton(text='Далі', callback_data='to_message_3_6')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb3_5.add(to_message_3_4, to_message_3_6, contents)

kb3_6 = InlineKeyboardMarkup(row_width=2)
to_message_3_5 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_3_5')
to_chapter_3 = InlineKeyboardButton(text='Далі', callback_data='to_chapter_3')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb3_6.add(to_message_3_5, to_chapter_3, contents)

# клавиатуры ЧАСТИНА 3. БІЛОК.

kb4_1 = InlineKeyboardMarkup(row_width=2)
to_message_3_6 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_3_6')
to_message_4_2 = InlineKeyboardButton(text='Далі', callback_data='to_message_4_2')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_1.add(to_message_3_6, to_message_4_2, contents)

kb4_2 = InlineKeyboardMarkup(row_width=2)
to_chapter_3 = InlineKeyboardButton(text='Повернутись', callback_data='to_chapter_3')
to_message_4_3 = InlineKeyboardButton(text='Далі', callback_data='to_message_4_3')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_2.add(to_chapter_3, to_message_4_3, contents)

kb4_3 = InlineKeyboardMarkup(row_width=2)
kb4_3_case_1 = InlineKeyboardButton(text='Приклад', callback_data='4_3_case_1')
to_message_4_2 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_2')
to_message_4_4 = InlineKeyboardButton(text='Далі', callback_data='to_message_4_4')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_3.add(kb4_3_case_1)
kb4_3.add(to_message_4_2, to_message_4_4)
kb4_3.add(contents)

kb4_3_case_1 = InlineKeyboardMarkup(row_width=1)
to_message_4_3 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_3')
kb4_3_case_1.add(to_message_4_3)

kb4_4 = InlineKeyboardMarkup(row_width=2)
to_message_4_3 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_3')
to_message_4_5 = InlineKeyboardButton(text='Далі', callback_data='to_message_4_5')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_4.add(to_message_4_3, to_message_4_5, contents)

kb4_5 = InlineKeyboardMarkup(row_width=2)
to_message_4_4 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_4')
to_message_4_6 = InlineKeyboardButton(text='Далі', callback_data='to_message_4_6')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_5.add(to_message_4_4, to_message_4_6, contents)

kb4_6 = InlineKeyboardMarkup(row_width=2)
to_message_4_5 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_5')
to_message_4_7 = InlineKeyboardButton(text='Далі', callback_data='to_message_4_7')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_6.add(to_message_4_5, to_message_4_7, contents)

kb4_7 = InlineKeyboardMarkup(row_width=2)
to_message_4_6 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_6')
to_message_4_8 = InlineKeyboardButton(text='Далі', callback_data='to_message_4_8')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_7.add(to_message_4_6, to_message_4_8, contents)

kb4_8 = InlineKeyboardMarkup(row_width=2)
to_message_4_7 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_7')
to_message_4_9 = InlineKeyboardButton(text='Далі', callback_data='to_message_4_9')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_8.add(to_message_4_7, to_message_4_9, contents)

kb4_9 = InlineKeyboardMarkup(row_width=2)
to_message_4_8 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_8')
to_chapter_4 = InlineKeyboardButton(text='Далі', callback_data='to_chapter_4')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb4_9.add(to_message_4_8, to_chapter_4, contents)

# клавиатуры ЧАСТИНА 4. ЯК СКЛАСТИ СВІЙ РАЦІОН.

kb5_1 = InlineKeyboardMarkup(row_width=2)
to_message_4_9 = InlineKeyboardButton(text='Повернутись', callback_data='to_message_4_9')
to_chapter_5 = InlineKeyboardButton(text='Далі', callback_data='to_chapter_5')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb5_1.add(to_message_4_9, to_chapter_5, contents)

# клавиатуры ЧАСТИНА 5. СИТІСТЬ. ЧАС ЗАЛЕЖИТЬ ВІД ХАРАКТЕРУ ЇЖІ.

kb6_1 = InlineKeyboardMarkup(row_width=2)
to_chapter_4 = InlineKeyboardButton(text='Повернутись', callback_data='to_chapter_4')
to_chapter_6 = InlineKeyboardButton(text='Далі', callback_data='to_chapter_6')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb6_1.add(to_chapter_4, to_chapter_6, contents)

# клавиатуры ЧАСТИНА 6. ЧОМУ ТЯГНЕ НА СОЛОДКЕ?

kb7_1 = InlineKeyboardMarkup(row_width=2)
to_chapter_5 = InlineKeyboardButton(text='Повернутись', callback_data='to_chapter_5')
to_chapter_7 = InlineKeyboardButton(text='Далі', callback_data='to_chapter_7')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb7_1.add(to_chapter_5, to_chapter_7, contents)

# клавиатуры ЧАСТИНА 7. ЦУКОР, ПРИХОВАНИЙ ЦУКОР І ПП ДЕСЕРТИ.

kb8_1 = InlineKeyboardMarkup(row_width=2)
to_chapter_6 = InlineKeyboardButton(text='Повернутись', callback_data='to_chapter_6')
to_chapter_8 = InlineKeyboardButton(text='Далі', callback_data='to_chapter_8')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb8_1.add(to_chapter_6, to_chapter_8, contents)

# клавиатуры ЧАСТИНА 8. ЯК ВТРИМАТИ СВОЮ ВАГУ НА ДОВГІ РОКИ.

kb9_1 = InlineKeyboardMarkup(row_width=2)
to_chapter_7 = InlineKeyboardButton(text='Повернутись', callback_data='to_chapter_7')
to_message_9_2 = InlineKeyboardButton(text='Далі', callback_data='to_message_9_2')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb9_1.add(to_chapter_7, to_message_9_2, contents)

kb9_2 = InlineKeyboardMarkup(row_width=1)
to_chapter_8 = InlineKeyboardButton(text='Повернутись', callback_data='to_chapter_8')
contents = InlineKeyboardButton(text='Зміст', callback_data='contents')
kb9_2.add(to_chapter_8, contents)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Вітаю тебе! \n\nВ цьому навчанні я даю максимально ефективну інформацію та цінні знання, які залишаться з тобою на протязі всього життя. \n⁃ Харчуватися без обмежень \n⁃ Розбиратися в продуктах та отримувати з них максимальну цінність \n⁃ Зможеш досягти своєї мети, без шкоди для психічного та фізичного стану. \n⁃ Здобудеш нові, класні звички \n⁃ Позбавишся РПП",
        reply_markup=kb
    )

@dp.message_handler(lambda message: message.chat.type == 'private', content_types=['text', 'photo'])
async def forward(message: types.Message):
    msg = f"ID {message.from_user.id}\nПользователь @{message.from_user.username} написал: {message.text}"
    await bot.send_message(sys_admin, msg)

# Функция callback_query_handler вносится один раз для обработки всех событий
@dp.callback_query_handler(lambda call: True)
async def answer(call: types.CallbackQuery):
    if call.data == 'whoami_first':
        await bot.send_message(call.message.chat.id, 'Мене звати Росіна, я сертифікований і практикуючий нутріціолог. Почала свій шлях з того, що захопилася цим напрямком для себе, оскільки довгий час була незадоволена своїм тілом, здоров\'ям та станом організму. Сиділа на різних дієтах, змушувала себе займатися спортом, але результату все ніяк не помічала, вага снижувалася, згодом поверталась, тілом так само була незадоволена, і так все тривало по колу. \n\nНа сьогоднішній день, для мене нутриціологія стала способом життя, я позбулася старих шкідливих звичок, пройшла через зриви, прикрощі, набряки, недосипання, стрес, РПП. І тепер готова поділитися з вами перевіреними навіть на мені, дієвими, надійними знаннями, які стануть фундаментом та основою реального результату. \n\nЯ знаю, як важко буває досягти своїх цілей, особливо коли навколо стільки інформації, марафонів, фітнес-блогерів, а ти вже перепробував майже всі варіанти дієт, ЯКІ НЕ ПРАЦЮЮТЬ, або тимчасовий результат, зіпсоване здоров\'я і витрачений час. \n\nМоє завдання – це не обмежувати тебе в їжі та розказати, що не потрібно демонізувати продукти. \n\nБільш детально ознайомишся з тим, що ти їж і п\'єш. Тому, після навчання ви зможете усвідомлено підходити до свого раціону та здоров\'я. Дізнаєтеся про найпоширеніші помилки при схудненні, як правильно розрахувати добову норму їжі, зрозумієте принципи здорового харчування, як правильно вибирати продукти і як сформувати свій раціон. \n\nВажливо стежити за своїм прогресом, і звичайно ж мати терпіння, тому що результат потребує часу та завзятості.')
        with open('files/start.png', 'rb') as photo:
            await bot.send_photo(call.message.chat.id, photo)
        await bot.send_message(call.message.chat.id, 'Можливі запитання', reply_markup=kb0)

    if call.data == 'whoami':
        await bot.send_message(call.message.chat.id, 'Можливі запитання', reply_markup=kb0)

    elif call.data == 'question_1':
        await bot.send_message(call.message.chat.id,
                               "Для кого підійде навчання? \n\n⁃ Для тих, хто хоче схуднути здоровим та ЕФЕКТИВНИМ способом. \n⁃ Для тих, хто бажає розібратися зі своїм раціоном та почати дбати про своє здоров'я. \n⁃ Хто втомився сидіти в обмеженнях, дієтах і постійно відчуває голод. \n⁃ Для тих, хто хоче дізнатися про принципи здорового харчування, покращити свій стан, налагодити свій режим.",
                               parse_mode='Markdown', reply_markup=kb0_1)

    elif call.data == 'question_2':
        await bot.send_message(call.message.chat.id,
                               "У якому форматі відбувається навчання? \n\n⁃ Навчання створено у текстовому форматі, тобто ви одразу отримуєте готову інформацію з вічним доступом. \n⁃ Вся інформація зібрана у простому та зрозумілому варіанті, включаючи: зображення, таблиці та формули. Незабаром до кожного розділу будуть ще додаткові відео.",
                               parse_mode='Markdown', reply_markup=kb0_1)

    elif call.data == 'question_3':
        await bot.send_message(call.message.chat.id,
                               "Чи підійде мені навчання, якщо я маю захворювання? \n\n⁃ Взагалі харчування є найбільш ефективною формою лікування будь-якого захворювання. Тому буде корисно дізнатися не лише з метою схуднення, а насамперед, як побудувати здоровий та збалансований раціон.",
                               parse_mode='Markdown', reply_markup=kb0_1)

    elif call.data == 'question_4':
        await bot.send_message(call.message.chat.id,
                               "Що якщо я не отримаю жодних результатів? \n\n⁃ Гарантую, якщо ви дотримуватиметеся всіх рекомендацій і пройдете навчання до кінця, то ви отримаєте результат. \n\nЦе чиста фізіологія та наука. Будьте готові, що організму потрібен час на перебудову, дайте собі час і дотримуйтесь рекомендацій.",
                               parse_mode='Markdown', reply_markup=kb0_1)

    elif call.data == 'question_5':
        await bot.send_message(call.message.chat.id,
                               "У мене є розлад харчової поведінки, це навчання підійде для мене? \n\n⁃ Так! Якби на початку мого шляху, я пройшла це навчання, то не мучила б роками свій організм. Ви дізнаєтеся, як працює наше тіло, як воно засвоює їжу, що таке вуглеводи, білки, жири. Про те, що їсти, можна і потрібно, навіть при схудненні.",
                               parse_mode='Markdown', reply_markup=kb0_1)
    
    elif call.data == 'buy':
        await bot.send_message(call.message.chat.id,"Для покупки треба написати менеджеру",
                               parse_mode='Markdown', reply_markup=kb0_2)

    elif call.data == 'number':
        keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = KeyboardButton(text="Відправити!", request_contact=True)
        keyboard.add(button_phone)
        await bot.send_message(call.message.chat.id, '⬇️Відправ свій номер⬇️', reply_markup=keyboard)

    elif call.data == 'buy_check':
        user_id = call.from_user.id
        if user_id in full_access_users:
            # User has access to the course, send course messages
            await bot.send_message(user_id, "Почати курс!", parse_mode='Markdown', reply_markup=kb1_0)
        else:
            await bot.send_message(user_id, "Доступ відхилено. Зверніться до менеджера для отримання доступу.")
    
#запросы для full access
#запросы для full access
#запросы для full access
            
    #запросы зміст
    
    elif call.data == 'contents':
        await bot.send_message(call.message.chat.id,"Зміст курсу",
                               parse_mode='Markdown', reply_markup=kb1_0_0)
            
    #запросы вступ

    elif call.data == 'start_course':
        await bot.send_message(call.message.chat.id,"Вітаю! \nНасамперед хотіла б сказати, що дуже пишаюся тобою. Перший крок завжди зробити складніше, але після нього не буде шляху назад. \nЯ підготувала для тебе це навчання з турботою, щоб наблизити тебе до твоєї мрії. \n\nНавчання написано у дуже простій, інтерактивній та зрозумілій формі, але при цьому глибоко та інформативно розкриває всі функції нашого організму.",
                               parse_mode='Markdown', reply_markup=kb1_1)
        
    elif call.data == 'to_message_1_2':
        await bot.send_message(call.message.chat.id,"Отже, вся інформація, яка представлена тут, допоможе вам побудувати міцний фундамент знань, який завжди підтримуватиме ваше тіло та здоров'я у чудовому стані.",
                               parse_mode='Markdown', reply_markup=kb1_2)
    
    elif call.data == 'to_message_1_3':
        await bot.send_message(call.message.chat.id,"Не будемо орієнтуватися на заміри та вагу. \nНаприкінці шляху - ви відчуєте свій результат і пишатиметеся собою. \n\nПам'ятайте, що зміни починаються всередині нас поступово. \nПроблеми у відносинах із їжею завжди починаються з голови. Ми засвоюємо різну інформацію, але, на жаль, не завжди достовірну. Якщо розглядати тему харчування, то не можна говорити про користь чи шкоду якогось конкретного продукту. Раціон необхідно оцінювати повністю, включаючи абсолютно всі його складові.",
                               parse_mode='Markdown', reply_markup=kb1_3)
    
    elif call.data == 'to_message_1_4':
        await bot.send_message(call.message.chat.id,"Перше, що ми можемо собі зробити - це поставити 2 проміжні цілі на перший тиждень навчання. Точки мети мають бути досяжні, і без різких обмежень для себе, це може бути у сфері спорту та харчування. \n\nНаприклад: \n- протягом 7 днів я суворо дотримуюся режиму сну і лягаю спати не пізніше 23:00. \n- Протягом 7 днів після пробудження я роблю розминку. \n\nТак як за 7 днів результат ще не побачите, раджу ставити проміжні цілі мінімум на місяць, далі це увійде у звичку. (Головне пам ятати для чого ви це робите). \n\nА також поставити 2 цілі за винятком. \n\nНаприклад: \n- Протягом тижня я виключаю зі свого раціону цукор у чистому вигляді. (Цукерки, мед, тістечка). \n- Протягом тижня я виключаю борошняну продукцію. (При цьому – замінити на альтернативні варіанти). \n\nВажливо дотримуватись і не пропускати свої поставлені проміжні цілі. Тому що, тільки маленькими, але впевненими кроками, ви зможете дійти до якісного результату, здорового тіла та усвідомленого харчування без обмежень. \nЗапитаєте, чому без обмежень, коли вводите виняток на тиждень? Відповідь якраз криється у наших знаннях та звичках. З часом, пройшовши це навчання, ви дійсно зрозумієте, що можна їсти все, не обмежуючи себе в солоному, солодкому, борошняному тощо. ",
                               parse_mode='Markdown', reply_markup=kb1_4)
    
    elif call.data == 'to_message_1_5':
        await bot.send_message(call.message.chat.id,"МИ - ТЕ, ЩО МИ ЇМО \n\nУ більшості випадків ми починаємо думати про здорові звички тільки тоді, коли помічаємо проблеми з вагою, зовнішнім виглядом та здоров'ям. Однак відомо, що розвиток багатьох захворювань та зниження імунітету людини часто пов'язані з хаотичним та неповноцінним харчуванням. \nТому для початку ми розберемо, як працює звичка і для чого вона нам потрібна.",
                               parse_mode='Markdown', reply_markup=kb1_5)
    
    elif call.data == 'to_message_1_6':
        await bot.send_message(call.message.chat.id,"Здоров'я - це процес, який складається із щоденних дій, а не з тих, що ви робили вчора, або збираєтесь робити завтра.",
                               parse_mode='Markdown', reply_markup=kb1_6)
    
    elif call.data == 'to_message_1_7':
        await bot.send_message(call.message.chat.id,"Як формується наша звичка? \n\n⁃ Мета (ви прописуєте собі ціль на період навчання), щотижня їх можна міняти. \n⁃ Винагорода (бачите проміжний результат). \n⁃ Автоматизм (вироблена звичка, що вже виконується з легкістю).",
                               parse_mode='Markdown', reply_markup=kb1_7)
    
    elif call.data == 'to_message_1_8':
        await bot.send_message(call.message.chat.id,"ЗНАЧЕННЯ ЇЖІ ТА НУТРІТИВНА ЦІННІСТЬ \n\nОсновні харчові інгредієнти: білки, жири, вуглеводи, вітаміни та мінерали. Це дає будівельний матеріал для ферментів і гормонів, що забезпечують роботу нашого організму, а також для побудови та відновлення наших клітин, органів та тканин. \n\nЛюдський організм можна порівняти з автомобілем. \n\nЧим якісніше паливо, тим довше прослужить машина. Людське тіло – це та сама машина – чим якісніша їжа, тим міцніше наше здоров'я, і тим довше зберігається наша молодість. Їжа є джерелом енергії, вітамінів, мінералів, макро та мікроелементів, а також багатьох інших необхідних речовин. Хаотичне харчування негативно впливає на здоров'я людини. Переїдання або недостатнє споживання поживних речовин призводить до підвищеної стомлюваності, зниження працездатності, ослаблення імунітету і навіть провокує передчасне старіння. \n\n80% нашого раціону повинно складатися з продуктів, які мають нутритивну цінність. Тільки тоді ми отримаємо результат.",
                               parse_mode='Markdown', reply_markup=kb1_8)
    
    elif call.data == 'to_message_1_9':
        await bot.send_message(call.message.chat.id,"Усі продукти харчування можна розділити на нутрітивно цінні та не нутрітивно цінні. \nЯк визначити НЦ продукту: \n\nРозберемо 2 сніданки з однаковою калорійністю, але різною НЦ. \n\n1 бал - ставимо продуктам з високою НЦ \n0 балів - ставимо продуктам зі зниженною НЦ",
                               parse_mode='Markdown', reply_markup=kb1_9)
    
    elif call.data == '1_9_case_1':
        await bot.send_message(call.message.chat.id,"(Картинка) \n\nГранола з молоком - 0 \nСухофрукти - 0 \nЯгоди з горіхами - 1 \nЦЗ хліб - 0 \nВершкове масло - 1 \nСклянка апельсинового фрешу - 0",
                               parse_mode='Markdown', reply_markup=kb1_9_case)
    
    elif call.data == '1_9_case_2':
        await bot.send_message(call.message.chat.id,"(Картинка) \n\nЦілісна вівсяна крупа зварена на воді - 1 \nЯгоди, горіхи - 1 \nЯйце - 1 \nЦЗ хліб - 0 \nАвокадо - 1 \nЗелень - 1",
                               parse_mode='Markdown', reply_markup=kb1_9_case)
    
    elif call.data == 'to_message_1_10':
        await bot.send_message(call.message.chat.id,"Отже, у першому прикладі ми маємо сніданок із невеликою нутрітивною цінністю, та простими вуглеводами, які швидко призведуть до голоду. \n\nУ другому прикладі в нас вийшов нутрітивно цінний сніданок, який принесе нам більше користі, енергії та тривалої ситості.",
                               parse_mode='Markdown', reply_markup=kb1_10)
    
    elif call.data == 'to_message_1_11':
        await bot.send_message(call.message.chat.id,"ПЕРЕЖОВУВАННЯ \n\nПам'ятайте, що цінність деяких продуктів знижується, навіть якщо оцінювалися в 1 бал, через те, що погано пережували. Мало хто про це замислюється, але первісне розщеплення починається у роті. У слині знаходиться важливий фермент, який називається слинна амілаза, він відповідає за засвоєння всіх вуглеводів. І чим більше за нас працюють блендери, комбайни, тим менше ми даємо можливість нашим бактеріям та ферментам подрібнювати ці продукти, користь знижується.",
                               parse_mode='Markdown', reply_markup=kb1_11)
        
    elif call.data == 'to_message_1_12':
        await bot.send_message(call.message.chat.id,"БЕЗКОРИСНА ЇЖА ВКЛЮЧАЄ НАСТУПНІ ПРОДУКТИ: \n\nМарна їжа - це все, що не приносить жодної користі вашому організму. \n\n- Заморожені напівфабрикати \n- Ковбасні вироби, шинка \n- Перероблені рибні продукти, крабові палички \n- Продукти, що містять хімічні інгредієнти: добавки, ароматизатори, підсолоджувачі, загусники, підсилювачі смаку \n- Бульйонні кубики, приправи зі складним складом \n- Снеки, чіпси, попкорн, сухарики \n- Стабілізатори та замінники цукру \n- Картопля фрі, сендвічі, бургери, пончики \n- Продукти, що містять трансжири: майонез, маргарин, спред, кулінарні олії, пальмова олія \n- Кондитерські десерти: торти, тістечка, муси, желе, збиті вершки \n- Хлібобулочні вироби з білого пшеничного борошна: батони, хліб, пироги, печиво, сухарики\n- Шоколадні вироби: батончики, солодощі, протеїнові батончики, продукти на фруктозі \n- Продукти швидкого приготування: каші швидкого приготування, пюре, локшина \n- Молочні продукти з 0% жирністю та фруктовими добавками: сирна маса, глазуровані сирки, солодкий йогурт \n- Соуси: кетчупи, сири та інші, що містять майонез, сою \n- Солодкі напої: пакетовані соки, газовані напої",
                               parse_mode='Markdown', reply_markup=kb1_12)
    
    elif call.data == 'to_message_1_13':
        await bot.send_message(call.message.chat.id,"При такому харчуванні можуть виникати запори, інтоксикації, а також порушується очищення кишківника та всього організму від поганого холестерину та шлаків. У кишечнику виникають процеси запалення та бродіння. \n\nВітамінів і мінералів теж не вистачатиме, тому що з такої їжі неможливо вичавити цінність.",
                               parse_mode='Markdown', reply_markup=kb1_13)
        
    elif call.data == 'to_message_1_14':
        await bot.send_message(call.message.chat.id,"«ХВОРОБУ ЛЕГШЕ ПОПЕРЕДИТИ, А НЕ ЛІКУВАТИ» \n\nТому правильне сприйняття принципів раціонального харчування має бути основою побудови нашої харчової поведінки та сприяти профілактиці захворювань, а не провокувати їхню появу. \n\n- Ми любимо їсти солодке, і дуже часто нас тягне на солодощі: випічку, шоколад, цукерки та тістечка, та іноді в нашому раціоні так багато простих вуглеводів і так мало нутрітивних продуктів, що містять вітаміни та мінерали, яких не вистачає нашому організму. \n\nВ цьому навчанні ми в жодному разі не заборонятимемо собі ті чи інші продукти, оскільки всі ми знаємо, що заборони не працюють. Ми розберемо причину, чому вас тягне до солодкого, і що з цим робити, а також поговоримо про приховані цукри.",
                               parse_mode='Markdown', reply_markup=kb1_14)
        
    elif call.data == 'to_message_1_15':
        await bot.send_message(call.message.chat.id,"«ПЕРЕД ТИМ ЯК ПОЧНЕТЕ, НЕОБХІДНО, ЩОБ ВИ ПОЗБУЛИСЯ ВІД НАСТУПНИХ ОЧІКУВАНЬ: \n\n⁃ Ідеальне тіло за 2 тижні, таблетки для схуднення, жироспалюючи продукти, обгортання і жиророзчинні засоби, дієти з нульовим вмістом жиру, голодування, і всі інші види дієт. \n\n⁃ ЧАРІВНОЇ ТАБЛЕТКИ НЕМАЄ! Максимум, що ви отримаєте від цих хворих способів - це тимчасовий ефект і втрату води. У гіршому випадку, будете схильні до розладів харчової поведінки, таких як анорексія, булімія, аменорея та інше, а також збої у гормональній системі. \nЗ естетичної точки зору дієти можуть призвести до в'ялості шкіри, появи розтяжок та целюліту. Отже, дуже важливо створити правильний дефіцит калорій, якщо буде потрібно, і правильний баланс білків, вуглеводів і жирів. \n\nДалі ви отримаєте чітку покрокову інструкцію, як екологічно позбутися зайвої ваги, стати здоровішим, і не збожеволіти від голоду, та як зберегти результат на довгі роки!",
                               parse_mode='Markdown', reply_markup=kb1_15)
        
    elif call.data == 'to_message_1_15':
        await bot.send_message(call.message.chat.id,"«ПЕРЕД ТИМ ЯК ПОЧНЕТЕ, НЕОБХІДНО, ЩОБ ВИ ПОЗБУЛИСЯ ВІД НАСТУПНИХ ОЧІКУВАНЬ: \n\n⁃ Ідеальне тіло за 2 тижні, таблетки для схуднення, жироспалюючи продукти, обгортання і жиророзчинні засоби, дієти з нульовим вмістом жиру, голодування, і всі інші види дієт. \n\n⁃ ЧАРІВНОЇ ТАБЛЕТКИ НЕМАЄ! Максимум, що ви отримаєте від цих хворих способів - це тимчасовий ефект і втрату води. У гіршому випадку, будете схильні до розладів харчової поведінки, таких як анорексія, булімія, аменорея та інше, а також збої у гормональній системі. \nЗ естетичної точки зору дієти можуть призвести до в'ялості шкіри, появи розтяжок та целюліту. Отже, дуже важливо створити правильний дефіцит калорій, якщо буде потрібно, і правильний баланс білків, вуглеводів і жирів. \n\nДалі ви отримаєте чітку покрокову інструкцію, як екологічно позбутися зайвої ваги, стати здоровішим, і не збожеволіти від голоду, та як зберегти результат на довгі роки!",
                               parse_mode='Markdown', reply_markup=kb1_15)
        
    #запросы ЧАСТИНА 1. Основа
    
    elif call.data == 'to_chapter_1':
        await bot.send_message(call.message.chat.id,"ЧАСТИНА 1. \nОснова \n\n⁃ Харчування становить 60% від вашого результату. \n⁃ Тренування – це ще 20% вашого результату, але просто вправи не допоможуть. Вони потрібні нам, щоб зробити наше тіло пружним та підтягнутим. \n⁃ Відновлення – 20% вашого результату. Якщо ви спите по 3-4 години вночі, у вас немає режиму і ви постійно відчуваєте стрес - забудьте про очікуємий результат! Саме тому більшість стопоряться у процесі і не отримують результату. Вони зазнають сильного стресу, відбувається гормональний збій. При цьому можуть збалансовано харчуватися та тренуватися.",
                               parse_mode='Markdown', reply_markup=kb2_1)
    
    elif call.data == 'to_message_2_2':
        await bot.send_message(call.message.chat.id,"Якщо харчуватися з дефіцитом калорій, але не тренуватися, то тіло незабаром буде виглядати дрябло і набуде дуже неестетичного вигляду. Вам це не потрібно. Вам потрібні м'язи, яких можна досягти в тренажерному залі чи вдома! \n\nЯкщо ви тренуєтеся, але ігноруєте харчування, ви не схуднете. Ви просто наростите м'язи під шаром жиру. Без належного дефіциту калорій ви не дістанетесь до своєї мети. \n\nЯкщо ви правильно харчуєтеся та тренуєтеся, але ігноруєте відпочинок та відновлення – це також зіграє у мінус!",
                               parse_mode='Markdown', reply_markup=kb2_2)
    
    elif call.data == 'to_message_2_3':
        await bot.send_message(call.message.chat.id,"Важливо! \n\nСпати потрібно 7-8 годин. Якщо ви погано виспалися – скасуйте тренування та уникайте стресів та перевтом, інакше ви можете отримати серйозні гормональні проблеми, зниження імунітету та ваш загальний стан може виявитися на межі депресії. Якщо не буде умов для повноцінного відпочинку, результати сповільняться. Було проведено безліч досліджень про те, що людям, яким не вистачає відпочинку та сну, вони починають доводити себе до переїдання та швидкого набору ваги. \n\nХАРЧУВАННЯ + ТРЕНУВАННЯ + СОН = РЕЗУЛЬТАТ! \n\nОкремо це не спрацює. \n\nДослідження показують, якщо ми будемо займатися хоча б 20 хвилин на день будь-яким фізичним навантаженням, яке включає наші м'язові волокна, при уьому ми виробляємо свої власні внутрішні антиоксиданти (супероксиддисмутазу, каталазу – ферменти, які захищають нас від окислення ліпідів та від старіння).",
                               parse_mode='Markdown', reply_markup=kb2_3)
        
    #запросы ЧАСТИНА 2. ДЕФІЦИТ КАЛОРІЙ.
    
    elif call.data == 'to_chapter_2':
        await bot.send_message(call.message.chat.id,"ЧАСТИНА 2. \nДЕФІЦИТ КАЛОРІЙ. \n\nЩоб почати спалювати жир, потрібний дефіцит калорій. \nІншими словами, важливо споживати менше енергії (їжі), ніж встигаєте витратити протягом дня. Все, що організм не встиг переробити на енергію, відкладається в жир. \n\nЩоб набрати вагу, потрібно споживати більше калорій, ніж ваше тіло використовує протягом дня. (Але це повинні бути якісні калоріі, здорової їжі) \nЩоб схуднути, вам потрібно споживати менше калорій, ніж спалює ваше тіло. Якщо ви витрачаєте та споживаєте однакову кількість, то не прогресуєте. \n\nПід час дефіциту калорій організм шукає додаткових джерел енергії, тому починає спалювати жирові клітини. Дефіцит потрібно правильно розраховувати і не надто різко, щоб спалювати жир, а не м'язи (що є стресовим станом для організму).",
                               parse_mode='Markdown', reply_markup=kb3_1)
    
    elif call.data == 'to_message_3_2':
        await bot.send_message(call.message.chat.id,"Багато людей, які хочуть схуднути, починають урізати занадто багато калорій і споживають близько 1000, 900 чи 800 калорій на день. Одні виключають усі жири, інші їдять лише білок, вважаючи вуглеводи злом та основним джерелом жирових відкладень. \nНЕ РОБІТЬ ЦЬОГО! \n\nЦе може призвести до випадіння волосся, втрати еластичності шкіри, погіршення загального стану здоров'я, збої в роботі органів, проблеми зі щитовидною залозою та гормонами, відсутність менструацій та ряд психологічних захворювань – анорексія, булімія тощо…",
                               parse_mode='Markdown', reply_markup=kb3_2)
        
    elif call.data == 'to_message_3_3':
        await bot.send_message(call.message.chat.id,"ЯК СТВОРИТИ ДЕФІЦИТ КАЛОРІЙ? \n\nЯкщо потрібно схуднути, то від загальної калорійності ми спочатку віднімаємо 5%, а після 1-2 тижні відстежуємо динаміку. Якщо динаміка позитивна, то розрахунки вірні і можна їм слідувати, доки вага не зупиниться. Може трапиться і таке, що вага зупинилася, а об єми йдуть. \nЦе також вважається позитивною динамікою. Має бути баланс! \n\nЯкщо на 5% дефіциту немає жодного результату, можна знизити ще на 5% (10% від спочатку розрахованої калорійності), але не опускати нижче 1600 ккал. \n\nЯкщо ви отримаєте 1600 ккал і нижче, то калорійність раціону не зменшуємо, а збільшуємо енерговитрати.  ",
                               parse_mode='Markdown', reply_markup=kb3_3)
    
    elif call.data == 'to_message_3_4':
        await bot.send_message(call.message.chat.id,"БЖУ - РОЗРАХУНКОВА ФОРМУЛА \n\nВсі люди відрізняються один від одного, тому кожній людині потрібна своя індивідуальна кількість калорій на день, щоб втрачати, набирати або підтримувати вагу. \n\nРозрахунок робиться досвідченим шляхом, а це означає, що потрібно експериментувати постійно. На прикладі далі розберемо одну з популярних формул. \n\nРозрахунок калорійності за формулою Харріса-Бенедикта: \n\nДля жінок: \nBMR = 447,6+(9,2 х вага(кг)) + (3,1 х зріст (см)) - (4,3 х вік(років)) \n\nДля чоловіків: \nBMR = 88,36 + (13,4 х вага (кг)) + (4,8 х зріст (см)) - (5,7 х вік (років)) \n\n  Далі отриману цифру калорійності ми множимо коефіцієнт активності. Дуже важливо правильно визначити свій коефіцієнт активності – не применшувати активність, а й не переоцінити свої енерговитрати. \n\n    ⁃ Мала активність, сидяча робота – 1,2 \n   ⁃ Легка активність (щоденні фізичні навантаження чи заняття спортом 1-3 рази на тиждень) – 1,375 \n ⁃ Середня активність (тренування 3-5 разів/тиждень) – 1,55 \n   ⁃ Активний спосіб життя (інтенсивні тренування, заняття 6-7 разів на тиждень) – 1,725 \n    ⁃ Професійні спортсмени – 1,9 \n\nДалі можно побачити приклад розрахунку➡️",
                               parse_mode='Markdown', reply_markup=kb3_4)
        
    elif call.data == '3_4_case_1':
        await bot.send_message(call.message.chat.id,"ПРИКЛАД: \n\nВага – 60 кг \nЗріст – 165см \nВік – 28 років \nРівень активності – легкі тренування 3 рази на тиждень \n\nПотім ми вводимо дані в нашу формулу: BMR = 447,6 + (9,2 х вага в кг) + (3,1 х зріст в см) – (4,3 х вік) \n\nЛШМ = 1390 ккал це наш базовий рівень метаболізму (BMR) \nЗгідно з дослідженнями, багато людей переоцінюють рівень своєї повсякденної активності та застрягають на цьому процесі. \nБільшість із них мають низький рівень добової активності. \nПотім ми множимо число BMR на Вашу активну швидкість метаболізму (AMR) \n\nДля нашого прикладу будемо використовувати легку активність \n\nОтримуємо загальну кількість - 1911кал. \nЦе кількість калорій, необхідне підтримки постійної ваги. \n\nМи не можемо засвоїти ту кількість енергії, яку споживаємо на 100%. Про це дуже важливо пам'ятати і не належить до розрахунків фанатично. Важливо приділяти особливу увагу як кількості, а й якості споживаних калорій. ",
                               parse_mode='Markdown', reply_markup=kb3_4_case_1)
        
    elif call.data == 'to_message_3_5':
        await bot.send_message(call.message.chat.id,"ВУГЛЕВОДИ, ЖИРИ, БІЛКИ. \nРОЗРАХУНОК: \n\nНаше здоров'я, фізична активність, настрій та зовнішній вигляд залежать від харчування, в основі якого лежить вічний закон природи – баланс усіх компонентів. \n\nНаша їжа складається з так званих нутрієнтів, їх співвідношення впливає на кількість корисних нутрієнтів у нашому організмі, збільшення або втрату ваги, загальне самопочуття. \n\nЯ рекомендую вам прибрати перекуси, щоб між повноцінними прийомами їжі були чисті проміжки. Так як під час перекусів відбувається додатковий стрибок інсуліну. \n\nЗапорукою здорового харчування є жири, білки та вуглеводи. \nРозраховуються у потрібній кількості та відсотках. При побудові здорового меню їх розраховують з огляду на загальну добову калорійність раціону. \n\nПоживні речовини є найважливішим «будівельним матеріалом» нашого організму. \nСпіввідношення яких впливає на кількість енергії, що отримується з їжею, і на те, як вона перероблятиметься організмом. \n\nВони поділяються на такі категорії: \n\nБілки – відповідають за зростання м'язів (м'ясо, риба, сир, яйця, горіхи тощо). \nЖири – контролюють гормональний баланс, роботу мозку, засвоєння вітамінів та вуглеводів – джерело глюкози, нашої енергії (олії, сир, горіхи, оливки, авокадо тощо) \nПоживні речовини відрізняються своєю енергетичною цінністю та впливом на організм. Для здорового харчування вам потрібно знати, скільки кожного з них вам потрібно включити до свого раціону з погляду калорій та відсоткового вмісту.",
                               parse_mode='Markdown', reply_markup=kb3_5)
    
    elif call.data == 'to_message_3_6':
        await bot.send_message(call.message.chat.id,"ДОБОВА НОРМА СПОЖИВАННЯ ПОЖИВНИХ РЕЧОВИН \n\nБілки: \n1 г/кг – низька активність \n1,5 г/кг – середня активність \n2 г/кг – інтенсивна активність \n\nЖири: \n0,9 г/кг – низька активність \n1 г/кг – середня активність \n1,2-1,5 г/кг – інтенсивна активність \n\nВуглеводи: \n2 г/кг – низька активність \n2,5-3 г/кг – середня активність \n3 та більше г/кг – інтенсивна активність \n\nЯкщо ви тренуєтеся 3 рази на тиждень, 2-3 грами вуглеводів на кг буде достатньо.",
                               parse_mode='Markdown', reply_markup=kb3_6)
        
    #запросы ЧАСТИНА 3. БІЛОК.
        
    elif call.data == 'to_chapter_3':
        await bot.send_message(call.message.chat.id,"ЧАСТИНА 3. \nБІЛОК. \n\nБілок – це найважливіший структурний компонент нашого організму. Це нашбудівельний матеріал. Усі білки можна розділити на 2 групи: прості та складні. \nФункції білка: \nОдна з основних функцій – це підтримка рідини, тобто крові в судині. \nБілки виробляють антитіла, які регулюють нашу імунну систему. \n\nЯкщо ми не доїдаємо, або прибираємо білки з раціону, їмо тільки вуглеводи та жирні кислоти, то частина вуглеводів використовується для того, щоб створити замінні амінокислоти. Вони будуються із глюкози. \n\nКоли ми не доїдаємо білок, або він погано засвоюється, організм страждає від таких порушень: \n⁃ Набряклість \n⁃ Низька імунна система \n⁃ Проблеми зі шкірою, нігтями та волоссям \n⁃ Дефіцити мікроелементів, білок виконує важливу транспортну функцію заліза, цинку, селену тощо. \n⁃ Гормональні порушення \n⁃ Зменшення м'язової тканини",
                               parse_mode='Markdown', reply_markup=kb4_1)
    
    elif call.data == 'to_message_4_2':
        await bot.send_message(call.message.chat.id,"Зниження вироблення соляної кислоти так само призводить до того, що частина білка не засвоюється. \nЩо стосується рослинних білків, засвоєння бобових, горіхів та круп набагато нижче, ніж білків тваринного походження, оскільки у складі вони мають більше захисних механізмів: клітковина, оболонка, антинутрієнти. \n\nДля веганів або вегетаріанців кількість рослинної їжі повинно бути збільшено, щоб отримувати свою необхідну порцію білка. \n\nМіф: м'ясо тяжке для шлунка. \n\nУ людей, які йдуть на веганство, перестають давати організму тваринний білок, соляна кислота починає знижуватися. А значить – це може призвести до зниження кислотності у шлунку. Тому, коли ви знову почнете вживати більше тваринних продуктів, то можете відчути тяжкість. При неприємних відчуттях після вживання м'яса, людям із традиційним типом харчування варто перевірити шлунок, а не прибирати тваринні продукти.",
                               parse_mode='Markdown', reply_markup=kb4_2)
    
    elif call.data == 'to_message_4_3':
        await bot.send_message(call.message.chat.id,"НОРМИ БІЛКУ: \nНа кілограм ваги не менше 0,8 г білка на добу (норма для тих, хто веде малоактивний спосіб життя). \nПри досить активному способі життя кількість білка має бути до 1,2-1,6г на кг. \n\nБілок дуже важливий для контролю ситості та правильної роботи ШКТ. А для того, щоб запустити нормальну роботу ЖКТ і гормонів, рекомендую починати кожен прийом їжі з білка. \nЯк закрити свою білкову норму? З яких продуктів? \nТваринні: риба, м'ясо, морепродукти, субпродукти, яйця, сир. \nРослинні: бобові, крупи, деякі овочі.",
                               parse_mode='Markdown', reply_markup=kb4_3)
        
    elif call.data == '4_3_case_1':
        await bot.send_message(call.message.chat.id,"Для прикладу розберемо кількість протеїну в цих продуктах на 100г: \n\nТофу - 13г протеїну \nНут - 7г протеїну \nМигдаль - 29г протеїну \nБрокколі - 4г протеїну \nАвокадо - 2г протеїну \nКіноа - 4г протеїну \nКешью - 18г протеїну \nАрахіс олія - 28г протеїну \n\nКурячі яйця - 14г протеїну \nКуряча грудка - 25г протеїну \nКреветки - 18г протеїну \nТунець - 25г протеїну \nКачка (філе) - 27г протеїну \nГрецький йогурт - 9г протеїну \n\nВ ідеалі співвідношення має виглядати так: 70-80% тваринний білок, 20-30% рослинний білок",
                               parse_mode='Markdown', reply_markup=kb4_3_case_1)
        
    elif call.data == 'to_message_4_4':
        await bot.send_message(call.message.chat.id,"ЖИРИ: \n\nЖири діляться на 3 основні категорії: насичені жири, мононенасичені жири та поліненасичені жири. Твариннні і рослинні жири це суміш всіх трьох типів. \nЖири, як і вуглеводи є енергетичним паливом. Єдина відмінність, що вуглеводи неспроможні накопичуватися, а жири мають нескінченний резерв накопичення. \nЖири починають накопичуватися в жировій тканині, після того, як організм вирішив, що їх більше нікуди застосувати. \n\nФункції жирів: \n- Захисна. Ліпіди виконують захисну функцію, особливо в нервових волокнах. \n- Енергетична. Близько 40% жирів йде на виконання цієї функції. \n- Пластична та мембрана-утворювальна. \n- Жири розчиняють жиророзчинні вітаміни А, Е, D, К. Без жирів, засвоєння цих вітамінів неможливе. \n- Транспортна. \n- Гормони. Жири відповідальні за те, щоб синтезувалися гормони, було лібідо, працював головний мозок, а для жінок, щоб був регулярний цикл. \n\nДля того, щоб прибрати жир, необхідно порахувати скільки калорій ви отримуєте з продуктів харчування. \nЯкщо ми їмо трохи менше, ніж потрібно для підтримки, наш організм починає вивільняти жирну кислоту із жирової клітини. \n\nЖири, як і білки, контролюють нашу харчову поведінку. Дуже важливо, щоб жири були в кожному прийомі їжі. \nВажливо враховувати, що жири довго засвоюються, тому якщо ми переїдаємо макронутрієнтами (білки, вуглеводи та жири), білок та вуглеводи використовуються на потреби організму в першу чергу, а жир залишається і транспортується у жирову тканину. Крім накопичення та зменшення жирової тканини, жири мають багато інших важливих функцій, які забезпечують стан здоров'я.  \n\nКоли ми вживаємо молочні продукти, то отримуємо насичені жири, кількість яких варто контролювати. \nМолочні продукти мають високий інсуліновий індекс. І якщо є надмірна вага, або проблеми з вуглеводним обміном, то починати сніданок з йогурту або продуктів, що містять лактозу, не найкращий варіант. Лактоза – це молочний цукор.",
                               parse_mode='Markdown', reply_markup=kb4_4)
    
    elif call.data == 'to_message_4_5':
        await bot.send_message(call.message.chat.id,"Нестача жирів у їжі може привести до наступних наслідків: \n⁃ Втрата пам'яті \n⁃ Психічний розлад \n⁃  Депресія \n⁃  Менструальний біль \n⁃  Рання менопауза \n⁃ Остеопороз \n⁃  Діабет \n⁃  Анемія \n⁃ Атеросклероз \n⁃  Хвороба Альцгеймера \n⁃  Випадання волосся \n⁃  Суха шкіра \n⁃  М'язи перестають рости",
                               parse_mode='Markdown', reply_markup=kb4_5)
        
    elif call.data == 'to_message_4_6':
        await bot.send_message(call.message.chat.id,"Вуглеводи: \n\nВони є ключовим компонентом більшості продуктів харчування та основним джерелом енергії для людини. Діляться на прості та складні. \n\nПрості вуглеводи – швидкі. \nЛегко засвоюються організмом і швидко підвищують рівень цукру в крові, що може призвести до погіршення обміну речовин та набору ваги. \nДо них відносяться: фрукти, овочі, молочні продукти, деякі види круп (манка, пшонна крупа, білий рис). \nТорти, цукерки та інші продукти, що містять рафінований цукор, також містять вуглеводи, але не містять вітамінів, мінералів та клітковину. \n\nСкладні вуглеводи – повільні. \nСкладаються з багатьох зв'язаних сахаридів, що включають від десятків до сотень структурних елементів. Такі вуглеводи сприятливі тим, що при перетравленні вони поступово виділяють свою енергію в організм, забезпечуючи тривале відчуття ситості. \nСкладні вуглеводи є комплексом моносахаридів (простих вуглеводів). Вони включають крохмаль, глікоген та харчові волокна. \nКрупи (макарони, крупи, борошно, хліб) \nБобові (крім сої), овочі (кукурудза та картопля) \n\nМІФИ: «Для того, щоб схуднути, потрібно виключити вуглеводи», «вуглеводи не можна їсти вранці та ввечері», «потрібно відмовитися від десертів». \nРекомендація: схилятися на користь складних вуглеводів. Вони дуже важливі для нашого раціону.",
                               parse_mode='Markdown', reply_markup=kb4_6)
    
    elif call.data == 'to_message_4_7':
        await bot.send_message(call.message.chat.id,"ВАЖЛИВО, ЯК ВИ ПРИГОТУЄТЕ ЇЖУ. \n\nГотувати легкими способами - варіння і приготування на пару - найкращий варіант, оскільки зберігається безліч цінних речовин. \nРекомендація: не смажити їжу, особливо з жиром та олією.",
                               parse_mode='Markdown', reply_markup=kb4_7)
        
    elif call.data == 'to_message_4_8':
        await bot.send_message(call.message.chat.id,"ВОДНИЙ БАЛАНС. \n\nВода – це основа всієї рідини, яка знаходиться у нашому організмі. Щоб наше тіло працювало злагоджено, воно має споживати стільки води, скільки втрачає протягом дня. \nЯк визначити свою норму води: \nРозрахувати 30-35 мл рідини на 1 кг ваги.  \n\nВраховуйте клімат, в якому ви знаходитесь. \n-Не потрібно спеціально вживати велику кількість води, по 4-5л, якщо ви не професійний спортсмен, і не живете в гарячому кліматі. \n-Коли ми вживаємо надто мало води, наші нирки та печінка не справляються з детоксом. \n\nПІД ЧАС ТРЕНУВАНЬ ОБОВ'ЯЗКОВО П'ЄМО ВОДУ! \n\nЯкщо не пити воду, то не уникнути уповільнення процесу схуднення, здуття живота та уповільнення метаболізму. \nЯкщо випивати достатню кількість води, то буде зневоднення - сеча світла. Якщо ні, стає темною. \n\nМІФ: «Щоб розігнати метаболізм, треба пити натще воду з лимоном» \nВоду з лимоном порожній шлунок можна вживати тільки здоровим людям, вживання 50-100мл лимонної кислоти, фрешу, яблучного оцту, або подібного, тягне за собою посилення ситуації, за наявності зниженого рівня кислоти, або підвищеного рівня кислоти в шлунку + метаболізм не прискорюється за рахунок води з лимоном. Метаболізм прискорюється та сповільнюється лише за рахунок кількості наших м'язів.",
                               parse_mode='Markdown', reply_markup=kb4_8)
        
    elif call.data == 'to_message_4_9':
        await bot.send_message(call.message.chat.id,"Більшість вашого раціону повиненно складатися з овочів. \nВи можете приготувати їх різним способом, найкраще буде зварити, готувати на пару, запікати або тушити. Найліпший спосіб Їсти овочі - це, звичайно їсти їх сирими. Сирі продукти містять багато пектину та клітковини. Ці речовини сприяють очищенню кишечника та зниженню рівня холестерину. Салат краще їсти відразу після того, як ви його приготували.",
                               parse_mode='Markdown', reply_markup=kb4_9)
        
    #запросы ЧАСТИНА 4. ЯК СКЛАСТИ СВІЙ РАЦІОН.
        
    elif call.data == 'to_chapter_4':
        await bot.send_message(call.message.chat.id,"ЧАСТИНА 4. \nЯК СКЛАСТИ СВІЙ РАЦІОН. \n\nВ ідеалі, щоб харчування було поділено на кілька прийомів. \nТобто 3 - 4 разовий раціон (залежить від вашого способу життя) \n\nПриклад: \n9:00 – сніданок – 30% денного раціону. \n13:00 – обід – 35% \n16:00 – перекус – 10% \n19:00 – вечеря – 25% \n(Не забувайте в кожен свій прийом їжі включати клітковину) \n\nУвага! У випадку, якщо у вас присутня інсулінорезистентність, рекомендую повністю прибрати перекуси.",
                               parse_mode='Markdown', reply_markup=kb5_1)
        
    #запросы ЧАСТИНА 5. СИТІСТЬ. ЧАС ЗАЛЕЖИТЬ ВІД ХАРАКТЕРУ ЇЖІ.
    
    elif call.data == 'to_chapter_5':
        await bot.send_message(call.message.chat.id,"ЧАСТИНА 5. \nСИТІСТЬ. ЧАС ЗАЛЕЖИТЬ ВІД ХАРАКТЕРУ ЇЖІ. \n\nЯкщо ви з'їли: білок і трохи овочів - ви зголоднієте досить швидко, через 1-1,5 години, залежно від порції білка. \nЯкщо ви з'їли: білок та жири – ситість збережеться на 4-5 годин, оскільки жири довго розщеплюються. \nЯкщо ви з'їли: білок + жири + вуглеводи – ситість буде максимально довгою 5-6 годин. \n\nЯкщо у вас проблема із ситістю, постарайтеся збільшити порції нутритивних продуктів. \n\nЯ рекомендую кожен прийом їжі починати з білка, а потім уже вуглеводи з жирами. Оскільки черговість макронутрієнтів впливає на те, як швидко та в яких кількостях виділятиметься інсулін. \nПам'ятайте, що немає певного часу, до якого можна їсти. Ви можете їсти о 18:00, та о 20:00. Намагайтеся робити останній прийом їжі за 3-4 години до сну.",
                               parse_mode='Markdown', reply_markup=kb6_1)
        
    #запросы ЧАСТИНА 6. ЧОМУ ТЯГНЕ НА СОЛОДКЕ?
    
    elif call.data == 'to_chapter_6':
        await bot.send_message(call.message.chat.id,"ЧАСТИНА 6. \nЧОМУ ТЯГНЕ НА СОЛОДКЕ? \n\nВ основному, як тільки ви відчуваєте тягу до солодкого, то велика ймовірність, що вам не вистачає будівельних матеріалів: отже, швидше за все, ви не доїдаєте свою норму білків і жирів. \n\n- Але чому хочеться солодкого після їжі, навіть якщо ситно поїли? \nЗнову ж таки, для початку потрібно розібрати свою тарілку, можливо в ній було наприклад, мало білків і більше вуглеводів, або була занадто маленька порція. \nПід час прийому їжі у нас виробляються одні з таких гормонів як: грелін та лептин. \n\nГрелін - забезпечує емоційне задоволення від їжі, пробуджує апетит, у великих кількостях виробляється при стресі, що і викликає сильне бажання щось з'їсти. \nЛептин – виробляється жировими клітинами, і саме він подає сигнал у наш мозок, що ми наїлися. Найчастіше у повних людей, функція ліпнина порушена. Щоб допомогти його нормалізувати: потрібен повноцінний сон, фізична активність і поповнення дефіцитів Омега 3, якщо вони присутні. \n\nТак от, коли під час їжі, лептин і грелін ще не встигли спрацювати, то може виникати жага до десерту, спробуйте в такому разі трохи перечекати після їжі. \n\n3-й варіант - потяг до солодкого може відбуватися через емоційний голод. Багато хто замінює солодким позитивні емоції. У даному варіанті рекомендую для початку визначити чи це так, знайти те, що вас наповнюватиме щасливими емоціями, це можуть бути: нове хобі, друзі, подорожі, медитації, займіться тим, що приноситиме щире задоволення. \n\n4-й варіант – ви ставите собі заборони. Важливо налагодити здорові стосунки з їжею. Припиніть демонізувати та забороняти собі продукти. Ще раз повторюся, зміни починаються з голови.",
                               parse_mode='Markdown', reply_markup=kb7_1)
        
    #запросы ЧАСТИНА 7. ЦУКОР, ПРИХОВАНИЙ ЦУКОР І ПП ДЕСЕРТИ.
    
    elif call.data == 'to_chapter_7':
        await bot.send_message(call.message.chat.id,"ЧАСТИНА 7. \nЦУКОР, ПРИХОВАНИЙ ЦУКОР І ПП ДЕСЕРТИ \n\nЦукор…, його порівнюють з наркотиком... \n\nНасамперед закликаю не демонізувати цукор, як часто це роблять. З цукром потрібно потоваришувати і правильно його вживати. При здорових стосунках із їжею – цукор ніхто не виключає. Гірше, коли є нездорова залежність від їжі та заборони. \nНайбільше глюкози міститься у швидких вуглеводах. До них відносяться і глюкоза (джерело енергії), фруктоза (в основному це фрукти), галактоза (отримуємо з лактози). Лактоза – це цукор у молочній продукції. \nОднак надлишок глюкози здатний негативно впливати на наш організм, підвищуючи рівень мікрозапалення і прискорюючи процеси старіння. \nА також надлишок глюкози відкладатиметься у жирову тканину. \n\nМіф: «Потрібно з'їсти/випити глюкози, щоб з'явилася енергія». \nНаш мозок харчується глюкозою. АЛЕ існує такий процес, коли організм створює глюкозу з амінокислот і жирів самостійно. Для того, щоб глюкоза потрапила в клітини головного мозку, інсулін не потрібен. Мозок отримає глюкозу, навіть якщо людина не поїла. \n\nФруктоза – простими словами – це природний цукор (фрукти, сухофрукти, соки, фреші, мед, сиропи). \n\nДумаю, всі бачили ці популярні полиці в магазинах для діабетиків, де все зроблено на фруктозі. Насправді калорійність цукрута фруктози не сильно відрізняється. Багато хто ще думає, що фруктоза корисніша і безпечніша за цукор. \n\nНадмірне споживання фруктози призводить до: інсулінорезистентності, ожиріння печінки, підвищення запалення, накопичення сечової кислоти. \nДосить часто ЗОЖні десерти мають високий вміст фруктози та за калоріями можуть прирівнюватися до торта. \nНайкращим варіантом буде - вживати ягоди, тому що в них низький вміст фруктози. \nЛайфхак: щоб уникати різких підйомів глюкози в крові, слід поєднувати швидкі вуглеводи, фруктовмісні продукти - відразу після основного прийому їжі.",
                               parse_mode='Markdown', reply_markup=kb8_1)
        
    #запросы ЧАСТИНА 8. ЯК ВТРИМАТИ СВОЮ ВАГУ НА ДОВГІ РОКИ.
    
    elif call.data == 'to_chapter_8':
        await bot.send_message(call.message.chat.id,"ЧАСТИНА 8. \nЯК ВТРИМАТИ СВОЮ ВАГУ НА ДОВГІ РОКИ \n\nДля підтримки ваги – людині потрібно отримувати з їжею ту калорійність, яку вона витрачає. \nКожна людина має свою власну вагу, яка підтримується протягом усього життя. \nУ нас дуже розумний організм, і він завжди повертається у свою звичну вагу. Тому коли людина худне, припустимо на марафоні в короткий проміжок часу, а потім робить чітмили, або марафон закінчується, то організм відразу прагне повернутися до своєї звичної ваги, яка була вже тривалий час. Для того, щоб зафіксувати свій результат, потрібна стабільність, тимчасові методи зниження ваги не працюють. \nЧим частіше людина намагається схуднути, триматися на дієтах, виснажує себе тренуваннями – тим більше організм виділяє кортизол та пролактин, тим більше він знижує гормони щитовидної залози. Часто в таких ситуаціях навантажується робота гормональної системи та виникає відчуття постійного голоду/ломки. Потім людина починає переїдати. \"Ломається\" обмін речовин. \n\nТому важливий фактор: утримувати свій стан упродовж життя не на силі волі, а на розумінні.",
                               parse_mode='Markdown', reply_markup=kb9_1)
        
    elif call.data == 'to_message_9_2':
        await bot.send_message(call.message.chat.id,"Отже, ми розібрали основні фактори, які зможуть привести ваше тіло та здоров'я до ладу. Пам'ятайте, що все залежить тільки від вас, адже наше тіло не можна купити, позичити, подарувати. Ми можемо його тільки створити і підтримувати самостійно. Не бійтеся їжі, це джерело нашої енергії, розумійте, аналізуйте те, що ви їсте, більше рухайтеся, полюбіть себе, нові звички, тренування. Відчуйте себе вільним від дієт та марафонів, вони не працюють. Зробити перший крок завжди складніше, але уявіть як ви пишатиметеся собою в результаті! \nДякую, що обрали моє навчання, буду щаслива, якщо залишите свій зворотний зв'язок.  \nЯ щиро вірю і знаю, що ви досягнете своєї мети! Не зупиняйтеся!",
                               parse_mode='Markdown', reply_markup=kb9_2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)