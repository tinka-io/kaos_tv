import threading

import logger as log
import telegram_bot as tb
import play_media as pm
import delete_media as dm


folder = 'Media'

run_player = False
def stop_player():
    global run_player
    
    log.error("stop player")
    pm.stop_playing = True
    run_player = False

def play_media():
    log.info("\tstart Media Player")
    
    global run_player
    run_player = True
    while run_player:
        try:
            pm.play_all_media(folder)
        except:
            log.error("play_media crashed")
            
        try:
            dm.delete_all_media_older_than(folder, max_age=2)
        except:
            log.error("delete_all_mdeia crashed")
    
    log.error("player stoped")
	
if __name__ == '__main__':
    log.info("Start KAOS TV")
     
    x = threading.Thread(target=play_media, args=())
    x.start()
    
    try:
        tb.ktv(folder)
    except:
        log.error("telegram bot crashed")
    
    
    stop_player()
    x.join()
    log.error("shutdow - end of programm")