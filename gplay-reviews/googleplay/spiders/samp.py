def func(k):
    a = []
    for i in range(k,k+10):
        a.append({i:str(i)})
        # print(a)
    return a

print func(2)