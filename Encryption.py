def encrypt(key, filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(filename, "wb")
    file.write(data)
    file.close()


def decrypt(key, filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    file = open(filename, "wb")
    file.write(data)
    file.close()


choice = input("Press 1 to encrypt your file or 2 to decrypt it with a known key. ")
key = int(input("Give a key between 1-255. "))
filename = input("Enter the file location you want to encrypt. ")
if choice == "1":
    encrypt(key, filename)
else:
    decrypt(key, filename)
