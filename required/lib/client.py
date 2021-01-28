class Client:
    running:bool

    def __init__(self) -> None:
        Client.running = True

    def __call__(self, *args:list, **kwds:dict) -> dict:
        o = input('> ').rstrip().split(':')