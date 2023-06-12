import random
import os
from gtts import gTTS
import playsound
import speech_recognition as sr

films = ['терминатор', 'терминатор 2', 'рембо', 'пятый элемент']
hellows = ['hola', 'привет', 'здравствуйте', 'hi']


def listen():  # слушаем команду
    print('скажите команду')
    rec = sr.Recognizer()  # включение модуля расшифровщика
    with sr.Microphone() as source:  # называем микрофон source
        voice = rec.listen(source, phrase_time_limit=3)  # запись того что с микрофона в течении 3 сек в переменную
    try:
        com = rec.recognize_google(voice, language='ru')  # расшифровывание звука в текст
        print('вы сказали', com)
        choose(com)
    except sr.UnknownValueError:
        print('не могу распознать')
    except sr.RequestError:
        print('ошибка гугла')
    except sr.WaitTimeoutError:
        print('не дозвонились')
    # com = input('скажите команду\n')

    pass


def choose(msg):  # выбираем действие
    msg = msg.lower()
    if 'привет' in msg:
        h = random.choice(hellows)
        action(h)
    elif 'пока' in msg:
        action('до свидания')
        os.abort()
    elif 'как дела' in msg:
        action('норм')
    elif 'анекдот' in msg:
        action('купил мужик шляпу, а она ему как раз')
    elif 'фильм' in msg:
        r = random.choice(films)
        action(r)
    else:
        action(msg)
    pass


def action(say):  # выполняем действие
    print('бот:', say)
    voice = gTTS(say, lang='ru')
    fname = '1.mp3'
    voice.save(fname)
    playsound.playsound(fname)
    os.remove(fname)

    pass


while True:
    listen()
