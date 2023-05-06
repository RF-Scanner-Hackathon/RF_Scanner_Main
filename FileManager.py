import os
import shutil

userArray = []


def __init__(self):
    # if not os.path.exists("user.txt"):
    # Write the folder path to a file
    open("users.txt", "x")
    loadUserArray()


def create_folder(fname, lname, last4DigitsOfPhone):
    # Create a folder with the user's name
    f_name = (fname + lname + last4DigitsOfPhone)
    folder_name = f"{f_name}"
    folder_path = os.path.join(os.getcwd(), folder_name)
    if os.path.exists(folder_path):
        return
    os.makedirs(folder_path)

    # Create file name with folder name
    infoFile_name = "info.txt"

    # Get user input for file contents & Create and write to file
    with open(os.path.join(folder_name, infoFile_name), "w") as file:
        file.write(fname + '\n' + lname + '\n' + last4DigitsOfPhone + '\n' + folder_path)

    # Write the folder path to a file
    with open("users.txt", "a") as f:
        f.write(f"{folder_path}\n")

    return folder_path


class user:
    def __init__(self, fname, lname, pnumber, fpath):
        self.fname = fname
        self.lname = lname
        self.pnumber = pnumber
        self.fpath = fpath

    def __str__(self):
        returnString = self.fname
        returnString += '-'
        returnString += self.lname
        returnString += '-'
        returnString += self.pnumber
        returnString += '-'
        returnString += self.fpath
        return returnString

    def getPath(self):
        return self.fpath

    def getFname(self):
        return self.fname

    def getPNumber(self):
        return self.pnumber

    def equals(self, other):
        if self.fname == other.fname and self.pnumber == other.pnumber:
            return True
        return False

    def logInComp(self, fname, pnumber):
        if self.fname == fname and self.pnumber == pnumber:
            return True
        return False


def loadUser(infoTextFilePath):
    tempFile = open(infoTextFilePath, "r")
    tempUser = user(tempFile.readline(), tempFile.readline(), tempFile.readline(), tempFile.readline())
    return tempUser


def getInfoText(folderPath):
    folderPath = folderPath.rstrip('\n')
    print(folderPath)
    fileName = "info.txt"
    for root, dirs, files in os.walk(folderPath):
        if fileName in files:
            return os.path.join(root, fileName)
    print("Cant find info with ")
    print(folderPath)
    return


def save_file(user, file_path):
    new_file_path = shutil.move(file_path, user.fpath)

    return new_file_path


# def  load_file(user, )

# The following method will search for the user.
def log_in(fname, lastFourDigitOfPhoneNo):
    for element in userArray:
        if element.fname.strip().__eq__(fname.strip()) and element.pnumber.strip().__eq__(
                lastFourDigitOfPhoneNo.strip()):
            # if element.logInComp(fname, lastFourDigitOfPhoneNo):
            print("user found")
            return element
        print(fname)
        print(type(fname))
        print(element.getFname())
        print(type(element.getFname()))
    print("user not found")
    return


def loadUserArray():
    returnArray = []
    with open("users.txt", "r") as f:
        for line in f:
            returnArray.append(line)
    for element in returnArray:
        # print(element)
        userArray.append(loadUser(getInfoText(element)))

        # print(element)
        # print(getInfoText(str(element)))

    return returnArray


def main():
    # f_name = input("Enter the first name : ")
    # l_name = input("Enter the last name : ")
    # phone = str(input("Enter the last 4 digits of phone number : "))
    # tempVar = loadUser(getInfoText(create_folder(f_name,l_name, phone)))

    # print(tempVar)
    # print(tempVar.getPath())
    print(loadUserArray())
    # print(userArray)

    # print(userArray[0])
    save_file(log_in("Sam", "9999"), r"C:\Users\Samarpita Podder\Desktop\file.txt")


main()