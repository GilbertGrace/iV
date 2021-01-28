''' Bootloader '''
from pdb import set_trace as pause
import os, sys, datetime, time, socket, getopt, getpass, signal, hashlib, glob, json, sqlite3, tkinter, center_tk_window

class StartupError(Exception): pass
class AuthError(Exception): pass
class Exit(Exception): pass

config:dict = {
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

with open('E:/Projects/iV Pro/required/etc/config.json', 'r') as f: config.update(json.loads(f.read()))

for _ in config['required']:
    if not os.path.join(config['root'], 'required', _) in sys.path: sys.path.append(os.path.join(config['root'], 'required', _))

class Client:
    running:bool

    def __init__(self) -> None:
        Client.running = True

    def __call__(self, *args:list, **kwds:dict) -> dict:
        o = input('> ').rstrip().split(':')

class Engine:
    def __init__(self) -> None:
        pass

client:Client = None; engine:Engine = None # processes
splash:tkinter.Tk = None;  editor:tkinter.Tk = None # windows

def report(message:str, verbose:bool=False): 
    with open(os.path.join(config['root'], config['etc_path'], config['log_file']), 'a') as log: log.write(f'[{datetime.datetime.now()}]: {message}\n')
    if verbose: print(message)

def loop() -> None:
    ''' Terminal thread loop '''
    client = Client()
    while (client.running): client()
    raise Exit # finished

def show():
    ''' Loads the editor '''
    global splash
    splash = tkinter.Tk()
    splash.title('Welcome')
    min_width = 600; min_height = 400
    splash.geometry('%sx%s+0+0' % (min_width, min_height))
    splash.resizable(0, 0)
    image = tkinter.PhotoImage(file = f"{config['root']}/{config['var_path']}/splash.gif") 
    handle = tkinter.Label( splash, image = image) 
    handle.place(x = 0, y = 0)
    button = tkinter.Button(splash, text ='Launch', command = start)
    button.pack()
    splash.wm_attributes('-topmost', True)
    splash.protocol('WM_DELETE_WINDOW', onexit)
    center_tk_window.center(splash, splash)
    #splash.after_idle(start)
    splash.mainloop()

def start(*args, **kwargs):
    global engine, editor, splash
    #engine = Engine()
    editor = tkinter.Tk()
    editor.title('iV Pro')
    min_width = 1280; min_height = 720
    editor.geometry('%sx%s+0+0' % (min_width, min_height))
    editor.minsize(min_width, min_height)
    editor.maxsize(editor.winfo_screenwidth(), editor.winfo_screenheight())
    #image = tkinter.PhotoImage(file = f"{config['root']}/{config['var_path']}/iris.png")
    #editor.iconphoto(False, image)
    #editor.wm_attributes("-disabled", True)
    editor.state('zoomed')
    center_tk_window.center(editor, editor)
    splash.destroy()

def onexit(): pass

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
                    print(config['copyright'])
                    for _ in config['help']: print(_)
                    sys.exit(1)
                elif o in ('-t', '--terminal'): loop()
                else: raise getopt.GetoptError()
        else: show(); raise Exit
    except AuthError as e: report('Authentication failed.', True); sys.exit(1)
    except getopt.GetoptError as e: report('Unhandled option.', True); sys.exit(1)
    except Exit as e: os.system('cls'); report('Session ended.'); sys.exit(1)