def palind(pal):
    return pal == pal[::-1]

pal = input(str("Decime tu palabra: "))

print(palind(pal))