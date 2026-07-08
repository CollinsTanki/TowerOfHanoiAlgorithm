def n_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        n_hanoi(n-1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        n_hanoi(n-1, auxiliary, target, source)
        