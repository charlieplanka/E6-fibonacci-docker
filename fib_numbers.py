def get_fibo_num(k):
    fibo_cur, fibo_next = 0, 1
    for _ in range(k-1):
        fibo_cur, fibo_next = fibo_next, fibo_cur + fibo_next
    return fibo_cur
