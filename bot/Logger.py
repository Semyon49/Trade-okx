import logging

def setup_logger():
    logging.basicConfig(filename="mylog.log", level=logging.DEBUG, format="%(asctime)s %(levelname).3s | %(message)s", datefmt="%m/%d %H:%M:%S")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(fmt="%(asctime)s %(levelname).3s | %(message)s", datefmt="%m/%d %H:%M:%S"))
    
    logger = logging.getLogger('Trade-Bot')
    logger.addHandler(console_handler) 
    return logger
