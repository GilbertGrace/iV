''' Bootstrap '''

class Exit(Exception): pass
class AuthenticationError(Exception): pass
class OptionError(Exception): pass

from pdb import set_trace as pause
from uuid import getnode as get_mac
from varname.helpers import Wrapper
import sys, os, signal, getopt, getpass, tkinter, random, string, center_tk_window

# this object is required for the application to work
startupConfiguration:dict = {
    'root' : 'E:/Projects/iV Pro/required',
    'logFile' : 'etc/access.log',
    'source' : 'var/src',
    'etcPath' : 'etc',
    'varPath' : 'var',
    'session' : {},
    'required' : [ 'lib', 'sys' ],
    'content' : [ 'assets', 'playbooks', 'frameworks']
}

app:tkinter.Tk = None; splash:tkinter.Tk = None; progress:object = None

def stub():pass

def loadConfigs() -> any:
    global startupConfiguration
    from glob import glob
    from json import loads

    root:str = startupConfiguration['root']
    etcPath:str = startupConfiguration['etcPath']
    length = len(f'{os.path.join(root, etcPath)}/')

    for _ in glob(f'{os.path.join(root, etcPath)}/*.json'):
        if _[length:-5] == 'config' or _[length:-5] == 'help':
            with open(_, 'r') as f: startupConfiguration.update(loads(f.read()))

        else:
            with open(_, 'r') as f: startupConfiguration['session'].update(loads(f.read()))

def loadContent() -> any:
    global startupConfiguration
    from glob import glob; from json import loads; from auth import read, write

    for _ in glob(os.path.join(startupConfiguration['root'], startupConfiguration['source'], '*.json')):
        file = os.path.join(startupConfiguration['root'], startupConfiguration['varPath'], 'frameworks', f'{os.path.basename(_)[:-5]}.sfx') #"".join(random.choice(string.digits) for i in range(25))
        #while file in glob(os.path.join(startupConfiguration['root'], startupConfiguration['varPath'], 'src/*.json')):
        #    file = os.path.join(startupConfiguration['root'], startupConfiguration['varPath'], 'src', f'{"".join(random.choice(string.digits) for i in range(25))}.sfx')
        with open(_, 'r') as f: write(f.read(), file)

    root:str = startupConfiguration['root']; varPath:str = startupConfiguration['varPath']
    

    for dir in startupConfiguration['content']:
        for _ in glob(f'{os.path.join(root, varPath, dir)}/*.sfx'):
            with open(os.path.join(_), 'r') as f: startupConfiguration.update(loads(bytes.fromhex(read(f.read())).replace(b'\n', b'').replace(b' ', b'').replace(b'!', b' ')))

def preparePath() -> any:
    root:str = startupConfiguration['root']; varPath:str = startupConfiguration['varPath']

    for _ in startupConfiguration['required']:
        path = os.path.join(root, _)
        if not path in sys.path: sys.path.append(path)

preparePath(); import ttk

