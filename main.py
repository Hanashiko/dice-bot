from aiogram import Bot, types, Dispatcher, executor
from random import randint, choice

bot = Bot(token='your_tg_bot_api_token')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('''Привіт!
Мене звати DiceBot
Щоб кинути кубик напишіть `/dice` |кількість кубиків| |який кубив|
Можеш подивитися інформацію про мене, використавши команду /info''',parse_mode='markdown')

@dp.message_handler(commands=['info'])
async def send_welcome(message: types.Message):
    await message.reply('''Меня зовут: DiceBot
Мій нік: DiceBot
Навіщо мене створили: для кидання різноманітних кубиків
Мій айді: (place your bot id there)
Мій творець: Hanashiko
Версія: 0.2.2''')

@dp.message_handler(commands=['dice'])
async def cmd_d4(message: types.Message):
    try:
        args = message.text.split()
        argument1 = args[1]
        argument2 = args[2]
    except:
        await message.reply("Пишіть по прикладу: `/dice` [кількість кубиків] [тип кубика]", parse_mode="markdown")
        return
    try:
        arg1 = int(argument1)
        arg2 = int(argument2)
    except:
        await message.reply("Після команди `/dice` обов'язково вводьте саме числа", parse_mode="markdown")
        return
    sum = 0
    throws = []
    for i in range(arg1):
        drop = randint(1,arg2)
        throws.append(str(drop))
        sum+=drop
    result_drop = ', '.join(throws)
    await message.reply(f"Сума кидків: `{sum}` \nВсі кидки: {result_drop}", parse_mode="markdown")
    
executor.start_polling(dp, skip_updates=True)
