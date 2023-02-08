class Encryptor_Decryptor():
    def __init__(self, filename):
        self.filename = filename
        
    def Encrypt(self):
        with open(self.filename, "r") as file:
            filetxt = file.read()
        txtlist = [*filetxt]
        newstr = ""
        for letter in txtlist:
            newstr += chr(ord(letter)+ 3)
        with open(self.filename, "w") as file:
            file.write(newstr)

    def Decrypt(self):
        with open(self.filename, "r") as file:
            filetxt = file.read()
        txtlist = [*filetxt]
        newstr = ""
        for letter in txtlist:
            newstr += chr(ord(letter)- 3)
        with open(self.filename, "w") as file:
            file.write(newstr)

en1 = Encryptor_Decryptor("sample.txt")
en1.Encrypt()
