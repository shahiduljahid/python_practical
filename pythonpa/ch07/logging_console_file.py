import logging         #导入模块
#配置logging
logger = logging.getLogger(__name__)    #获取logger对象
logger.setLevel(level=logging.DEBUG)    #设置日志记录级别
handler = logging.FileHandler("logging_console_file.txt") #创建文件处理器对象用以记录详细信息
handler.setLevel(logging.DEBUG)        #设置日志级别
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)           #设置日志格式化参数
console = logging.StreamHandler()       #创建控制台处理器，输出错误信息
console.setLevel(logging.ERROR)       #设置日志记录级别
logger.addHandler(handler)             #把handler对象添加到logger对象
logger.addHandler(console)             #把console对象添加到logger对象
#输出日志信息
logger.debug("调试信息")
logger.info("一般信息")
logger.warning("警告信息")
logger.error("错误信息")
logger.critical("严重错误")
