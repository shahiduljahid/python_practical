import logging           #导入模块
#配置logging
logging.basicConfig(level = logging.INFO
            ,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#输出日志信息
logging.debug("调试信息")  #不会输出
logging.info("一般信息")
logging.warning("警告信息")
logging.error("错误信息")
logging.critical("严重错误")
