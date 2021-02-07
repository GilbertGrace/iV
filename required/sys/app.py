''' Bootstrap '''

from pdb import set_trace as pause
from varname.helpers import Wrapper
from uuid import getnode as get_mac
import os, sys, datetime, time, socket, getopt, getpass, signal, hashlib, glob, json, sqlite3, center_tk_window, binascii, random, string

class StartupError(Exception): pass
class AuthError(Exception): pass
class Exit(Exception): pass

# data
cache:dict = {
    'root' : 'E:/Projects/iV Pro',
    'etc_path' : 'required/etc',
    'var_path' : 'required/var',
    'config_file' : 'config.json'
}

with open(os.path.join(cache['root'], cache['etc_path'], cache['config_file']), 'r') as f: cache.update(json.loads(f.read()))

for _ in cache['required']:
    if not os.path.join(cache['root'], 'required', _) in sys.path: sys.path.append(os.path.join(cache['root'], 'required', _))

import tkinter, ttk; from tkinter import *; from ttk import *; from editor import *; from engine import *; from client import *; from dev import *

splash:tkinter.Tk = None;  editor:tkinter.Tk = None; engine:Engine = None; progress:object = None

def report(message:str, verbose:bool=False): 
    with open(os.path.join(cache['root'], cache['etc_path'], cache['log_file']), 'a') as log: log.write(f'[{datetime.datetime.now()}]: {message}\n')
    if verbose: print(message)

def read(source:str) -> str:
    ''' Deserialise '''
    return source

def write(source:str, target:str):
    ''' Serialise '''
    with open(target, 'wb') as f: f.write(binascii.hexlify(bytes(source, 'utf-8')))

def loop() -> None:
    ''' Terminal thread loop '''
    Client.running = True
    os.system('cls')
    while (Client.running): Client.execute()
    raise Exit # finished

def start(*args, **kwargs):
    ''' bootstrap '''
    global engine, editor, splash, progress
    engine = Engine(progress, splash, cache)#; pause()
    editor = Editor(cache, engine)
    editor.wm_attributes("-disabled", True)
    editor.title('iV Pro')
    min_width = 1280; min_height = 720
    editor.geometry('%sx%s+0+0' % (min_width, min_height))
    editor.minsize(min_width, min_height)
    editor.maxsize(editor.winfo_screenwidth(), editor.winfo_screenheight())
    editor.state('zoomed')
    center_tk_window.center(editor, editor)
    closing()#; pause()
    #editor.winfo_toplevel().iconphoto(False, PhotoImage(file = f"{cache['root']}/{cache['var_path']}/media/iris.png"))

def show():
    ''' splashscreen '''
    global splash, progress
    splash = tkinter.Tk()
    splash.winfo_toplevel().iconphoto(False, PhotoImage(file = f"{cache['root']}/{cache['var_path']}/media/iris.png"))
    splash.title('Start Page')
    min_width = 600; min_height = 400
    splash.geometry('%sx%s+0+0' % (min_width, min_height))
    splash.resizable(0, 0)
    splash.overrideredirect(1) #Remove border
    image = tkinter.PhotoImage(file = f"{cache['root']}/{cache['var_path']}/media/splash.gif") 
    handle = tkinter.Label( splash, image = image) 
    handle.place(x = 0, y = 0)
    #button = tkinter.Button(splash, text ='Launch', command = start)
    #button.pack()
    #progress = ttk.Progressbar(splash, orient = tkinter.HORIZONTAL, length = 900, mode = 'determinate')
    #progress.pack(pady = 10, side='bottom')
    splash.wm_attributes('-topmost', True)
    splash.protocol('WM_DELETE_WINDOW', closing)
    center_tk_window.center(splash, splash)
    splash.after_idle(start)
    splash.mainloop()

def closing():
    global splash, editor
    if editor: editor.wm_attributes("-disabled", False)
    splash.destroy()
    Client.running = False

# entry point
if __name__ == '__main__':
    try:
        if hashlib.sha256(bytes(socket.gethostbyname(socket.gethostname()), 'utf_8')).hexdigest() in cache['authorised']: pass
        elif hashlib.sha256(bytes(getpass.getpass('password: '), 'utf_8')).hexdigest() == cache['password']: pass
        else: raise AuthError()
        def shutdown(signum, frame): raise Exit()
        signal.signal(signal.SIGINT, shutdown)
        opts, args = getopt.getopt(sys.argv[1:], 'ht', ['help', 'terminal'])
        report('Session started.')
        if len(opts):
            for o, a in opts:
                if o in ('-h', '--help'):
                    print(cache['copyright'])
                    for _ in cache['help']: print(_)
                    sys.exit(1)
                elif o in ('-t', '--terminal'): loop()
                else: raise getopt.GetoptError()
        else: show(); raise Exit
    except StartupError as e: report('Startup failed.', True); sys.exit(1)
    except AuthError as e: report('Authentication failed.', True); sys.exit(1)
    except getopt.GetoptError as e: report('Unhandled option.', True); sys.exit(1)
    except Exit as e: os.system('cls'); report('Session ended.'); sys.exit(1)