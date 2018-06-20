from cs50 import get_string
import sys

def main():

    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("ERROR")
        exit(1)

    sys.argv[1] = int(sys.argv[1])
    #print(sys.argv[1])
    key = int(sys.argv[1])

    if key < 0:
        print("negative key value")
        exit(1)

    plainText = get_string("Plaintext: ")
    #print(plainText)

    print ("ciphertext: ", end="")
    for c in plainText:
        if c.isalpha() == False:
            print(c, end="")
        if c.isalpha() == True:
            if c.islower() == True:
                alphIndex = ((((ord(c) - 97)+ key)% 26)+ 97)
            if c.isupper() == True:
                alphIndex = ((((ord(c) - 65)+ key)% 26)+ 65)
            print(chr(alphIndex), end="")
    print("")
if __name__ == "__main__":
    main()
