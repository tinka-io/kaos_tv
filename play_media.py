import vlc
import os
import time
import os
import logger as log

player = vlc.MediaPlayer()

def play_all_media(folder = 'Media'):
    
    media_files = []
    for root, dirs, files in os.walk(folder):
        media_files += [os.path.join(root, file) for file in files]
    
    if(media_files == []):
        log.warn("can't fine any Media Files")
        time.sleep(10)

    for file in media_files:    
        media = vlc.Media(file)
        player.set_media(media)
        player.play()
        player.set_fullscreen(True)
        
        time.sleep(0.25)
        
        while player.is_playing():
            pass

if __name__ == '__main__':
    while True:
        play_all_media()