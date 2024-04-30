import os
import logging
import pathes as path
logging.basicConfig(filename=path.logging,
                    encoding='utf-8', 
                    level=logging.DEBUG,
                    format='%(asctime)s \t %(name)s \t %(levelname)s \t %(message)s')
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
    