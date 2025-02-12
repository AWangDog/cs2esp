# python -m nuitka --follow-imports --standalone --onefile --windows-console-mode=disable --enable-plugin=tk-inter --mingw64 --output-dir=out --windows-product-version=1.0.0 --remove-output --product-name=Network_Information --file-description=CS2ESP --output-filename=CS2ESP start.py 
import os, tkinter as tk, pystray, threading, sys, psutil
from PIL import Image, ImageDraw
import key
import subprocess
from pynput import mouse
import threading

def get_program_name_by_pid(pid):
    try:
        process = psutil.Process(pid)
        return process.name()
    except psutil.NoSuchProcess:
        return None

def create_image():
    width = 64
    height = 64
    color1 = (0, 0, 0)
    color2 = (255, 255, 255)
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((10, 10, 54, 54), fill=color2)
    dc.text((15, 20), "A", fill=color1)
    dc.text((15, 40), "B", fill=color1)
    return image

FILE_NAME = os.path.splitext(get_program_name_by_pid(os.getpid()))[0]
if os.path.isfile('icon.ico'):
    ICON = Image.open('icon.ico')
elif os.path.isfile('icon.jpg'):
    ICON = Image.open('icon.jpg')
    ICON.save('temp.ico')
else:
    ICON = create_image()
def main():
    icon = pystray.Icon("test_icon", ICON, FILE_NAME, pystray.Menu(
        pystray.MenuItem('开启/关闭', toggle_visibility),
        pystray.MenuItem('退出', exit_)
    ))
    def setup(icon):
        icon.visible = True
    tray_icon_thread = threading.Thread(target=icon.run, args=(setup,))
    tray_icon_thread.daemon = True
    tray_icon_thread.start()

def toggle_visibility():
    global start
    threading.Thread(target=toggle_start, args=(start,)).start()

def exit_():
    if 'icon' in globals() and icon is not None: # type: ignore
        icon.stop() # type: ignore
    if 'root' in globals() and root is not None: 
        root.quit()
        root.destroy()
    if 'mouse_listener' in globals() and mouse_listener is not None:
        mouse_listener.stop()
    sys.exit(0)

def on_click(x, y, button, pressed):
    global start
    global mouse4_pressed
    if button == mouse.Button.x1:
        if pressed:
            mouse4_pressed = True
            threading.Thread(target=toggle_start, args=(start,)).start()

def toggle_start(switch):
    global start, tfa
    if not switch:
        subprocess.run(f'LogWriter.exe 1 -path {tfa}', shell=True, capture_output=True, text=True)
    else:
        subprocess.run(f'LogWriter.exe 0 -path {tfa}', shell=True, capture_output=True, text=True)
    start = not start

def start_mouse_listener():
    mouse_listener.start()

if __name__ == '__main__':
    start = False
    tfa = key.get_2fa(key.Key().key)
    
    mouse4_pressed = False
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_thread = threading.Thread(target=start_mouse_listener)
    mouse_thread.start()
    
    main()
    root = tk.Tk()
    root.withdraw()
    root.title(FILE_NAME)
    ICON.save('temp.ico')
    root.iconbitmap('temp.ico')
    os.remove('temp.ico')
    root.mainloop()