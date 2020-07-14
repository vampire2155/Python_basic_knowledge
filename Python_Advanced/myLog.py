# -*- coding: utf-8 -*-

import logging
import os

def create_logger(logPath):
    # 创建一个日志对象
    logger = logging.getLogger(os.path.split(logPath)[1])
    # 设置记录级别
    logger.setLevel(logging.INFO)

    # 打开指定的文件并将其作为日志记录的位置--日志记录流
    fh = logging.FileHandler(logPath)
    # 定义日志输出格式
    formatter = logging.Formatter("\n\n{}\n%(asctime)s - %(name)s - %(levelname)s - %(message)s".format("="*100))
    fh.setFormatter(formatter)

    # 往 logger 中添加输出方式
    logger.addHandler(fh)
    return logger

apiLog = create_logger(r"G:\Python_scripts\Python_Advanced\api.log")

def decoratelog(func):
    """
    日志装饰器
    :param func: 被装饰函数的函数名
    :return:
    """
    def wrapper(*args, **kwargs):
        logger = create_logger(r"G:\Python_scripts\Python_Advanced\error.log")
        try:
            func(*args, **kwargs)
        except Exception as e:
            # 记录异常
            err = "异常发生在：{}, 内容：{}".format(func.__name__, e)
            print("报错产生了")
            # 特别适合记录异常信息的一个方法
            logger.exception(err)
    return wrapper

# 只有当前文件调用的时候才会执行， 被其他模块调用，不会执行
# 通常被用来测试本模块函数功能是否正常
if __name__ == '__main__':
    @decoratelog
    def foo():
        print(a)
    foo()
