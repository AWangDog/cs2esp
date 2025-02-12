import wmi
import base64
import pyotp
import time

def string_to_base32(input_string):
    byte_data = input_string.encode('utf-8')
    base32_data = base64.b32encode(byte_data)
    base32_string = base32_data.decode('utf-8')
    return base32_string

class Key:
    def __init__(self):
        self.s = wmi.WMI()
        self.key = self.get_key()
    def get_CPU_info(self):
            cpu = []
            cp = self.s.Win32_Processor()
            for u in cp:
                cpu.append(
                    {
                        "Name": u.Name,
                        "Serial Number": u.ProcessorId,
                        "CoreNum": u.NumberOfCores
                    }
                )
            return cpu
    def get_disk_info(self):
        disk = []
        for pd in self.s.Win32_DiskDrive():
            disk.append(
                {
                    "Serial": self.s.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip(),  # 获取硬盘序列号，调用另外一个win32 API
                    "ID": pd.deviceid,
                    "Caption": pd.Caption,
                    "size": str(int(float(pd.Size) / 1024 / 1024 / 1024)) + "G"
                }
            )
        return disk
    def get_network_info(self):
        network = []
        for nw in self.s.Win32_NetworkAdapterConfiguration():
            if nw.MACAddress != None:
                network.append(
                    {
                        "MAC": nw.MACAddress,
                        "ip": nw.IPAddress
                    }
                )
        return network
    def get_mainboard_info(self):
        mainboard = []
        for board_id in self.s.Win32_BaseBoard():
            mainboard.append(board_id.SerialNumber.strip().strip('.'))
        return mainboard

    def get_key(self):
        a = self.get_disk_info()
        
        # b = self.get_CPU_info()
        
        # c = self.get_network_info()
        
        d = self.get_mainboard_info()
        # machinecode_str = a[0]['Serial'] + b[0]['Serial Number'] + c[0]['MAC'] + d[0]
        machinecode_str = a[0]['Serial'] + d[0]
        return string_to_base32(machinecode_str)

def get_2fa(key, time_shift = 0):
    long = 30
    long_shift = time_shift * long
    totp = pyotp.TOTP(key, interval=long)
    return totp.at(int(time.time()) + long_shift)

if __name__ == '__main__':
    key = Key()
    print(key.key)
    print(get_2fa(key.key, -1))
    print(get_2fa(key.key))
    print(get_2fa(key.key, 1))