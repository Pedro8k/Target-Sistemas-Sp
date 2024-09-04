def esta_em_fibonacci(n):
    fib = [0,1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    if n in fib:
        print("O número ", n, " está na sequência de Fibonnaci.")
        return
    print("O número ", n, " NÃO está na sequência de Fibonacci.")

esta_em_fibonacci(377)
esta_em_fibonacci(610)
esta_em_fibonacci(3)
esta_em_fibonacci(1)
esta_em_fibonacci(0)
esta_em_fibonacci(2584)
esta_em_fibonacci(2600)