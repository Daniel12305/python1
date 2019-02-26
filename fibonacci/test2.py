


def fibonacci(n, results):
    if n == 0:   
        return 0  
    elif n == 1:  
        return 1  
    else :  
        f = fibonacci(n-1, results) + fibonacci(n-2, results)
        f1 = f[:]
        results.appned(f1)


    return results