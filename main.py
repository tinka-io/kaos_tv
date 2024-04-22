from multiprocessing import Process, Lock
import time
import setproctitle

import logger as log
import telegram_bot as tb
import play_media as pm
import delete_media as dm

# Usefull commands:
# watch -n 1 "ps aux | grep KAOS_TV"
# watch -n 1 "pgrep -f KAOS_TV | xargs -I _ ps -T -p _"

max_age = 2

def play_media():
    log.info("\tstart media player")

    index = 0
    lock = Lock()
    
    ps_wait = None
    ps_run = None
    while True:
        
        ps_run = Process(target=pm.play_all_media, args=(lock, index,))
        ps_run.start()
        log.debug(f'start {index}')
        index += 1
            
        time.sleep(1.0)
        if ps_wait:
            log.debug(f'wait for {index-1}')
            ps_wait.join()
            log.debug(f'join {index-1}')
        ps_wait = ps_run
	
if __name__ == '__main__':
    setproctitle.setproctitle('KAOS_TV')
    log.info("="*50)
    log.info("start KAOS_TV")
    log.warn("you can see WARNING massages")
    log.error("you can see ERROR massages")
    log.debug("you can see DEBUG massages")
    log.info("="*50)
    
    try:
        dm.delete_all_media_older_than(max_age)
    except:
        log.error("delete_all_mdeia crashed")
    
    ps_teleg_bot = Process(target=tb.teleg_bot, args=(max_age, ))
    ps_teleg_bot.start()
    
    play_media()
    
    ps_teleg_bot.kill()
    log.info("shutdow - end of programm")