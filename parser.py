import string

VAR = string.ascii_lowercase
OP = ">|&"

def check(w):
    state = True
    counter = 0

    for char in w:
        if state:
           if char in VAR: state = False
           elif char in OP + ')': return False
        else:
            if char in OP: state = True
            elif char in VAR + '(': return False 
        if char == '(': counter += 1
        if char == ')': counter -= 1

    return not state and counter == 0
    

def bal(w,op):
    ln = 0
    for i in range(len(w)-1, -1,-1):
        char = w[i]
        if w == ')': ln += 1
        elif char == '(': ln -= 1
        elif char in op and ln == 0: return i
    return -1

def onp(w):
    #usuwanie zbędnych nawiasów
    while w[0] == '(' and w[-1] == ')' and check(w[1:-1]): 
        w = w[1:-1]
    
    p = bal(w, '>')
    if p >= 0 : return onp(w[:p]) + onp(w[p+1:]) + ">"
    
    p = bal(w, '|&')
    if p >= 0 : return onp(w[:p]) + onp(w[p+1:]) + w[p]
    
    return w

def value(w, arg):
    w = map(w,arg)

    

def var(w):
    return ''.join(sorted(set(w) & set(VAR)))

def map(w, arg):
    s = zip(var(w),arg)
    d = {}
    for i in s:
        d[i[0]] = i[1]
    return d

w = input()
print(var(w))
