import math
x=float(input("Enter a num"))
def taylor_series_cos(x, term=10):
    cos_x=0
    for n in range(term):
        cos_x +=((-1)**n)*(x**(2*n))/math.factorial (2*n)
    return cos_x

def taylor_series_sin(x,term =10):
    sinx=0
    for n in range(term):
        sinx +=((-1)**n)*(x**(2*n+1))/math.factorial(2*n+1)
    return sinx
    
print("Taylor series cos(0.5):",taylor_series_cos(x))
print("Taylor series sin(0.5):", taylor_series_sin(x))
