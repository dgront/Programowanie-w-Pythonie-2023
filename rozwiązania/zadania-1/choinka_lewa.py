N = 5
for i in range(N):
    for j in range(N - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print('#', end="")
    print()