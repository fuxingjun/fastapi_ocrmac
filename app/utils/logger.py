import logging
import os


class Logger(logging.Logger):
    def __init__(self, name, level=logging.INFO, file=None, stream=True):
        """
        封装日志类
        :param str name: 日志名称
        :param str level: 日志级别
        :param str file: 文件名称，不传时不会输出到文件
        """

        # 继承logging模块中的Logger类，因为里面实现了各种各样的方法，很全面，但是初始化很简单
        # 所以我们需要继承后把初始化再优化下，变成自己想要的。
        super().__init__(name, level)

        # 设置日志格式
        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s--%(lineno)dline :%(message)s"
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        if stream:
            handle1 = logging.StreamHandler()
            handle1.setFormatter(formatter)
            self.addHandler(handle1)
        # 文件输出渠道
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


def create_directory(filepath):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)


log_path = 'logs/my_log.log'
create_directory(log_path)
# 因为一个项目的日志都是写入到一个日志文件的，所以可以把name，file这两个参数写死，直接实例化
# 后期每个模块调用就不用实例化，导入可以直接使用
logger = Logger("log_name", file=log_path)

if __name__ == '__main__':
    mlogger = Logger("abc")
    mlogger.info("封装好的日志类，console")
    logger.info("封装好的日志，文件渠道测试")
