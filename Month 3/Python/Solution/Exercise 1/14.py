print("Using for loop:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


print("Using while loop:")
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
