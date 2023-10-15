import os
from datetime import datetime, timedelta

import logger as log
import pathes as path

def delete_all_media_older_than(max_age = 2):
    for dir_name, subdir_list, file_list in os.walk(path.media):
        for file_name in file_list:
    
            file_path = os.path.join(dir_name, file_name)
            mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            print(f'{datetime.now() - mtime} > {timedelta(days=max_age)}')
            
            if datetime.now() - mtime > timedelta(days=max_age):
                log.info(f'delete: {file_path}')
                os.remove(file_path)

if __name__ == '__main__':
    delete_all_media_older_than()