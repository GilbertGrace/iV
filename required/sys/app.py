''' Bootloader '''
from pdb import set_trace as pause
import os, sys, datetime, socket, getopt, getpass, signal, hashlib, glob, json, sqlite3, tkinter

class StartupError(Exception): pass
class AuthError(Exception): pass
class Exit(Exception): pass

class Client:
    def __init__(self) -> None:
        pass

class Engine:
    def __init__(self) -> None:
        pass

class Editor(tkinter.Toplevel):
    def __init__(self) -> None:
        pass

splash:tkinter.Tk = None
client:Client = None
editor:Editor = None
engine:Engine = None
config:dict = dict()

def check() -> bool:
    ''' Verify system '''
    if hashlib.sha256(bytes(socket.gethostbyname(socket.gethostname()), 'utf_8')).hexdigest() == 'd23ff466e452db6e45e4c1bac2bdb4ce3bf9fd37789500b266f4145c7bb209dc': return True
    elif hashlib.sha256(bytes(getpass.getpass('password: '), 'utf_8')).hexdigest() == '4d164cbf641eabdcfd4a61eab475f245a559a3f8b287618fb3d414b07eea86df': return True
    else: raise AuthError()

def init():
    ''' Prepare environment '''
    global config, client, splash
    check()
    with open('E:/Projects/iV Pro/required/etc/config.json', 'r') as f: config.update(json.loads(f.read()))
    client = Client()
    splash = tkinter.Tk()
    report('Session started.')

def loop() -> dict:
    '''  '''
    return dict()

def show():
    splash.mainloop()

def build():
    ''' Load application data '''
    global engine, editor
    engine = Engine()
    editor = Editor()

def report(message:str, verbose:bool=False): 
    with open(os.path.join(config['root'], config['etc_path'], config['log_file']), 'a') as log: log.write(f'[{datetime.datetime.now()}]: {message}\n')
    if verbose: print(message)

if __name__ == '__main__':
    try:
        def shutdown(signum, frame): raise Exit()
        signal.signal(signal.SIGINT, shutdown)
        opts, args = getopt.getopt(sys.argv[1:], 'ht', ['help', 'terminal'])

        if len(opts):
            for o, a in opts:
                if o in ('-h', '--help'):
                    print(config['copyright'])
                    for _ in config['help']: print(_)
                    sys.exit(1)
                elif o in ('-t', '--terminal'):
                    init()

                    for _ in config['required']:
                        if not os.path.join(config['root'], 'required', _) in sys.path: sys.path.append(os.path.join(config['root'], 'required', _))

                    loop()
                else: raise getopt.GetoptError()
        else:
            init()

            for _ in config['required']:
                if not os.path.join(config['root'], 'required', _) in sys.path: sys.path.append(os.path.join(config['root'], 'required', _))
                
            show()
        
    except StartupError as e: init()
    except AuthError as e: report('Authentication failed.', True); sys.exit(1)
    except getopt.GetoptError as e: os.system('cls'); report('Unhandled option.'); sys.exit(1)
    except Exit as e: os.system('cls'); report('Force exit.'); sys.exit(1)