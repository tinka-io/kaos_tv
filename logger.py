import os
import logging

logging.basicConfig(filename='kaos_tv.log',
                    encoding='utf-8', 
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def info(msg):
    print("info\t" +msg)
    logging.info(msg)

def warn(msg):
    print("warn:\t" + msg)
    logging.warning(msg)

def error(msg):
    print("error:\t" + msg)
    logging.error(msg)
    
def exept(msg):
    print("exept:\t" + msg)
    logging.exception(msg)

def debug(msg):
    print("debug:\t" + msg)
    logging.debug(msg)
    