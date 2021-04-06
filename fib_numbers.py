from pymemcache.client import base

client = base.Client(("localhost", 11211))


def get_fibo_num(k):
    fibo = client.get(str(k))
    if fibo is None:
        fibo, fibo_next = 0, 1
        for _ in range(k-1):
            fibo, fibo_next = fibo_next, fibo + fibo_next
        client.set(str(k), fibo)
    return int(fibo)


# print(get_fibo_num(1000))
