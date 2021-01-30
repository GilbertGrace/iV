''' Bootloader '''
from pdb import set_trace as pause
import os, sys, datetime, time, socket, getopt, getpass, signal, hashlib, glob, json, sqlite3, center_tk_window, binascii

class StartupError(Exception): pass
class AuthError(Exception): pass
class Exit(Exception): pass

# data
stack:dict = {
    'version' : '1.0',
    'root' : 'E:/Projects/iV Pro',
    'etc_path' : 'required/etc',
    'var_path' : 'required/var',
    'connection_string' : 'system.db',
    'config_file' : 'config.json',
    'log_file' : 'access.log',
    'copyright' : '\u00a9 2021 KOJAN Group LLP, all rights reserved.',
    'author' : 'Tanaka Mutsatsa',
    'date' : '31/1/2021',
    'company' : 'Studio KOJAN',
    'tel' : '07398290770',
    'email' : 'admin@studiokojan.com',
    'public_release' : False,
    'password' : '4d164cbf641eabdcfd4a61eab475f245a559a3f8b287618fb3d414b07eea86df',
    'authorised' : [
        'd23ff466e452db6e45e4c1bac2bdb4ce3bf9fd37789500b266f4145c7bb209dc'
    ],
    'required' : ['lib', 'sys'],
    'help' : [
        '-t : launch terminal',
        '-h : show this dialog'
    ]
}

with open(os.path.join(stack['root'], stack['etc_path'], stack['config_file']), 'r') as f: stack.update(json.loads(f.read()))

for _ in stack['required']:
    if not os.path.join(stack['root'], 'required', _) in sys.path: sys.path.append(os.path.join(stack['root'], 'required', _))

from tkinter import *
from ttk import *

class Client:
    running:bool = False

    @staticmethod
    def execute(*args:list, **kwds:dict) -> dict:
        o = input('> ').rstrip().split('::')#; pause()
        if o[0] == 'serialise':
            with open(o[1], 'r') as f: write(f.read(), o[2])
        #elif o[0] == '': pass
        else: print('syntax error')

class Engine:
    def __init__(self) -> None:
        global stack, splash, progress
        report('Engine waking...')
        
        # load modules to stack
        modules = glob.glob('E:/Projects/iV Pro/required/var/modules/*.sfx')
        length = len(modules); count = 1
        if length: progress_chunk_size = round(100 / length)
        else: progress_chunk_size = 100

        for _ in modules:
            with open(_, 'r') as f: o = json.loads(bytes.fromhex(read(f.read())).replace(b'\n', b'').replace(b' ', b'').replace(b'##', b' ')); stack.update(o)
            time.sleep(0.25) # animate progress
            progress['value'] = progress_chunk_size * count; 
            splash.update_idletasks() # update graphics
            count += 1
        progress['value'] = 100 # done
        report('Engine awake')

    def render(): return

splash:Tk = None;  editor:Tk = None; engine:Engine = None; progress:object = None

def report(message:str, verbose:bool=False): 
    with open(os.path.join(stack['root'], stack['etc_path'], stack['log_file']), 'a') as log: log.write(f'[{datetime.datetime.now()}]: {message}\n')
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
    while (Client.running): Client.execute()
    raise Exit # finished

def show():
    ''' Loads the editor '''
    global splash, progress
    splash = Tk()
    splash.title('Welcome')
    min_width = 600; min_height = 400
    splash.geometry('%sx%s+0+0' % (min_width, min_height))
    splash.resizable(0, 0)
    image = PhotoImage(file = f"{stack['root']}/{stack['var_path']}/media/splash.gif") 
    handle = Label( splash, image = image) 
    handle.place(x = 0, y = 0)
    button = Button(splash, text ='Launch', command = start)
    button.pack()
    progress = Progressbar(splash, orient = HORIZONTAL, length = 100, mode = 'determinate')
    progress.pack(pady = 10)
    splash.wm_attributes('-topmost', True)
    splash.protocol('WM_DELETE_WINDOW', closing)
    center_tk_window.center(splash, splash)
    #splash.after_idle(start)
    splash.mainloop()

def draw() -> None:
    global stack
    done:bool = False
    target = []
    names = []
    
    for key, val in stack.items():
        if isinstance(val, dict) and 'constructor' in val:
            target.append(key)

    while(not done):
        for key in target:
            if not key in names:
                o:object = None
                constructor = stack[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '#': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                
                properties = stack[key]['properties']
                
                for prop in properties:
                    for _ in prop['options']:
                        if isinstance(prop['options'][_], str) and prop['options'][_][0] == '#': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                
                o = getattr(sys.modules[__name__], stack[key]['type'])(getattr(sys.modules[__name__], stack[key]['parent']), **constructor) # create object

                for prop in properties: getattr(o, prop['method'])(**prop['options']) # implement property
                
                if o: names.append(key)
                else: o = None
        if names.sort() == target.sort(): done = True
        else: done = False

def start(*args, **kwargs):
    global engine, editor, splash, progress
    #engine = Engine()

    editor = Tk()
    editor.wm_attributes("-disabled", True)
    editor.title('iV Pro')
  
    min_width = 1280; min_height = 720
    editor.geometry('%sx%s+0+0' % (min_width, min_height))
    editor.minsize(min_width, min_height)
    editor.maxsize(editor.winfo_screenwidth(), editor.winfo_screenheight())
    #image = PhotoImage(file = f"{stack['root']}/{stack['var_path']}/iris.png")
    #editor.iconphoto(False, image)
    editor.state('zoomed')
    center_tk_window.center(editor, editor)
    engine = Engine()
    draw()
    closing()

def closing():
    global splash, editor
    if editor: editor.wm_attributes("-disabled", False)
    splash.destroy()

# entry point
if __name__ == '__main__':
    try:
        if hashlib.sha256(bytes(socket.gethostbyname(socket.gethostname()), 'utf_8')).hexdigest() == 'd23ff466e452db6e45e4c1bac2bdb4ce3bf9fd37789500b266f4145c7bb209dc': pass
        elif hashlib.sha256(bytes(getpass.getpass('password: '), 'utf_8')).hexdigest() == '4d164cbf641eabdcfd4a61eab475f245a559a3f8b287618fb3d414b07eea86df': pass
        else: raise AuthError()
        def shutdown(signum, frame): raise Exit()
        signal.signal(signal.SIGINT, shutdown)
        opts, args = getopt.getopt(sys.argv[1:], 'ht', ['help', 'terminal'])
        report('Session started.')
        if len(opts):
            for o, a in opts:
                if o in ('-h', '--help'):
                    print(stack['copyright'])
                    for _ in stack['help']: print(_)
                    sys.exit(1)
                elif o in ('-t', '--terminal'): loop()
                else: raise getopt.GetoptError()
        else: show(); raise Exit
    except AuthError as e: report('Authentication failed.', True); sys.exit(1)
    except getopt.GetoptError as e: report('Unhandled option.', True); sys.exit(1)
    except Exit as e: os.system('cls'); report('Session ended.'); sys.exit(1)