# Python 标准模块学习

Python Builtin Module

## logging 模块

logging 模块主要是实现事件日志功能，其官方文档为[logging](https://docs.python.org/3/library/logging.html)。

`__code__`用于获取函数的编译后的字节码以及函数相关信息

- LogRecord 类用于记录需要记录的信息
- Formatter 类用于将`LogRecord`中的信息进行格式化
- Filter 类用于过滤指定的日志记录
- Handler 类用于指定日志的目的地，标准输出还是文件等
- Manager 类用于管理层次化的 logger
- Logger 类是用于利用日志的接口类
