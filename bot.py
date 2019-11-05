import telebot
from datetime import datetime
from datetime import timedelta
one_day = timedelta(1)
now1 = datetime.now()
tomoroww = now1 + one_day
dayp = str(tomoroww.strftime("%A"))

global monA
global monB
global tueA
global tueB
global wen
global thuA
global thuB
global friA
global friB
global sun

TOKEN = '975925818:AAEWY89tap7F9VSLidJMvHRQVfQHlK1Sids'
bot = telebot.TeleBot(TOKEN)
value = 0




@bot.message_handler(commands=['start'])
def start_command(message):
    now = datetime.now() + timedelta(hours=1)
    monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
    monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
    tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
    tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
    wen = "Время:" + now + "\nСреда\nСвободный день"
    thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
    thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
    friA = "Время:" + now + "\nПятница\nСвободный день"
    friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
    sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    bot.send_message(message.chat.id,"Время:" + str(datetime.now() + timedelta(hours=1)) + "\n\nНа пары ? Неужели",  reply_markup=keyboard)
    bot.delete_message(message.chat.id, message.message_id - 1)



@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('today'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        today(query.message)
    if data.startswith('tomorow'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        tomorow(query.message)
    if data.startswith('a'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        todaya(query.message)
    if data.startswith('b'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        todayb(query.message)
    if data.startswith('ta'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        tomorowa(query.message)
    if data.startswith('tb'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        tomorowb(query.message)
    if data.startswith('back'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        back(query.message)
    if data.startswith('qwerty'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        vsedni(query.message)


    if data.startswith('Monday'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        monday(query.message)


    if data.startswith('Tuesday'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        bot.delete_message(query.message.chat.id, query.message.message_id)
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('A', callback_data='tuea'),
            telebot.types.InlineKeyboardButton('B', callback_data='tueb')
        )
        bot.send_message(query.message.chat.id, "Выбери неделю:", reply_markup=keyboard)
    if data.startswith('tuea'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        answer = "A"
        tuesday(query.message, answer)
    if data.startswith('tueb'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        answer = "B"
        tuesday(query.message, answer)

    if data.startswith('Wednesday'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        wednesday(query.message)

    if data.startswith('Thursday'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        bot.delete_message(query.message.chat.id, query.message.message_id)
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('A', callback_data='thua'),
            telebot.types.InlineKeyboardButton('B', callback_data='thub')
        )
        bot.send_message(query.message.chat.id, "Выбери неделю:", reply_markup=keyboard)
    if data.startswith('thua'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        answer = "A"
        thursday(query.message, answer)
    if data.startswith('thub'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        answer = "B"
        thursday(query.message, answer)

    if data.startswith('Friday'):
        bot.answer_callback_query(query.id)
        bot.delete_message(query.message.chat.id, query.message.message_id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('A', callback_data='fria'),
            telebot.types.InlineKeyboardButton('B', callback_data='frib')
        )
        bot.send_message(query.message.chat.id, "Выбери неделю:", reply_markup=keyboard)
    if data.startswith('fria'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        answer = "A"
        friday(query.message, answer)
    if data.startswith('frib'):
        bot.answer_callback_query(query.id)
        now = str((datetime.now() + timedelta(hours=1)).strftime("%H:%M"))
        monA = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        monB = "Время:" + now + "\nПонедельник\n8:00-9:30 Systemy wbudowane (wyklad)\nPiotr Bilski\nKab 104\n\n9:45-11:15 Sieci komputerowe (wyklad)\nDariusz\nKab 227"
        tueA = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (wyklad)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nProjektowanie aplikacji bazodanowych (laboratorium)\nPelczynski Pawel\nKab 0"
        tueB = "Время:" + now + "\nВторник\n13:15-14:45\nPodstawowe techniki animacji komputerowej (laboratorium)\nAntoniuk Izabella\nKab 227\n\n15:00-16:30\nSztuczna intelegencja (laboratorium)\nZawadski Mariusz\nKab 5"
        wen = "Время:" + now + "\nСреда\nСвободный день"
        thuA = "Время:" + now + "\nЧетверг\n9:45-11:15 Inżynieria oprogramowania (wyklad)\nBilski Adrian\nKab 305\n\n13:15-14:45 Gkiai-Wzorce architektoniczne serwisow internetowych (laboratorium)\nBobinski Piotr\nKab 329\n\n15:00-16:30 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329\n\n16:45-18:15 Sztuczna intelegencja(wyklad)\nBilski Adrian\nKab 329"
        thuB = "Время:" + now + "\nЧетверг\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\n13:15-14:45 Techniki przetwarzania wielowatkowego (laboratorium)\nBobinski Piotr\nKab 329\n\nInżynieria oprogramowania\nZawadzki Mariusz\nKab 108"
        friA = "Время:" + now + "\nПятница\nСвободный день"
        friB = "Время:" + now + "\nПятница\n8:00-9:30 Administrowanie sieciami komputerowymi (laboratorium)\nDariusz\nKab 227\n\n9:45-11:15 Sieci computerowe (laboratorium)\nDariusz\nKab 227"
        sun = "Время:" + now + "\nВоскресенье\nВ воскресенье нету занятий"
        answer = "B"
        friday(query.message, answer)





def today(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('A', callback_data='a'),
        telebot.types.InlineKeyboardButton('B', callback_data='b')
    )
    bot.send_message(message.chat.id, "Выбери неделю:",reply_markup=keyboard)

def tomorow(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('A', callback_data='ta'),
        telebot.types.InlineKeyboardButton('B', callback_data='tb'))
    bot.send_message(message.chat.id, "Выбери неделю:",reply_markup=keyboard)

def tomorowa(message):
    bot.delete_message(message.chat.id, message.message_id)
    tomorow = dayp
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    if(tomorow == "Monday"):
        bot.send_message(message.chat.id, monA, reply_markup=keyboard)
    if(tomorow == "Tuesday"):
        bot.send_message(message.chat.id, tueA, reply_markup=keyboard)
    if(tomorow == "Wednesday"):
        bot.send_message(message.chat.id, wen, reply_markup=keyboard)
    if(tomorow == "Thursday"):
        bot.send_message(message.chat.id, thuA, reply_markup=keyboard)
    if(tomorow == "Friday"):
        bot.send_message(message.chat.id, friA, reply_markup=keyboard)
    if(tomorow == "Saturday"):
        bot.send_message(message.chat.id, "В субботу нету занятий", reply_markup=keyboard)
    if(tomorow == "Sunday"):
        bot.send_message(message.chat.id, sun, reply_markup=keyboard)

def tomorowb(message):
    bot.delete_message(message.chat.id, message.message_id)
    tomorow = dayp
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    if(tomorow == "Monday"):
        bot.send_message(message.chat.id, monB, reply_markup=keyboard)
    if(tomorow == "Tuesday"):
        bot.send_message(message.chat.id, tueB, reply_markup=keyboard)
    if(tomorow == "Wednesday"):
        bot.send_message(message.chat.id, wen, reply_markup=keyboard)
    if(tomorow == "Thursday"):
        bot.send_message(message.chat.id, thuB, reply_markup=keyboard)
    if(tomorow == "Friday"):
        bot.send_message(message.chat.id, friB, reply_markup=keyboard)
    if(tomorow == "Saturday"):
        bot.send_message(message.chat.id, "В субботу нету занятий", reply_markup=keyboard)
    if(tomorow == "Sunday"):
        bot.send_message(message.chat.id, sun, reply_markup=keyboard)


def todaya(message):
    bot.delete_message(message.chat.id, message.message_id)
    todaya = str(now.strftime("%A"))
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    if(todaya == "Monday"):
        bot.send_message(message.chat.id, monA,reply_markup=keyboard)
    if(todaya == "Tuesday"):
        bot.send_message(message.chat.id, tueA,reply_markup=keyboard)
    if(todaya == "Wednesday"):
        bot.send_message(message.chat.id, wen,reply_markup=keyboard)
    if(todaya == "Thursday"):
        bot.send_message(message.chat.id, thuA,reply_markup=keyboard)
    if(todaya == "Friday"):
        bot.send_message(message.chat.id, friA,reply_markup=keyboard)
    if(todaya == "Saturday"):
        bot.send_message(message.chat.id, "В субботу нету занятий",reply_markup=keyboard)
    if(todaya == "Sunday"):
        bot.send_message(message.chat.id, sun, reply_markup=keyboard)

def todayb(message):
    bot.delete_message(message.chat.id, message.message_id)
    todayb = str(now.strftime("%A"))
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    if(todayb == "Monday"):
        bot.send_message(message.chat.id, monA,reply_markup=keyboard)
    if(todayb == "Tuesday"):
        bot.send_message(message.chat.id, tueA,reply_markup=keyboard)
    if(todayb == "Wednesday"):
        bot.send_message(message.chat.id, wen,reply_markup=keyboard)
    if(todayb == "Thursday"):
        bot.send_message(message.chat.id, thuA,reply_markup=keyboard)
    if(todayb == "Friday"):
        bot.send_message(message.chat.id, friA,reply_markup=keyboard)
    if(todayb == "Saturday"):
        bot.send_message(message.chat.id, "В субботу нету занятий",reply_markup=keyboard)
    if(todayb == "Sunday"):
        bot.send_message(message.chat.id, sun, reply_markup=keyboard)

def vsedni(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Понедельник', callback_data='Monday'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('Вторник', callback_data='Tuesday'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('Среда', callback_data='Wednesday'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('Четверг', callback_data='Thursday'))
    keyboard.row(
        telebot.types.InlineKeyboardButton('Пятница', callback_data='Friday'))
    bot.send_message(message.chat.id, "Выбери день недели", reply_markup=keyboard)


def monday(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    bot.send_message(message.chat.id, monA,reply_markup=keyboard)

def tuesday(message, answer):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    if(answer == "A"):
        bot.send_message(message.chat.id, tueA,reply_markup=keyboard)
    if (answer == "B"):
        bot.send_message(message.chat.id, tueB, reply_markup=keyboard)

def wednesday(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    bot.send_message(message.chat.id, wen,reply_markup=keyboard)


def thursday(message, answer):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    if(answer == "A"):
        bot.send_message(message.chat.id, thuA,reply_markup=keyboard)
    if (answer == "B"):
        bot.send_message(message.chat.id, thuB, reply_markup=keyboard)


def friday(message, answer):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Сегодня', callback_data='today'),
        telebot.types.InlineKeyboardButton('Завтра', callback_data='tomorow')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Все дни', callback_data='qwerty')
    )
    if(answer == "A"):
        bot.send_message(message.chat.id, friA,reply_markup=keyboard)
    if (answer == "B"):
        bot.send_message(message.chat.id, friB, reply_markup=keyboard)


bot.polling(none_stop=True)
