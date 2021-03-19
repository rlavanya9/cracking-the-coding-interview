def tower_hanoi(n,start,final,middle):
    if n >= 1:
        tower_hanoi(n-1,start,middle,final)
        print_disk(start,final)
        tower_hanoi(n-1,middle,final,start)

def print_disk(start,final):
    print(f"move disk from {start} to {final}")

tower_hanoi(3,'A','B','C')