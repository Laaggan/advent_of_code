import numpy as np
import matplotlib.pyplot as plt
input_path = 'input/real_input_day_13.txt'
data = open(input_path).read().split('\n\n')
points = data[0]
folds = data[1]

points = np.array([list(map(int, a.split(','))) for a in points.split('\n')])
folds = [fold.split('=') for fold in folds.split('\n')]
for fold in folds:
    fold[0] = fold[0].replace("fold along ", "")
    fold[1] = int(fold[1])

paper = np.zeros((np.max(points[:, 1]) + 1, np.max(points[:, 0]) + 1))

for x, y in points:
    paper[y, x] = 1


for fold in folds:
    if fold[0] == 'y':
        upper_part = paper[:fold[1], :]
        lower_part = paper[(fold[1] + 1):, :]
        lower_part = np.flipud(lower_part)
        i = upper_part.shape[0] - lower_part.shape[0]
        upper_part[i:, :] = upper_part[i:, :] + lower_part
        paper = upper_part
    else:
        left_part = paper[:, :fold[1]]
        right_part = paper[:, (fold[1] + 1):]
        right_part = np.fliplr(right_part)
        j = left_part.shape[1] - right_part.shape[1]
        left_part[:, j:] = left_part[:, j:] + right_part
        paper = left_part

plt.imshow(paper > 0)
plt.show()
print(np.sum(np.sum(paper > 0)))