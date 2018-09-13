import hashlib

# Transform string into hashed password
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

# Compare recursively hashed passwords
def comparePass(lines, str, i, isFound):
    # Split each line by each comma and save in temporary array length 3
    temp = lines[i-1].split(',')
    # Transform salt value (temp[1]) and password into hashed password using sha256
    codedPass = hash_with_sha256(str+temp[1])
    # Remove \n from split item to avoid errors
    hashedPass = temp[2].rstrip("\n")
    # If file ends return isFound
    if(i>=len(lines)):
        return isFound
    # Else compare each password and if found print User Name and make isFound True
    elif(codedPass == hashedPass):
        print("Password found for " + temp[0])
        isFound = True
    # Recursive call
    return comparePass(lines, str, i+1, isFound)

def main(str, min, max, isFound):

    # Verify that the password length is appropriate and only numbers
    if(len(str)<min or len(str)>max or not str.isdigit()):
        print("INVALID PASSWORD")
        return

    # Read file and separate each line into an array
    with open('rosys_passwords.txt', 'r') as textFile:
        lines = textFile.readlines()

    i = 1
    isFound = comparePass(lines, str, i, isFound)
    if not isFound:
        print("Password Not Found")

min = 3
max = 7
found = False
str = '123'
main(str, min, max, found)