def createApp(*args, **kwargs) -> tkinter.Tk:
    global startupConfiguration, splash, progress
    #from app import portal
    from glob import glob
    from json import loads
    from auth import read

    #report('Engine waking...')
    # load modules to startupConfiguration
    modules = glob(os.path.join(startupConfiguration['root'], startupConfiguration['varPath'], 'modules/*.sfx'))
    length = len(modules)
    progress_chunk_size = 100; count = 1
    if length: progress_chunk_size = round(100 / length)

    #pause()
    
    for _ in modules:
        with open(_, 'r') as f: o = loads(bytes.fromhex(read(f.read())).replace(b'\n', b'').replace(b' ', b'').replace(b'!', b' ')); startupConfiguration.update(o)
        #splash.after(10, None) # animate progress
        #progress['value'] = progress_chunk_size * count
        #splash.update_idletasks() # update graphics
        count += 1

    for key, val in startupConfiguration.items():
        if isinstance(val, dict) and 'methodname' in val:
            methodname = val['methodname']
            foo = val['method']

            # declare function
            exec(f"""def {methodname}(*args, **kwargs):
                try:exec("{foo}")
                finally:pass""")

            if not val['methodname'] in dir(sys.modules['__main__']): setattr(sys.modules['__main__'], val['methodname'], locals()[methodname])

    splash = tkinter.Tk()
    image = tkinter.PhotoImage(file = f"{startupConfiguration['root']}/{startupConfiguration['varPath']}/assets/splash.gif")
    splash.winfo_toplevel().iconphoto(False, tkinter.PhotoImage(file = f"{startupConfiguration['root']}/{startupConfiguration['varPath']}/assets/iris.png"))

    splash.title('Start Page')
    min_width = 600; min_height = 400
    splash.geometry('%sx%s+0+0' % (min_width, min_height))
    splash.resizable(0, 0)
    splash.overrideredirect(1) #Remove border
    handle = tkinter.Label( splash, image = image) 
    handle.place(x = 0, y = 0)
    #button = tkinter.Button(splash, text ='Launch', command = start)
    #button.pack()
    #progress = ttk.Progressbar(splash, orient = tkinter.HORIZONTAL, length = 900, mode = 'determinate')
    #progress.pack(pady = 10, side='bottom')
    splash.wm_attributes('-topmost', True)
    splash.protocol('WM_DELETE_WINDOW', closing)
    center_tk_window.center(splash, splash)

    def start():
        global app
        app = tkinter.Tk()
        app.wm_attributes("-disabled", True)
        app.title('iV Pro')
        min_width = 1280; min_height = 720
        app.geometry('%sx%s+0+0' % (min_width, min_height))
        app.minsize(min_width, min_height)
        app.maxsize(app.winfo_screenwidth(), app.winfo_screenheight())
        app.state('zoomed')
        center_tk_window.center(app, app)
        #app.winfo_toplevel().iconphoto(False, PhotoImage(file = f"{cache['root']}/{cache['var_path']}/media/iris.png"))
        root = ttk.Frame(app); setattr(sys.modules['__main__'], 'root', root); getattr(sys.modules['__main__'], 'root').pack(fill='both', expand=1)
        menuBar = tkinter.Menu(app)

        for o in startupConfiguration['menuStrip']['menus']:
            head = tkinter.Menu(menuBar, tearoff=0)
            
            for i in o['items']:
                if i['has_sub']:
                    sub = tkinter.Menu(head, tearoff=0)
                    for _ in i['subs']:
                        if _['type'] == 'seperator': sub.add_separator()
                        else:
                            command = getattr(sys.modules['__main__'], _['command']) if _['command'] in dir(sys.modules['__main__']) else stub
                            sub.add_command(label=_['text'], command=command) # symbolic
                    head.add_cascade(label=i['text'], menu=sub)
                else:
                    if i['type'] == 'seperator': sub.add_separator()
                    else:
                        command = getattr(sys.modules['__main__'], i['command']) if i['command'] in dir(sys.modules['__main__']) else stub
                        head.add_command(label=i['text'], command=command) # symbolic

                menuBar.add_cascade(label=o['text'], menu=head)

        app.config(menu=menuBar)

        statusbar = tkinter.Label(app, text=startupConfiguration['statusBar']['text'], bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W, borderwidth='0')
        statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        statusbar.configure()

        level_1 = []
        level_2 = []
        level_3 = []
        level_4 = []
        level_5 = []
        level_6 = []
        level_7 = []
        level_8 = []
        level_9 = []
        names_1 = []
        names_2 = []
        names_3 = []
        names_4 = []
        names_5 = []
        names_6 = []
        names_7 = []
        names_8 = []
        names_9 = []
        
        for key, val in startupConfiguration.items():
            if isinstance(val, dict) and 'constructor' in val and val['active']:
                if key[0] == 'i': level_9.append(key)
                elif key[0] == 'h': level_8.append(key)
                elif key[0] == 'g': level_7.append(key)
                elif key[0] == 'f': level_6.append(key)
                elif key[0] == 'e': level_5.append(key)
                elif key[0] == 'd': level_4.append(key)
                elif key[0] == 'c': level_3.append(key)
                elif key[0] == 'b': level_2.append(key)
                elif key[0] == 'a': level_1.append(key)

        for key in level_1:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_2:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_3:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_4:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_5:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_6:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_7:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_8:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_9:
            if 'pre' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['pre']: exec(_)

        for key in level_1:
            if not key in names_1:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)
                
                if o: names_1.append(key)
                else: o = None

        for key in level_2:
            if not key in names_2:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)

                if o: names_2.append(key)
                else: o = None

        for key in level_3:
            if not key in names_3:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)
                
                if o: names_3.append(key)
                else: o = None

        for key in level_4:
            if not key in names_4:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)
                
                if o: names_4.append(key)
                else: o = None

        for key in level_5:
            if not key in names_5:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)
                
                if o: names_5.append(key)
                else: o = None

        for key in level_6:
            if not key in names_6:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)
                
                if o: names_6.append(key)
                else: o = None

        for key in level_7:
            if not key in names_7:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)
                
                if o: names_7.append(key)
                else: o = None

        for key in level_8:
            if not key in names_8:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)
                
                if o: names_8.append(key)
                else: o = None

        for key in level_9:
            if not key in names_9:
                o:object = None
                constructor = startupConfiguration[key]['constructor']
                
                for _ in constructor:
                    if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                                
                module = tkinter if startupConfiguration[key]['type'][0] == '1' else ttk; typ = startupConfiguration[key]['type'][1:]
                o = getattr(module, typ)(getattr(sys.modules['__main__'], startupConfiguration[key]['parent']), **constructor) # create object
                setattr(sys.modules['__main__'], key, o)
                
                if o: names_9.append(key)
                else: o = None

        for key in level_9:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)
                    
                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        for key in level_8:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)
                    
                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        for key in level_7:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)
                    
                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        for key in level_6:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)
                    
                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        for key in level_5:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)
                    
                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        for key in level_4:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)
                    
                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        for key in level_3:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)
                    
                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        for key in level_2:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)

                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        for key in level_1:
            properties = startupConfiguration[key]['properties']

            for prop in properties:
                if '~positional' in prop['options']:
                    positional = prop['options']['~positional']

                    for n, x in enumerate(positional):
                        if isinstance(x, str) and x[0] == '@':
                            positional[n] = getattr(sys.modules['__main__'], x[1:])

                    prop['options'].pop('~positional')
                else: positional = []

                for _, val in prop['options'].items():
                    if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules['__main__'], prop['options'][_][1:]) # resolve symbolic links
                    elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                        root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                        prop['options'][_] = getattr(getattr(sys.modules['__main__'], root), target)

                getattr(getattr(sys.modules['__main__'], key), prop['method'])(*positional, **prop['options'])

        # finalise
        for key in level_1:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

        for key in level_2:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

        for key in level_3:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

        for key in level_4:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

        for key in level_5:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

        for key in level_6:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

        for key in level_7:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

        for key in level_8:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

        for key in level_9:
            if 'init' in startupConfiguration[key]:
                for _ in startupConfiguration[key]['init']: exec(_)

    splash.after_idle(start)

    return splash

