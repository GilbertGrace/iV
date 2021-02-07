''' Graphical User Interface '''

import tkinter, ttk, sys
from ttkthemes import ThemedStyle

menubar = None
filemenu = None
viewmenu = None
editmenu = None
go = None
build = None
select = None
media = None
helpmenu = None
window = None
banner = None
btn1 = None
btn2 = None
btn3 = None
btn4 = None
btn5 = None
btn6 = None
btn7 = None
btn8 = None
btn9 = None
btn10 = None
btn11 = None
style = None
base = None
viewport = None
left = None
tabs =None
preview = None
geometry = None
_signal = None
properties = None
stack = None
frame = None
right = None
controls = None
play = None
_next = None
prev = None
jumpBack = None
jumpNext = None
project = None
sequence = None
_object = None
script = None
mesh = None
texture = None
device = None
_file = None
macro = None
resources = None
debug = None
library = None
transfer = None
plugin = None
statusbar = None
progress = None
m = None

def draw(cache) -> None:
    ''' UI builder '''
    from app import pause
    done:bool = False
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
    
    for key, val in cache.items():
        if isinstance(val, dict) and 'constructor' in val:
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
        if not key in names_1:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)
            
            if o: names_1.append(key)
            else: o = None

    for key in level_2:
        if not key in names_2:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)

            if o: names_2.append(key)
            else: o = None

    for key in level_3:
        if not key in names_3:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)
            
            if o: names_3.append(key)
            else: o = None

    for key in level_4:
        if not key in names_4:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)
            
            if o: names_4.append(key)
            else: o = None

    for key in level_5:
        if not key in names_5:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)
            
            if o: names_5.append(key)
            else: o = None

    for key in level_6:
        if not key in names_6:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)
            
            if o: names_6.append(key)
            else: o = None

    for key in level_7:
        if not key in names_7:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)
            
            if o: names_7.append(key)
            else: o = None

    for key in level_8:
        if not key in names_8:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)
            
            if o: names_8.append(key)
            else: o = None

    for key in level_9:
        if not key in names_9:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules[__name__], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules[__name__], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules[__name__], key, o)
            
            if o: names_9.append(key)
            else: o = None

    for key in level_9:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
                
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise

    for key in level_8:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
                
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise

    for key in level_7:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
                
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise

    for key in level_6:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
                
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise

    for key in level_5:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
                
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise

    for key in level_4:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
                
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise

    for key in level_3:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
                
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise

    for key in level_2:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
                
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise

    for key in level_1:
        properties = cache[key]['properties']
        positional = []

        for prop in properties:
            if '~positional' in prop['options']: positional = [getattr(sys.modules[__name__], i[1:]) for i in prop['options']['~positional'] if i[0] == '@']; prop['options'].pop('~positional')

            for _, val in prop['options'].items():
                if isinstance(prop['options'][_], str) and prop['options'][_][0] == '@': prop['options'][_] = getattr(sys.modules[__name__], prop['options'][_][1:]) # resolve symbolic links
                elif isinstance(prop['options'][_], str) and prop['options'][_][0] == '!': # nested // add more levels of recursion
                    root = val[1:].split('!')[0]; target = val[1:].split('!')[1]
                    prop['options'][_] = getattr(getattr(sys.modules[__name__], root), target)
        for prop in properties: getattr(getattr(sys.modules[__name__], key), prop['method'])(*positional, **prop['options']) # implement property
        if 'init' in cache[key]: exec(*cache[key]['init']) # finalise
    #pause()

