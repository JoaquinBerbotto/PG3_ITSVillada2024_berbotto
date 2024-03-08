def num_step(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if abs(int(num_str[i]) - int(num_str[i + 1])) != 1:
            return False
    return True

num = int(input("Ingrese un número: "))
print(num_step(num))