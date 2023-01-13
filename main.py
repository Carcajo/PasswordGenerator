import random
lettersDown = "abcdefghijklmnopqrstuvwxyz"
lettersUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "{}[](),;:#$%-_"
numbers = "1234567890"

summa = lettersUp + lettersDown + symbols + numbers
length = 8
password = "".join(random.sample(summa,length))

print(password)
