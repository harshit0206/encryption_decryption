pas=input()
key = '5@%0sn6@9)sgsn438%$#8wjjdisk76238'
passw = ''

def encry(pas, key):
    global passw
    for i in range(len(pas)):
        x = ord(pas[i])
        y = ord(key[i])
        passw += chr(x + y)
    print(passw)

def decry(passw, key):
    pas = ''
    for i in range(len(passw)):
        x = ord(passw[i])
        y = ord(key[i])
        pas += chr(x - y)
    print(pas)

encry(pas, key)

decry(passw, key)
