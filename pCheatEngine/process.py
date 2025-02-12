import win32api
import win32con
import psutil

def getProcess(pid:int) -> psutil.Process:
    return psutil.Process(pid)

def getProcessCwd(process:psutil.Process) -> str:
    return process.cwd()

def getProcessName(process:psutil.Process) -> str:
    return process.name()

def getProcessIdDict() -> dict:
    pid_list = psutil.pids()
    pid_dict = {}
    for pid in pid_list:
        pid_dict[pid] = getProcessName(getProcess(pid))
    return pid_dict

def getProcessId(pid_dict:dict, processName:str) -> list:
    pid_list = []
    for pid, pid_name in pid_dict.items():
        if pid_name == processName:
            pid_list.append(pid)
    return pid_list

def getProcessIdByName(processName:str) -> list:
    pid_dict = getProcessIdDict()
    return getProcessId(pid_dict, processName)

def openProcess(pid:int) -> int:
    return win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)

def closeProcess(processHandle:int) -> None:
    win32api.CloseHandle(processHandle)