''' Graphical User Interface '''

import tkinter, ttk, sys

class Editor(tkinter.Tk):
    def __init__(self, cache) -> None:
        tkinter.Tk.__init__(self)
        root = ttk.Frame(self); setattr(sys.modules['__main__'], 'root', root); getattr(sys.modules['__main__'], 'root').pack(fill='both', expand=1)
        menuBar = tkinter.Menu(self)

        for o in cache['menuStrip']['menus']:
            head = tkinter.Menu(menuBar, tearoff=0)
            
            for i in o['items']:
                if i['has_sub']:
                    sub = tkinter.Menu(head, tearoff=0)
                    for _ in i['subs']:
                        if _['type'] == 'seperator': sub.add_separator()
                        else: sub.add_command(label=_['text'], command=lambda x: 0) # symbolic
                    head.add_cascade(label=i['text'], menu=sub)
                else:
                    if i['type'] == 'seperator': sub.add_separator()
                    else: sub.add_command(label=i['text'], command=lambda x: 0)

                menuBar.add_cascade(label=o['text'], menu=head)

        self.config(menu=menuBar)

        statusbar = tkinter.Label(self, text=cache['statusBar']['text'], bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W, borderwidth='0')
        statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        statusbar.configure()
        draw(cache)

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
        if not key in names_1:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)
            
            if o: names_1.append(key)
            else: o = None

    for key in level_2:
        if not key in names_2:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)

            if o: names_2.append(key)
            else: o = None

    for key in level_3:
        if not key in names_3:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)
            
            if o: names_3.append(key)
            else: o = None

    for key in level_4:
        if not key in names_4:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)
            
            if o: names_4.append(key)
            else: o = None

    for key in level_5:
        if not key in names_5:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)
            
            if o: names_5.append(key)
            else: o = None

    for key in level_6:
        if not key in names_6:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)
            
            if o: names_6.append(key)
            else: o = None

    for key in level_7:
        if not key in names_7:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)
            
            if o: names_7.append(key)
            else: o = None

    for key in level_8:
        if not key in names_8:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)
            
            if o: names_8.append(key)
            else: o = None

    for key in level_9:
        if not key in names_9:
            o:object = None
            constructor = cache[key]['constructor']
            
            for _ in constructor:
                if isinstance(constructor[_], str) and constructor[_][0] == '@': constructor[_] = getattr(sys.modules['__main__'], constructor[_][1:]) # resolve symbolic links
                            
            module = tkinter if cache[key]['type'][0] == '1' else ttk; typ = cache[key]['type'][1:]
            o = getattr(module, typ)(getattr(sys.modules['__main__'], cache[key]['parent']), **constructor) # create object
            setattr(sys.modules['__main__'], key, o)
            
            if o: names_9.append(key)
            else: o = None

    for key in level_9:
        properties = cache[key]['properties']

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
        properties = cache[key]['properties']

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
        properties = cache[key]['properties']

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
        properties = cache[key]['properties']

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
        properties = cache[key]['properties']

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
        properties = cache[key]['properties']

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
        properties = cache[key]['properties']

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
        properties = cache[key]['properties']

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
        properties = cache[key]['properties']

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
        if 'init' in cache[key]: exec(*cache[key]['init'])

    for key in level_2:
        if 'init' in cache[key]: exec(*cache[key]['init'])

    for key in level_3:
        if 'init' in cache[key]: exec(*cache[key]['init'])

    for key in level_4:
        if 'init' in cache[key]: exec(*cache[key]['init'])

    for key in level_5:
        if 'init' in cache[key]: exec(*cache[key]['init'])

    for key in level_6:
        if 'init' in cache[key]: exec(*cache[key]['init'])

    for key in level_7:
        if 'init' in cache[key]: exec(*cache[key]['init'])

    for key in level_8:
        if 'init' in cache[key]: exec(*cache[key]['init'])

    for key in level_9:
        if 'init' in cache[key]: exec(*cache[key]['init'])
    #pause()