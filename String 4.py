
def char_swap(a,b):
    
    c=b[:2]+a[2:]
    d=a[:2]+b[2:]
    return c+' '+d

print(char_swap('abc','xyz'))
