def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("[Consumer] Consumer %s"% n)

def produce(c):
    c.send(None)
    n = 0
    while n < 7:
        n = n + 1
        print('[PRODUCE] Producing %s'% n)
        r = c.send(n)
        print('[PRODUCER] Consumer %s'% r)
    c.close()

c = consumer()
produce(c)