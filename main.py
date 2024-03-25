import logging


logging.basicConfig(filemode='a',filename='new.log',
                    level=logging.INFO,
                    format='%(levelname)s-%(asctime)s - %(created)f -%(filename)s -%(funcName)s')


logging.debug('debug')
logging.info('info')
logging.warning('warning')


print(20)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
