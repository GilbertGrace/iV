''' Core services '''

import sys, glob, os, json

class Engine:
    def __init__(self, progress, splash, cache, *args, **kwargs) -> None:
        from app import report, read, pause
        #report('Engine waking...')
        # load modules to cache
        modules = glob.glob(os.path.join(cache['root'], cache['var_path'], 'modules/*.sfx'))
        length = len(modules)
        progress_chunk_size = 100; count = 1
        if length: progress_chunk_size = round(100 / length)

        for _ in modules:
            with open(_, 'r') as f: o = json.loads(bytes.fromhex(read(f.read())).replace(b'\n', b'').replace(b' ', b'').replace(b'!', b' ')); cache.update(o)
            splash.after(10, None) # animate progress
            #progress['value'] = progress_chunk_size * count
            splash.update_idletasks() # update graphics
            count += 1

        for key, val in cache.items():
            if isinstance(val, dict) and 'methodname' in val:
                # declare global functions
                def __foo__(*args, **kwargs) -> object: exec(val['method'])
                if not val['methodname'] in dir(sys.modules['__main__']): setattr(sys.modules['__main__'], val['methodname'], __foo__)

        #progress['value'] = 100 # done
        #report('Engine awake')