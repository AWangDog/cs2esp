# cs2esp
基于python的cs2透视
# 文件
- pCheatEngine : 进程和内存操作库
- main.py : 主要透视实现
- start.py : 启动实现
- key.py : 两步验证加密实现
# 原理
- main.py表面伪装成日志记录器, 通过2fa与主程序沟通, 接受到启用/停止esp指令后对cs2内存进行写入
# 关于
- 此程序仅用于学习目的, 请在24h内删除此程序
