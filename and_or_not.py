print('AND')

print(True and True)
print(False and True)
print(False and False)

a, b, c = 1, 2, 3

print(b > a and c > a)
print(c > a and c < 0)
print()

print('OR')
print(True or True)
print(False or True)
print(False or False)

print(b > a or c > a)
print(c < 0 or c > a)
print(c == 4 or b != 2)
print()

print('NOT')
print(not True)
print(not False)
print(not (c !=3))
print(not (c == 3))