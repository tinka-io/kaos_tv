import vlc
import os
import time
import os
import logger as log
import pathes as path
import setproctitle
    
def show_name(player, file_name):
    user_name = file_name.split('_')
    if(len(user_name) >= 3):
        user_name = user_name[2].split('.')
        text = user_name[0]
    else: 
        text = 'Unknown'
            
    m = vlc.VideoMarqueeOption
    player.video_set_marquee_int(m.Enable, 1)
    player.video_set_marquee_int(m.Size, 48)  # pixels
    player.video_set_marquee_int(m.Position, 9)
    player.video_set_marquee_int(8, 20) # m.marquee_X
    player.video_set_marquee_int(9, 20) # m.marquee_Y
    player.video_set_marquee_string(m.Text, text)

screen_saver_files = []
for root, dirs, files in os.walk(path.screen_saver):
    screen_saver_files += [os.path.join(root, file) for file in files]
    
def play_all_media(lock, index):
    setproctitle.setproctitle(f'KAOS_TV_VLC_{index}')
    global stop_playing, screen_saver_files
    
    player = vlc.MediaPlayer()
    
    media_files = []
    for root, dirs, files in os.walk(path.media):
        media_files += [os.path.join(root, file) for file in files]
    
    if(media_files == []):
        media_files += screen_saver_files
    media_files.sort()
    
    lock.acquire()
    for file in media_files:

        show_name(player, file)
        
        try:
            player.set_fullscreen(True)
            media = vlc.Media(file)
            player.set_media(media)
            player.play()
            log.info(f'{index} play media, {file}')
            
        except:
            log.error(f'{index} can\'t play media, {file}')
          
        if file.endswith('.jpg'):
            time.sleep(5)
        else:
            time.sleep(0.1)
            while player.is_playing():
                time.sleep(0.1)
                pass
    
    log.debug(f'{index} player relase')
    lock.release()
    time.sleep(2.0)
    
if __name__ == '__main__':
    while True:
        play_all_media(0)
        #time.sleep(3)