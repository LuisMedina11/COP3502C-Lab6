def encoder(x):   # Luis Medina code
    x = int(x)   # Turns str into int
    a = (((x // 10000000) % 10) + 3) % 10
    b = (((x // 1000000) % 10) + 3) % 10
    c = (((x // 100000) % 10) + 3) % 10
    d = (((x // 10000) % 10) + 3) % 10
    e = (((x // 1000) % 10) + 3) % 10
    f = (((x // 100) % 10) + 3) % 10
    g = (((x // 10) % 10) + 3) % 10
    h = ((x % 10) + 3) % 10    # Fetches value and adds 3
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    e = str(e)
    f = str(f)
    g = str(g)
    h = str(h)
    addition = a + b + c + d + e + f + g + h    # Adds str together
    return addition


def decode():
    print(f'The encoded password is {y}, and the original password is {z}.')  # Prints the decode function statement
    print()


w = True
if __name__ == "__main__":
    while w is True:
        print("Menu:")
        print("1. Encode Password\n"
              "2. Decode Password\n"
              "3. Exit Decoder\n"
              "Choose an option:\n")  # Prints menu

        m = input()
        m = int(m)

        if m == 1:
            z = input("Enter an 8-digit password to encode: ")   # Runs option 1
            y = encoder(z)
            print('Encoded password: ', y)

        elif m == 2:
            decode()  # Runs the decode function when option 2 is chosen

        elif m == 3:   # Runs option 3
            print('Goodbye.')
            w = False

        else:      # Runs when no option is chosen
            print('Wrong input. Try again.')
