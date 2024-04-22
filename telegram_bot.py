# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#downloading-a-file

import json
import os
import logger as log
import asyncio
from os.path import exists
import pathes as path
from telegram.ext import *
from telegram import Update
import setproctitle

# TODO https://github.com/ismaventuras/python-telegram-bot-service

class teleg_bot():    
    NAME = "KAOSTV_bot"
    TOKEN = os.getenv('TELEG_TOKEN')
    
    media_index = 0    
    
    def __init__(self, max_age = 2):
        setproctitle.setproctitle('KAOS_TV_TELEGRAM')
        log.info("\tstart Telegram Boot")
        
        teleg_bot.max_age = max_age
        
        if not exists(path.config):
            log.debug("- create new config file")
            teleg_bot.write_conifg()
        else:
            log.debug("- read indexes")
            teleg_bot.read_config() 
            log.debug(f'-- media: {teleg_bot.media_index}')
    
        application = ApplicationBuilder().token(teleg_bot.TOKEN).build()
        
        start_handler = CommandHandler('start', teleg_bot.start)
        application.add_handler(start_handler)
        
        photo_handler = MessageHandler(filters.PHOTO & (~filters.COMMAND), teleg_bot.photo)
        application.add_handler(photo_handler)
        
        video_handler = MessageHandler(filters.VIDEO & (~filters.COMMAND), teleg_bot.video)
        application.add_handler(video_handler)
        
        try:
            application.run_polling()
        except:
            log.exept("Can't connect to Telegram, maybe there is no Internet connection?")
        
    def read_config():
        with open(path.config) as json_file:
            json_str = json_file.read()
            jd = json.loads(json_str)
            teleg_bot.media_index = jd['media']
            
    def write_conifg():
        data = {
            'media' : teleg_bot.media_index,
        }
            
        with open(path.config, 'w') as json_file:
            json.dump(data, json_file)
            
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_says = update.message.text
        
        user_name = update.message.from_user.first_name
        log.info(f'start from: {user_name}')
        
        msg = f'Welcome to KAOS TV, {user_name}!\n'
        msg += f'Share your fotos and videos now.'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
        teleg_bot.write_conifg()
        
    async def message_handler(self, update: Update, context: CallbackContext):
        with open("update.json", 'r', encoding="UTF-8") as fp:
            data = json.load(fp)
        data.append(update.to_dict())
        with open("update.json", 'w', encoding="UTF-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
        context.bot.send_message(
            chat_id=update.message.chat.id, text=update.message.text)
        
    async def photo(update: Update, context: CallbackContext):
        user_name = update.message.from_user.first_name
        log.info(f'get Pic from: {user_name}')
        
        os.makedirs(path.media, exist_ok=True)
        file_id = update.message.photo[-1].file_id
        new_file = await context.bot.get_file(file_id)
        
        await new_file.download_to_drive(f"{path.media}/{teleg_bot.media_index:04d}_pic_{user_name}.jpg")
        msg = f'Thank you for your picture, I will display it for {teleg_bot.max_age} days.'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
        teleg_bot.media_index += 1
        teleg_bot.write_conifg()
        
    async def video(update: Update, context: CallbackContext):
        user_name = update.message.from_user.first_name
        log.info(f'get Video from: {user_name}')
        
        
        os.makedirs(path.media, exist_ok=True)        
        file_id = update.message.video.file_id
        new_file = await context.bot.get_file(file_id)
        
        await new_file.download_to_drive(f"{path.media}/{teleg_bot.media_index:04d}_vid_{user_name}.mp4")
        msg = f'Thank you for your video, I will display it for {teleg_bot.max_age} days.'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
        teleg_bot.media_index += 1
        teleg_bot.write_conifg()
        

if __name__ == '__main__':
    teleg_bot()
