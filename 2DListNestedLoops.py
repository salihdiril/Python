matris = [
    [1, 2, 3, 4, 5],
    [6, 7],
    [8, 9, 10],
    [11, 12, 13, 14, 25, 16],
    [17],
    [18, 39, 20, 21]
]

print(matris)
print(matris[2])
print(matris[3][4])

for row in range(len(matris)):
    print(matris[row])

for row in matris:
    for col in row:
        print(col)