class Str:
    def getString(self):
        self.s = input()
    def printString(self):
         print(self.s.upper())

s1 = Str()

s1.getString()
s1.printString()