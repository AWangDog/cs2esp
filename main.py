# python -m nuitka --standalone --onefile --windows-console-mode=disable --mingw64 --output-dir=out --remove-output --windows-uac-admin --product-name=LogWriter --file-description=LogWriter --product-version=1.0.0 --file-version=1.0.0 --output-filename=LogWriter main.py
import pCheatEngine as pce
import argparse
import os, sys
import key

ORG = 0xc032
NEW = 0x9090
parser = argparse.ArgumentParser(description="log writer")
parser.add_argument('log', help='Log that need to be entered.')
parser.add_argument('-path', help='Output path.')
if len(sys.argv) <= 1:
    parser.print_help()  # 打印帮助信息
    sys.exit(0)  # 退出程序
args = parser.parse_args()

def clearMem(s):
    processHandle = pce.process.openProcess(pce.process.getProcessIdByName("cs2.exe")[0])
    client_dll = pce.memory.getModuleAddr(processHandle, "client.dll")
    asmAddr = client_dll + 0x867D50
    if s:
        pce.memory.write(processHandle, asmAddr, NEW.to_bytes(2, byteorder="little"))
    else:
        pce.memory.write(processHandle, asmAddr, ORG.to_bytes(2, byteorder="little"))
    pce.process.closeProcess(processHandle)

def writeLog(log):
    if not args.path or not os.path.exists(args.path):
        path = os.path.splitdrive(os.getcwd())[0] + '\\log.log'
    else:
        path = args.path
    with open(path, "w") as f:
        f.write(log)

if args.path in [key.get_2fa(key.Key().key, -1), 
                key.get_2fa(key.Key().key),
                key.get_2fa(key.Key().key, 1)]:
    clearMem(args.log == '1')
else:
    writeLog(args.log)