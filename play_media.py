import vlc
import os
import time
import os
import logger as log

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
        
active_window = 0
player = vlc.MediaPlayer()
    
stop_playing = False
    
def play_all_media(folder = 'Media'):
    global active_window, player, stop_playing
    
    player_old = player
    active_window = 0
    player = vlc.MediaPlayer()
            
    media_files = []
    for root, dirs, files in os.walk(folder):
        media_files += [os.path.join(root, file) for file in files]
    
    if(media_files == []):
        log.warn("can't fine any Media Files")
        time.sleep(10)
    media_files.sort()
    
    for file in media_files:
        if stop_playing:
            return
         
        log.info(f'play media, {file}')
        show_name(player, file)
        
        try:
            player.set_fullscreen(True)
            media = vlc.Media(file)
            player.set_media(media)
            player.play()
                        
            if(active_window == 0):
                active_window = 1
                time.sleep(0.25)
                player_old.stop()
            
        except:
            log.error(f'can\'t play media, {file}')
          
        if file.endswith('.jpg'):
            time.sleep(5)
        else:
            time.sleep(0.25)
            while player.is_playing() and not stop_playing:
                pass    
    
if __name__ == '__main__':
    while True:
        play_all_media()
        #time.sleep(3)