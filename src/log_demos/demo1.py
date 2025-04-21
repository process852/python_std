import logging

# 创建一个名为 __name__ 的logger
logger = logging.getLogger(__name__)


def main():
    # 配置 Handlers 和 Formatters 用于格式化输出内容
    # 将日志输出到指定文件
    # file_handler = logging.FileHandler("demo1.log", mode='a', encoding='utf-8')
    # asctime 用于指代格式化日期时间
    # formater = logging.Formatter(
    #     fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    #     datefmt="%Y-%m-%d %H:%M:%S")
    logging.basicConfig(
        level=logging.INFO, 
        filename="demo1.log",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",)
    logger.info("This is an info message")

if __name__ == "__main__":
    main()
    print(main.__code__.co_filename)