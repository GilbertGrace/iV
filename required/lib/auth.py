import binascii

def read(source:str) -> str: return source

def write(source:str, target:str):
    ''' Serialise '''
    with open(target, 'wb') as f: f.write(binascii.hexlify(bytes(source, 'utf-8')))