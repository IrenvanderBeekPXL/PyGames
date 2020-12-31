file = open("prime.txt", "a")
file.write("2\n")
number = 3
while True:
    prime = True
    for i in range(3, number, 2):
        if number % i == 0:
            prime = False
            break
    if prime:
        file.write(str(number) + "\n")
    number += 2

#A ridiculously small program for extremely large prime numbers.