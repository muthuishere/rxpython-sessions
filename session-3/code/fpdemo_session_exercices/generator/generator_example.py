

def multiples_of_248_till(num):
    for val in range(1,num):
        yield (val * 248)


def multiples_of_248_till_v0(num):
    results=[]
    for val in range(1,num):
        results.append(val * 248)
    return results