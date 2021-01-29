''' Bootloader '''
from pdb import set_trace as pause
import os, sys, datetime, time, socket, getopt, getpass, signal, hashlib, glob, json, sqlite3, tkinter, center_tk_window, binascii

class StartupError(Exception): pass
class AuthError(Exception): pass
class Exit(Exception): pass

config:dict = {
    'version' : '1.0',
    'splash' : 'E:/Projects/iV Pro',
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

pool:dict = dict() # data

with open('E:/Projects/iV Pro/required/etc/config.json', 'r') as f: config.update(json.loads(f.read()))

for _ in config['required']:
    if not os.path.join(config['splash'], 'required', _) in sys.path: sys.path.append(os.path.join(config['splash'], 'required', _))

class Client:
    running:bool = False

    @staticmethod
    def execute(self, *args:list, **kwds:dict) -> dict:
        o = input('> ').rstrip().split('::')#; pause()
        if o[0] == 'serialise':
            with open(o[1], 'r') as f: write(f.read(), o[2])
        #elif o[0] == '': pass
        else: print('syntax error')

class Engine:
    def __init__(self) -> None:
        global pool, splash, progress
        report('Engine waking...')
        x:object = None
        
        # load modules
        modules = glob.glob('E:/Projects/iV Pro/required/var/modules/*.sfx')
        length = len(modules); count = 1
        if length: progress_chunk_size = round(100 / length)
        else: progress_chunk_size = 100

        for _ in modules:
            with open(_, 'r') as f: pool.update(json.loads(bytes.fromhex(read(f.read())).replace(b'\n', b'').replace(b' ', b'').replace(b'##', b' ')))
            time.sleep(0.1)
            progress['value'] = progress_chunk_size * count; 
            splash.update_idletasks()
            count += 1

        #time.sleep(0.2)
        progress['value'] = 100
        report('Engine awake')

    def render(): return

splash:tkinter.Tk = None;  editor:tkinter.Tk = None; engine:Engine = None; progress:object = None

def report(message:str, verbose:bool=False): 
    with open(os.path.join(config['splash'], config['etc_path'], config['log_file']), 'a') as log: log.write(f'[{datetime.datetime.now()}]: {message}\n')
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
    import ttk
    global splash, progress
    splash = tkinter.Tk()
    splash.title('Welcome')
    min_width = 600; min_height = 400
    splash.geometry('%sx%s+0+0' % (min_width, min_height))
    splash.resizable(0, 0)
    image = tkinter.PhotoImage(file = f"{config['splash']}/{config['var_path']}/media/splash.gif") 
    handle = tkinter.Label( splash, image = image) 
    handle.place(x = 0, y = 0)
    button = tkinter.Button(splash, text ='Launch', command = start)
    button.pack()
    progress = ttk.Progressbar(splash, orient = tkinter.HORIZONTAL, length = 100, mode = 'determinate')
    progress.pack(pady = 10)
    splash.wm_attributes('-topmost', True)
    splash.protocol('WM_DELETE_WINDOW', closing)
    center_tk_window.center(splash, splash)
    #splash.after_idle(start)
    splash.mainloop()

def start(*args, **kwargs):
    import ttk
    global engine, editor, splash, progress
    #engine = Engine()

    editor = tkinter.Tk()
    editor.wm_attributes("-disabled", True)
    editor.title('iV Pro')
  
    min_width = 1280; min_height = 720
    editor.geometry('%sx%s+0+0' % (min_width, min_height))
    editor.minsize(min_width, min_height)
    editor.maxsize(editor.winfo_screenwidth(), editor.winfo_screenheight())
    #image = tkinter.PhotoImage(file = f"{config['splash']}/{config['var_path']}/iris.png")
    #editor.iconphoto(False, image)
    menubar = tkinter.Menu(editor)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=closing)
    filemenu.add_command(label="Open", command=closing)
    filemenu.add_command(label="Save", command=closing)
    filemenu.add_command(label="Save as...", command=closing)
    filemenu.add_command(label="Close", command=closing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=editor.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = tkinter.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=closing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=closing)
    editmenu.add_command(label="Copy", command=closing)
    editmenu.add_command(label="Paste", command=closing)
    editmenu.add_command(label="Delete", command=closing)
    editmenu.add_command(label="Select All", command=closing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=closing)
    helpmenu.add_command(label="About...", command=closing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    editor.config(menu=menubar)

    tabControl = ttk.Notebook(editor)

    project = ttk.Frame(tabControl)
    tabControl.add(project, text ='Project')

    viewport = ttk.Frame(tabControl)
    tabControl.add(viewport, text ='Viewport')
    
    browser = ttk.Frame(tabControl)
    tabControl.add(browser, text ='Browser')
    
    texture = ttk.Frame(tabControl)
    tabControl.add(texture, text ='Texture')

    illustration = ttk.Frame(tabControl)
    tabControl.add(illustration, text ='Illustration')

    animation = ttk.Frame(tabControl)
    tabControl.add(animation, text ='Animation')

    sculpting = ttk.Frame(tabControl)
    tabControl.add(sculpting, text ='Sculpting')

    scripting = ttk.Frame(tabControl)
    tabControl.add(scripting, text ='Scripting')

    sequence = ttk.Frame(tabControl)
    tabControl.add(sequence, text ='Sequence')

    export = ttk.Frame(tabControl)
    tabControl.add(export, text ='Export')

    tabControl.pack(expand = 1, fill ="both", side='top')

    #ttk.Label(tab1, text ="Welcome to \ GeeksForGeeks").grid(column = 0, row = 0, padx = 30, pady = 30)
    #ttk.Label(tab2, text ="Lets dive into the\ world of computers").grid(column = 0, row = 0, padx = 30, pady = 30)
    editor.state('zoomed')
    center_tk_window.center(editor, editor)

    engine = Engine()
    closing()

def closing(): editor.wm_attributes("-disabled", False); splash.destroy()

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