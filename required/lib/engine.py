''' Core services '''

import sys, glob, os, json, tkinter

class Engine:
    def __init__(self, progress, splash, cache) -> None:
        from app import report, read, pause
        #report('Engine waking...')
        # load modules to cache
        modules = glob.glob(os.path.join(cache['root'], cache['var_path'], 'modules/*.sfx'))
        length = len(modules)
        progress_chunk_size = 100; count = 1
        if length: progress_chunk_size = round(100 / length)

        for _ in modules:
            with open(_, 'r') as f: o = json.loads(bytes.fromhex(read(f.read())).replace(b'\n', b'').replace(b' ', b'').replace(b'##', b' ')); cache.update(o)
            splash.after(10, None) # animate progress
            #progress['value'] = progress_chunk_size * count
            splash.update_idletasks() # update graphics
            count += 1

        for key, val in cache.items():
            if isinstance(val, dict) and 'methodname' in val:
                # declare global functions
                def __foo__(*args, **kwargs) -> object: exec(val['method'])
                if not val['methodname'] in dir(sys.modules[__name__]): setattr(sys.modules[__name__], val['methodname'], __foo__)

        #progress['value'] = 100 # done
        #report('Engine awake')
        #pause()
        self.preview = Preview()
        self.geometry = Geometry()
        self.signal = Signal()
        self.properties = Properties()
        self.callstack = CallStack()
        self.frame = Frame()
        self.library = Library()
        self.project = Project()
        self.sequence = Sequence()
        self._object = Object()
        self.script = Script()
        self.macro = Macro()
        self.mesh = Mesh()
        self._file = _File()
        self.resources = Resources()
        self.debug = Debug()
        self.transfer = Transfer()
        self.plugin = Plugin()

    def _file_(self, *args, **kwargs) -> None: pass
    def _view_(self, *args, **kwargs) -> None: pass
    def _edit_(self, *args, **kwargs) -> None: pass
    def _go_(self, *args, **kwargs) -> None: pass
    def _tool_(self, *args, **kwargs) -> None: pass
    def _media_(self, *args, **kwargs) -> None: pass
    def _window_(self, *args, **kwargs) -> None: pass
    def _help_(self, *args, **kwargs) -> None: pass
    def _build_(self, *args, **kwargs) -> None: pass
    def render(self) -> None: return
    def keyframe(self) -> None: return
    def add(self) -> None: return
    def snapshot(self) -> None: return
    def compile(self) -> None: return
    def _import_(self) -> None: return
    def _export_(self) -> None: return

def tabChanged(new, old, *args, **kwargs): pass

class Preview:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Geometry:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Signal:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Properties:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class CallStack:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Frame:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Library:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Project:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Sequence:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Object:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Script:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Macro:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Mesh:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class _File:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Resources:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Debug:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Transfer:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass

class Plugin:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def tabSelected(self): pass

    def windowClosed(self): pass
