# cs2esp
基于python的cs2透视
# 文件
- pCheatEngine : 进程和内存操作库
- main.py : 主要透视实现
- start.py : 启动实现
- key.py : 两步验证加密实现
# 打包指令
- `python -m nuitka --standalone --onefile --windows-console-mode=disable --mingw64 --output-dir=out --remove-output --windows-uac-admin --product-name=LogWriter --file-description=LogWriter --product-version=1.0.0 --file-version=1.0.0 --output-filename=LogWriter main.py`
- `python -m nuitka --follow-imports --standalone --onefile --windows-console-mode=disable --enable-plugin=tk-inter --mingw64 --output-dir=out --windows-product-version=1.0.0 --remove-output --product-name=Network_Information --file-description=CS2ESP --output-filename=CS2ESP start.py`
# 原理
- main.py表面伪装成日志记录器, 通过2fa与主程序沟通, 接受到启用/停止esp指令后对cs2内存进行写入
# 关于
- 此程序仅用于学习目的, 请在24h内删除此程序
