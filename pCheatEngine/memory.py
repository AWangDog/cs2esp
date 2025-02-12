import win32process
import win32con
import pymem
from enum import Enum
from . import types

class AllocationType(Enum):
    MEM_COMMIT = win32con.MEM_COMMIT
    MEM_RESERVE = win32con.MEM_RESERVE
    MEM_RESET = 0x80000
    MEM_RESET_UNDO = 0x1000000
    MEM_LARGE_PAGES = 0x20000000
    MEM_PHYSICAL = 0x400000
    MEM_TOP_DOWN = win32con.MEM_TOP_DOWN
    MEM_WRITE_WATCH = 0x200000
    MEM_PHYSICAL_CONTIGUOUS = 0x40000000
    MEM_LARGE_PAGES_2MB = 0x80000000

win32process.VirtualAllocEx

def read(processHandle:int, address:int, size:int) -> bytes:
    return win32process.ReadProcessMemory(processHandle, address, size)

def write(processHandle:int, address:int, bytes_:bytes) -> None:
    win32process.WriteProcessMemory(processHandle, address, bytes_)
    
def alloc(processHandle:int, size:int, type_:AllocationType, protection:int, lpAddress = 0):
    return win32process.VirtualAllocEx(processHandle, lpAddress, size, type_, protection)

def dealloc(processHandle:int, lpAddress:int, size:int, type_:int):
    return win32process.VirtualFreeEx(processHandle, lpAddress, size, type_)

def getModuleAddr(processHandle, moduleName):
    process = pymem.Pymem(win32process.GetProcessId(processHandle))
    modules = list(process.list_modules())
    for module in modules:
        if module.name == moduleName:
            ModuleAddr = module.lpBaseOfDll
    return ModuleAddr
    