class Editor(tkinter.Tk):
    def __init__(self, cache, engine) -> None:
        from app import closing
        global menubar, filemenu, viewmenu, editmenu, go, build, select, media, helpmenu, window, banner, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11
        global style, base, viewport, left, tabs, preview, geometry, _signal, properties, stack, frame, right, controls, play, _next, prev, jumpBack, jumpNext
        global project, sequence, _object, script, mesh, texture, device, _file, macro, resources, debug, library, transfer, plugin, statusbar, progress, m
        tkinter.Tk.__init__(self)
        
        menubar = tkinter.Menu(self)
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New File')
        filemenu.add_command(label='New Project')
        filemenu.add_command(label='New Window')
        filemenu.add_command(label='New Terminal')
        filemenu.add_separator()
        filemenu.add_command(label='Open File')
        filemenu.add_command(label='Open Recent')
        filemenu.add_command(label='Open Project')
        filemenu.add_command(label='Open Folder')
        filemenu.add_separator()
        filemenu.add_command(label='Save')
        filemenu.add_command(label='Save As')
        filemenu.add_command(label='Save All')
        filemenu.add_separator()
        filemenu.add_command(label='Close')
        filemenu.add_command(label='Close All')
        filemenu.add_command(label='Close Folder')
        filemenu.add_command(label='Close Window')
        filemenu.add_separator()
        filemenu.add_command(label='Exit')
        menubar.add_cascade(label='File', menu=filemenu)

        viewmenu = tkinter.Menu(menubar, tearoff=0)
        viewmenu.add_command(label='New File')
        viewmenu.add_command(label='New Project')
        viewmenu.add_command(label='New Window')
        viewmenu.add_command(label='New Terminal')
        viewmenu.add_separator()
        viewmenu.add_command(label='Open File')
        viewmenu.add_command(label='Open Recent')
        viewmenu.add_command(label='Open Project')
        viewmenu.add_command(label='Open Folder')
        viewmenu.add_separator()
        viewmenu.add_command(label='Save')
        viewmenu.add_command(label='Save As')
        viewmenu.add_command(label='Save All')
        viewmenu.add_separator()
        viewmenu.add_command(label='Close')
        viewmenu.add_command(label='Close All')
        viewmenu.add_command(label='Close Folder')
        viewmenu.add_command(label='Close Window')
        viewmenu.add_separator()
        viewmenu.add_command(label='Exit')
        menubar.add_cascade(label='View', menu=viewmenu)

        editmenu = tkinter.Menu(menubar, tearoff=0)
        editmenu.add_command(label='New File')
        editmenu.add_command(label='New Project')
        editmenu.add_command(label='New Window')
        editmenu.add_command(label='New Terminal')
        editmenu.add_separator()
        editmenu.add_command(label='Open File')
        editmenu.add_command(label='Open Recent')
        editmenu.add_command(label='Open Project')
        editmenu.add_command(label='Open Folder')
        editmenu.add_separator()
        editmenu.add_command(label='Save')
        editmenu.add_command(label='Save As')
        editmenu.add_command(label='Save All')
        editmenu.add_separator()
        editmenu.add_command(label='Close')
        editmenu.add_command(label='Close All')
        editmenu.add_command(label='Close Folder')
        editmenu.add_command(label='Close Window')
        editmenu.add_separator()
        editmenu.add_command(label='Exit')
        menubar.add_cascade(label='Edit', menu=editmenu)

        go = tkinter.Menu(menubar, tearoff=0)
        go.add_command(label='New File')
        go.add_command(label='New Project')
        go.add_command(label='New Window')
        go.add_command(label='New Terminal')
        go.add_separator()
        go.add_command(label='Open File')
        go.add_command(label='Open Recent')
        go.add_command(label='Open Project')
        go.add_command(label='Open Folder')
        go.add_separator()
        go.add_command(label='Save')
        go.add_command(label='Save As')
        go.add_command(label='Save All')
        go.add_separator()
        go.add_command(label='Close')
        go.add_command(label='Close All')
        go.add_command(label='Close Folder')
        go.add_command(label='Close Window')
        go.add_separator()
        go.add_command(label='Exit')
        menubar.add_cascade(label='Go', menu=go)

        build = tkinter.Menu(menubar, tearoff=0)
        build.add_command(label='New File')
        build.add_command(label='New Project')
        build.add_command(label='New Window')
        build.add_command(label='New Terminal')
        build.add_separator()
        build.add_command(label='Open File')
        build.add_command(label='Open Recent')
        build.add_command(label='Open Project')
        build.add_command(label='Open Folder')
        build.add_separator()
        build.add_command(label='Save')
        build.add_command(label='Save As')
        build.add_command(label='Save All')
        build.add_separator()
        build.add_command(label='Close')
        build.add_command(label='Close All')
        build.add_command(label='Close Folder')
        build.add_command(label='Close Window')
        build.add_separator()
        build.add_command(label='Exit')
        menubar.add_cascade(label='Build', menu=build)

        select = tkinter.Menu(menubar, tearoff=0)
        select.add_command(label='New File')
        select.add_command(label='New Project')
        select.add_command(label='New Window')
        select.add_command(label='New Terminal')
        select.add_separator()
        select.add_command(label='Open File')
        select.add_command(label='Open Recent')
        select.add_command(label='Open Project')
        select.add_command(label='Open Folder')
        select.add_separator()
        select.add_command(label='Save')
        select.add_command(label='Save As')
        select.add_command(label='Save All')
        select.add_separator()
        select.add_command(label='Close')
        select.add_command(label='Close All')
        select.add_command(label='Close Folder')
        select.add_command(label='Close Window')
        select.add_separator()
        select.add_command(label='Exit')
        menubar.add_cascade(label='Select', menu=select)
        
        tool = tkinter.Menu(menubar, tearoff=0)
        tool.add_command(label='New File')
        tool.add_command(label='New Project')
        tool.add_command(label='New Window')
        tool.add_command(label='New Terminal')
        tool.add_separator()
        tool.add_command(label='Open File')
        tool.add_command(label='Open Recent')
        tool.add_command(label='Open Project')
        tool.add_command(label='Open Folder')
        tool.add_separator()
        tool.add_command(label='Save')
        tool.add_command(label='Save As')
        tool.add_command(label='Save All')
        tool.add_separator()
        tool.add_command(label='Close')
        tool.add_command(label='Close All')
        tool.add_command(label='Close Folder')
        tool.add_command(label='Close Window')
        tool.add_separator()
        tool.add_command(label='Exit')
        menubar.add_cascade(label='Tool', menu=tool)

        media = tkinter.Menu(menubar, tearoff=0)
        media.add_command(label='New File')
        media.add_command(label='New Project')
        media.add_command(label='New Window')
        media.add_command(label='New Terminal')
        media.add_separator()
        media.add_command(label='Open File')
        media.add_command(label='Open Recent')
        media.add_command(label='Open Project')
        media.add_command(label='Open Folder')
        media.add_separator()
        media.add_command(label='Save')
        media.add_command(label='Save As')
        media.add_command(label='Save All')
        media.add_separator()
        media.add_command(label='Close')
        media.add_command(label='Close All')
        media.add_command(label='Close Folder')
        media.add_command(label='Close Window')
        media.add_separator()
        media.add_command(label='Exit')
        menubar.add_cascade(label='Media', menu=media)

        window = tkinter.Menu(menubar, tearoff=0)
        window.add_command(label='New File')
        window.add_command(label='New Project')
        window.add_command(label='New Window')
        window.add_command(label='New Terminal')
        window.add_separator()
        window.add_command(label='Open File')
        window.add_command(label='Open Recent')
        window.add_command(label='Open Project')
        window.add_command(label='Open Folder')
        window.add_separator()
        window.add_command(label='Save')
        window.add_command(label='Save As')
        window.add_command(label='Save All')
        window.add_separator()
        window.add_command(label='Close')
        window.add_command(label='Close All')
        window.add_command(label='Close Folder')
        window.add_command(label='Close Window')
        window.add_separator()
        window.add_command(label='Exit')
        menubar.add_cascade(label='Window', menu=window)

        helpmenu = tkinter.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='New File')
        helpmenu.add_command(label='New Project')
        helpmenu.add_command(label='New Window')
        helpmenu.add_command(label='New Terminal')
        helpmenu.add_separator()
        helpmenu.add_command(label='Open File')
        helpmenu.add_command(label='Open Recent')
        helpmenu.add_command(label='Open Project')
        helpmenu.add_command(label='Open Folder')
        helpmenu.add_separator()
        helpmenu.add_command(label='Save')
        helpmenu.add_command(label='Save As')
        helpmenu.add_command(label='Save All')
        helpmenu.add_separator()
        helpmenu.add_command(label='Close')
        helpmenu.add_command(label='Close All')
        helpmenu.add_command(label='Close Folder')
        helpmenu.add_command(label='Close Window')
        helpmenu.add_separator()
        helpmenu.add_command(label='Exit')
        menubar.add_cascade(label='Help', menu=helpmenu)
        self.config(menu=menubar)

        # buttons`
        banner = tkinter.Frame(self)
        banner.pack(side='top', fill='x', expand=0)
        banner.configure(background='gray30')

        btn1 = tkinter.Button(banner, text='Keyframe', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        btn1.pack(side='left', fill='x', padx=2)

        btn2 = tkinter.Button(banner, text='Render', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        btn2.pack(side='left', fill='x', padx=2)

        btn4 = tkinter.Button(banner, text='Run', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        btn4.pack(side='left', fill='x', padx=2)

        btn5 = tkinter.Button(banner, text='Add', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        btn5.pack(side='left', fill='x', padx=2)

        btn9 = tkinter.Button(banner, text='Snapshot', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        btn9.pack(side='left', fill='x', padx=2)

        btn10 = tkinter.Button(banner, text='Import', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        btn10.pack(side='left', fill='x', padx=2)

        btn11 = tkinter.Button(banner, text='Export', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        btn11.pack(side='left', fill='x', padx=2)

        # command prompt
        '''textbox = tkinter.Entry(banner, bd=5, width=200)
        textbox.configure(state='normal')
        textbox.pack(side='right', fill='x', padx=2) '''

        style = ThemedStyle(self)
        style.set_theme('equilux')
        style.configure('red.Horizontal.TProgressbar', foreground='red', background='red')
        #style.layout('TNotebook.Tab', []) # turn off tabs

        base = tkinter.Frame(self)
        base.configure(background='black')
        base.pack(fill='both', expand=1)
        
        viewport = tkinter.Frame(base, borderwidth='0')
        viewport.configure(background='black')
        viewport.pack(side='top', fill='both', expand=1)
        
        left = tkinter.Frame(viewport, borderwidth='0')
        left.configure(background='gray30')
        left.pack(side='left', fill='both', expand=1)

        tabs = ttk.Notebook(left)

        preview = ttk.Frame(tabs)
        tabs.add(preview, text ='Preview')

        geometry = ttk.Frame(tabs)
        tabs.add(geometry, text ='Geometry')

        _signal = ttk.Frame(tabs)
        tabs.add(_signal, text ='Signal')

        properties = ttk.Frame(tabs)
        tabs.add(properties, text ='Properties')

        stack = ttk.Frame(tabs)
        tabs.add(stack, text ='Call Stack')

        frame = ttk.Frame(tabs)
        tabs.add(frame, text ='Frame')

        library = ttk.Frame(tabs)
        tabs.add(library, text ='Library')

        tabs.pack(expand = 1, fill ='both', side='top')
        
        right = tkinter.Frame(viewport, borderwidth='0')
        right.configure(background='black')
        right.pack(side='right', fill='both', expand=1)
        
        controls = tkinter.Frame(right, borderwidth='1', height=25)
        controls.configure(background='gray30')
        controls.pack(side='bottom', fill='x', expand=0)

        play = tkinter.Button(controls, text='Play', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        play.pack(side='left', fill='x', padx=2)

        _next = tkinter.Button(controls, text='Next', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        _next.pack(side='left', fill='x', padx=2)

        prev = tkinter.Button(controls, text='Previous', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        prev.pack(side='left', fill='x', padx=2)

        jumpBack = tkinter.Button(controls, text='Jump Back', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        jumpBack.pack(side='left', fill='x', padx=2)

        jumpNext = tkinter.Button(controls, text='Jump Previous', pady=5, padx=5, bg='gray30', fg='#bfbfbf', borderwidth='0')
        jumpNext.pack(side='left', fill='x', padx=2)

        tabControl = ttk.Notebook(base)

        # project
        project = ttk.Frame(tabControl)
        tabControl.add(project, text ='Project')

        # sequence
        sequence = ttk.Frame(tabControl)
        tabControl.add(sequence, text ='Sequence')

        # object
        _object = ttk.Frame(tabControl)
        tabControl.add(_object, text ='Object')

        # script
        script = ttk.Frame(tabControl)
        tabControl.add(script, text ='Script')

        # mesh
        mesh = ttk.Frame(tabControl)
        tabControl.add(mesh, text ='Mesh')

        # texture
        texture = ttk.Frame(tabControl)
        tabControl.add(texture, text ='Texture')

        # device
        device = ttk.Frame(tabControl)
        tabControl.add(device, text ='Device')

        # file
        _file = ttk.Frame(tabControl)
        tabControl.add(_file, text ='File')

        # macro
        macro = ttk.Frame(tabControl)
        tabControl.add(macro, text ='Macro')

        # resources
        resources = ttk.Frame(tabControl)
        tabControl.add(resources, text ='Resources')

        # debug
        debug = ttk.Frame(tabControl)
        tabControl.add(debug, text ='Debug')

        # transfer
        transfer = ttk.Frame(tabControl)
        tabControl.add(transfer, text ='Transfer')

        # plugin
        plugin = ttk.Frame(tabControl)
        tabControl.add(plugin, text ='Plugin')

        tabControl.pack(expand = 1, fill ='both', side='bottom')

        statusbar = tkinter.Label(self, text=cache['copyright'], bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W, borderwidth='0', fg='#bfbfbf')
        statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        statusbar.configure(background='gray30')
        #progress = ttk.Progressbar(statusbar, style="red.Horizontal.TProgressbar", orient = tkinter.HORIZONTAL, length = 50, mode = 'determinate')
        #progress.pack(side='right', pady=1)

        m = tkinter.Menu(self, tearoff = 0) 
        m.add_command(label='New File')
        m.add_command(label='New Project')
        m.add_command(label='New Window')
        m.add_command(label='New Terminal')
        m.add_separator()
        m.add_command(label='Open File')
        m.add_command(label='Open Recent')
        m.add_command(label='Open Project')
        m.add_command(label='Open Folder')
        m.add_separator()
        m.add_command(label='Save')
        m.add_command(label='Save As')
        m.add_command(label='Save All')
        m.add_separator()
        m.add_command(label='Close')
        m.add_command(label='Close All')
        m.add_command(label='Close Folder')
        m.add_command(label='Close Window')
        m.add_separator()
        m.add_command(label='Exit')
        m.add_command(label ='Rename') 
        
        def do_popup(event): 
            try: 
                m.tk_popup(event.x_root, event.y_root) 
            finally: 
                m.grab_release() 
        
        self.bind('<Button-3>', do_popup)

        draw(cache)