import sys, glob, os, json

class Client:
    running:bool = False
    history:list = []

    @staticmethod
    def execute(*args:list, **kwds:dict) -> dict:
        from app import show, cache, Exit, write, report
        o = input('> ').rstrip().split('!'); Client.history.append(o)
        if o[0] == 'make':
            for _ in glob.glob(os.path.join(cache['root'], cache['source'], '*.json')):
                file = os.path.join(cache['root'], cache['var_path'], 'modules', f'{os.path.basename(_)[:-5]}.sfx') #"".join(random.choice(string.digits) for i in range(25))
                while file in glob.glob(os.path.join(cache['root'], cache['var_path'], 'modules/*.json')): file = os.path.join(cache['root'], cache['var_path'], 'modules', f'{"".join(random.choice(string.digits) for i in range(25))}.sfx')
                with open(_, 'r') as f: write(f.read(), file)
        elif o[0] == 'run': show()
        elif o[0] == 'clear':
            if len(o) > 1 and o[1] == 'history': Client.history.clear()
            else: os.system('cls')
        elif o[0] == 'history':
            for _ in Client.history[:-1]: print(''.join(_))
        elif o[0] == 'help':
            print(cache['copyright'])
            for _ in cache['help']: print(_)
        elif o[0] == 'system':
            for _ in cache['help']: print(_)
        elif o[0] == 'exit': os.system('cls'); report('Session ended.'); sys.exit(1)
        else: print('syntax error')