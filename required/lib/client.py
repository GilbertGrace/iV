import sys, glob, os, json

class Client:
    running:bool = False
    history:list = []

    @staticmethod
    def execute(cache, *args, **kwargs) -> dict:
        from app import init, Exit, write, report

        o = input('> ').rstrip().split('.'); Client.history.append(o)    

        if o[0] == 'clear':
            if len(o) > 1 and o[1] == 'history': Client.history.clear()
            else: os.system('cls')
        
        elif o[0] == 'history':
            for _ in Client.history[:-1]: print(''.join(_))
        
        elif o[0] == 'help':
            print(cache['copyright'])
            for _ in cache['help']: print(_)
        
        elif o[0] == 'run':
            from planera import PlaneraLife as root; from app import pause
            os.system('cls')
            print('installing...'); from time import sleep; sleep(1) # this is a vm that runs in ram
            
            k = dict()

            for pair in o:
                if o.index(pair) > 0: k.update({pair.split('=')[0]:pair.split('=')[1]})
            
            cursor = root.__boot(cache, True, **k)
            #pause()
            while (cursor.ready): cursor.next() # thread
            del(cursor)

        elif o[0] == 'exit': os.system('cls'); report('Session ended.'); sys.exit(1)

        else: print('syntax error')