import hashlib
import collections


def getUID():
    """this function gets UID value from txt file"""
    with open("UID.txt", "r") as fp:
        new_joined = []
        lines = fp.readlines()
        for i in lines:
            stringhash = str(i).rstrip("\n")
            new_joined.append(stringhash)
        return new_joined


# joined = zip([1,2,3], [a, b, c])
# return string(x) + str(y) for x,y in joined
def getPass():
    """this function gets password value from txt file"""
    with open("Password.txt", "r") as fp:
        new_joined = []
        lines = fp.readlines()
        for i in lines:
            stringhash = str(i).rstrip("\n")
            new_joined.append(stringhash)
        return new_joined


def getSalt():
    """this function gets salt value from txt file"""
    with open("Salt.txt", "r") as fp:
        new_joined = []
        lines = fp.readlines()
        for i in lines:
            stringhash = str(i).rstrip("\n")
            new_joined.append(stringhash)
        return new_joined


def getHash():
    """this function gets the hashed passwords from the txt file"""
    with open("Hash.txt", "r") as fp:
        new_joined = []
        lines = fp.readlines()
        for i in lines:
            stringhash = str(i).rstrip("\n")
            new_joined.append(stringhash)
        return new_joined


def addSalt():
    """this is the function that adds salt to the password and turns it into list of strings"""
    joined = list(zip(getPass(), getSalt()))
    new_joined = []
    for i in joined:
        str(i)
        x = i[0].rstrip("\n")
        y = i[1].rstrip("\n")
        new_joined.append(x + y)
    return new_joined


def hashPass(passwordAndSalt):
    """this function takes a password+salt string and uses MD5 hash algorithm"""
    m = hashlib.md5()
    m.update(passwordAndSalt.encode("utf-8"))
    return m.hexdigest()


def hashToList():
    """this function makes a list of the hashed passwords+salt"""
    new_joined = []
    for salt in addSalt():
        new_joined.append(hashPass(salt))
    return new_joined


def verify(list1, list2):
    """this function checks if the password and salt match the hash in the database"""
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print(
                "The input password and salt does not match the hash value in the database"
            )
        else:
            print("The input password and salt matches the hash value in the database")


def crackerSystem(uid, hash):
    for password in getPass():
        for salt in getSalt():
            preHash = password + salt
            if hashPass(preHash) == hash:
                return password, salt
    return "Cannot return password and salt"


# print(verify(getHash(), hashToList()))
# 10 different UIDs:
print(crackerSystem("001", "4a1d6f102cd95fac33853e4d72fe1dc5"))
print(crackerSystem("002", "e8e7d67256aedc225a072540540d910c"))
print(crackerSystem("003", "0c6a7629e1fe2eab887de89dd65072d9"))
print(crackerSystem("004", "0e8b4ee66ad464aee37a934d74088613"))
print(crackerSystem("005", "6261a6ddd461304eaed4090348d8d117"))
print(crackerSystem("006", "cfa0000941daff46ebf0ef1950c86db0"))
print(crackerSystem("007", "e09a3a07abbaa5bf3170e6d297dff065"))
print(crackerSystem("008", "11dcc98c009eb5b2a9449d05ea8bb381"))
print(crackerSystem("009", "dfbcb13e80aa4cfb872f987b17879ec8"))
print(crackerSystem("010", "db8a21330a299c4fcae3534cc7f1e01b"))
