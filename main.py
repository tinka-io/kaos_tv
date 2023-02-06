import threading

import logger as log
import telegram_bot as tb
import play_media as pm
import delete_media as dm

folder = 'Media'

def play_media():
    log.info("Start to Play Media")
    while True:
        pm.play_all_media(folder)
        dm.delete_all_media_older_than(folder, max_age=2)
	
if __name__ == '__main__':
    log.info("Start KAOS TV")
    
    x = threading.Thread(target=play_media, args=())
    x.start()
    
    tb.ktv(folder)