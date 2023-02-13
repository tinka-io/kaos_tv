import vlc
import os
import time
import os
import logger as log

player = vlc.MediaPlayer()

def show_name(player, text):
    m = vlc.VideoMarqueeOption
    player.video_set_marquee_int(m.Enable, 1)
    player.video_set_marquee_int(m.Size, 48)  # pixels
    player.video_set_marquee_int(m.Position, 9)
    player.video_set_marquee_int(8, 20) # m.marquee_X
    player.video_set_marquee_int(9, 20) # m.marquee_Y
    player.video_set_marquee_string(m.Text, text)
        
def play_all_media(folder = 'Media'):
    
    media_files = []
    for root, dirs, files in os.walk(folder):
        media_files += [os.path.join(root, file) for file in files]
    
    if(media_files == []):
        log.warn("can't fine any Media Files")
        time.sleep(10)

    for file in media_files:    
        
        user_name = file.split('_')
        if(len(user_name) >= 3):
            user_name = user_name[2].split('.')
            show_name(player, user_name[0])
        else: 
            show_name(player, 'Uknown')
            
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