rows  = int(input("9"))
stars = int(input("6"))

for row in range(rows):
    len = stars if row % 2 == 0 else stars - 1
    print '*' * len