def authenticate() -> bool: return True #  implement this!

def bind():
    def exitHandler(signum, frame): raise Exit()
    signal.signal(signal.SIGINT, exitHandler)

def report(message, *args, **kwargs) -> any:
    from datetime import datetime
    with open(os.path.join(startupConfiguration['root'], startupConfiguration['logFile']), 'a') as f: f.write(f'[{datetime.now()}]: {message}\n')

def shutdown(message:str=None, *args, **kwargs) -> any:
    if message: report(message) 
    else: report('Session ended')
    os.system('cls')
    sys.exit(1)

def closing():
    global splash, app
    if app: app.wm_attributes("-disabled", False)
    splash.destroy()
    #Client.running = False

def __init__(externalReference:bool=False):
    if externalReference:
        # partial initialisation
        loadConfigs()
        loadContent()
        
    else:
        # full initialisation
        bind()
        preparePath()
        authenticate()
        loadConfigs()
        loadContent()
    report('Session started')

def getOption() -> int:
    try: opts, args = getopt.getopt(sys.argv[1:], 'hp', ['help', 'prompt'])
    except getopt.GetoptError: raise OptionError()

    if len(opts):
        for o, a in opts:
            if o in ('-h', '--help'): return 1
            elif o in ('-t', '--terminal'): return 2
            else: raise OptionError()
    else: return 0

def deploy(*args, **kwargs) -> any:
    __init__()

    option = getOption()

    if option == 1:
        print()
        for _ in startupConfiguration['help']: print(_)
        sys.exit(1)
    
    elif option == 2:
        os.system('cls')
        #from app import Prompt
        #while(): Prompt.execute(input('> '))
    
    else: os.system('cls'); createApp().mainloop(); os.system('cls')

# entry point
try:
    if __name__ == '__main__': deploy()
    else: __init__(True) # for external imports in other modules

except Exit as e: shutdown()
except AuthenticationError as e: shutdown('Authentication failed')
except OptionError as e: shutdown('Unknown option')