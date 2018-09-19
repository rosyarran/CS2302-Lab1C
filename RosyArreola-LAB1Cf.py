import itertools
import hashlib

# Transform string into hashed password
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def generateString(items, min, max, k, lines):
    if(k > max):
        return
    else:
        perms = list(itertools.product(items, repeat=k))
        for j in perms:
            newStr = "".join(j)
            if len(newStr) >= min:
                comparePass(lines, newStr, 0)
        generateString(items, min, max, k+1, lines)

# Compare recursively hashed passwords
def comparePass(lines, str, i):
    if i >= len(lines):
        return
    # Split each line by each comma and save in temporary array length 3
    temp = lines[i].split(',')
    # Transform salt value (temp[1]) and password into hashed password using sha256
    codedPass = hash_with_sha256(str+temp[1])
    # Remove \n from split item to avoid errors
    hashedPass = temp[2].rstrip("\n")
    # If file ends return isFound
    if(codedPass == hashedPass):
        print("Password " + str + " found for " + temp[0])
    comparePass(lines, str, i+1)

def main(items, min, max):

    # Read file and separate each line into an array
    with open('password_file.txt', 'r') as textFile:
        lines = textFile.readlines()

    k = 0
    generateString(items, min, max, k, lines)

min = 3
max = 7
items = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
main(items, min, max)