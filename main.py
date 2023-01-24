import random
symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}[](),;:#$%-_"
length = 8
password = "".join(random.sample(symbols,length))

print(password)
