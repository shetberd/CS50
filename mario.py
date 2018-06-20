from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height >= 0 and height <= 23:
        break

spaces = height - 1
bricks = 2

for i in range(height):
    for k in range(spaces):
        print(" ", end="")

    for o in range(bricks):
        print("#", end="")

    print("")
    spaces -= 1
    bricks += 1
