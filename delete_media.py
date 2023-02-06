import os
from datetime import datetime, timedelta

def delete_all_media_older_than(folder = 'Media', max_age = 2):
    for dir_name, subdir_list, file_list in os.walk(folder):
        for file_name in file_list:
    
            file_path = os.path.join(dir_name, file_name)
            mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if datetime.now() - mtime > timedelta(days=max_age):
                
                os.remove(file_path)

if __name__ == '__main__':
    delete_all_media_older_than()