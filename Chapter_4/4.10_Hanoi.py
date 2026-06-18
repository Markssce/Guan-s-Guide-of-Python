# Hanoi Tower

def hanoi(n, a, b, c):
    if n == 1:
        print(f"Plate 1:{a} -> {c}")
        return 1

    else:
        # NO.n-1 Plate a -> b (by c) 
        t_1 = hanoi(n - 1, a, c, b)
        print(f"Plate{n}: {a} -> {c}")
        # Biggest Plate move directly
        t_2 = hanoi(n - 1, b, a, c)
        return t_1 + t_2 + 1

print(hanoi(10, "A", "B", "C"))