{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12392920691239292069\n",
      "\n",
      "381012285\n",
      "381012285\n",
      "381012285\n",
      "356406198\n",
      "356406198\n",
      "356406198\n",
      "356406198\n",
      "1239292069\n",
      "1239292069\n",
      "356406198\n",
      "356406198\n"
     ]
    }
   ],
   "source": [
    "import telebot\n",
    "bot = telebot.TeleBot('1648298005:AAGjvci1P6Molwf_WDp9UI_Qsv8zhnv00jE')\n",
    "keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)\n",
    "keyboard1.row('Завершить')\n",
    "arr_url = {}\n",
    "\n",
    "@bot.message_handler(commands=['start'])\n",
    "def start_message(message):\n",
    "\n",
    "    bot.send_message(message.chat.id, 'Здравствуйте! \\n'+'Чтобы получить бесплатный персонализированный каталог, отправляйте боту каждую ссылку, по которой пройдете на выставке (даже если она встретится вам несколько раз). В конце нажмите «Завершить» и получите номер, по которому сможете забрать готовый каталог.', reply_markup=keyboard1)\n",
    "\n",
    "@bot.message_handler(content_types=['text'])\n",
    "def send_text(message):\n",
    "    name = message.from_user.id\n",
    "    name_str = str(name)\n",
    "    id_admin = 356406198 #номер администратора\n",
    "    text_message = message.text.lower()\n",
    "    tt = text_message.split()\n",
    "    print(name)\n",
    "    if ('.ru' in text_message) or ('.com' in text_message) or ('.net' in text_message) or ('.org' in text_message) or (1<len(text_message.split('.'))):\n",
    "        bot.send_message(message.chat.id, 'Принято')\n",
    "        if name_str in arr_url.keys():\n",
    "            if text_message in arr_url[name_str]:\n",
    "                pass\n",
    "            else:\n",
    "                arr_url[name_str].append(text_message)\n",
    "        else:\n",
    "            arr_url[name_str] = []\n",
    "            arr_url[name_str].append(text_message)\n",
    "        \n",
    "    elif text_message == 'завершить':\n",
    "        bot.send_message(message.chat.id, 'Ваш номер для получения персонального каталога: ' + str(name))\n",
    "        bot.send_message(id_admin, 'Номер заказа: ' + name_str)\n",
    "        bot.send_message(id_admin, 'Ссылки:')\n",
    "        for i in arr_url[name_str]:\n",
    "            bot.send_message(id_admin, i)#отправка ссылок и id\n",
    "            \n",
    "    elif tt[0] == 'пароль':\n",
    "        j = tt[1]\n",
    "        try:\n",
    "            a = arr_url[j]\n",
    "            bot.send_message(message.chat.id, 'Номер заказа: ' + j)\n",
    "            bot.send_message(message.chat.id, 'Ссылки:')\n",
    "            for i in arr_url[j]:\n",
    "                bot.send_message(message.chat.id, i)#отправка ссылок и id\n",
    "        except:\n",
    "            bot.send_message(message.chat.id, 'Вы ввели неверный номер заказа повторите попытку.')\n",
    "    else:\n",
    "        bot.send_message(message.chat.id, 'Неверный формат. Бот принимает только ссылки.')\n",
    "\n",
    "\n",
    "\n",
    "        \n",
    "        \n",
    "bot.polling()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
