import logging
import os


class Logger:
    def __init__(self, logfile, cmd_level, file_level):
        # 创建日志对象
        self.logger = logging.getLogger(logfile)
        # 设置等级
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(cmd_level)

        # 设置文件日志
        fh = logging.FileHandler(logfile)
        fh.setFormatter(fmt)
        fh.setLevel(file_level)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def debug(self, message):
        self.logger.debug(message)

    def warn(self, message):
        self.logger.warning(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logger = Logger('test_log.log', logging.DEBUG, logging.DEBUG)
    logger.debug('debug message')
    logger.info('info_message')
    logger.warn('warning message')
    logger.error('error message')
    logger.critical('critical message')
