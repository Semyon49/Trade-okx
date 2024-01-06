from bot.Logger import setup_logger
from bot import Bot
from dotenv import load_dotenv
from okx.exceptions import OkxAPIException

def main():
    logger = setup_logger()
    load_dotenv()

    try:
        Bot().run()
    except KeyboardInterrupt:
        logger.debug("Бот остановлен вручную!")
    except OkxAPIException as e:
        logger.debug(str(e))
    except Exception as e:
        logger.error(str(e))

if __name__ == '__main__':
    main()
