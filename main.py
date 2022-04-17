import numpy as np
from matplotlib import pyplot as plt, projections

x = [  # s x1 x2
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1],
]
o = [[0, 0, 1, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 0, 1, 1]]
w = [[i for i in np.random.random(3)], [i for i in np.random.random(3)]]
# w = [[1,2,3], [3,2,1]]
teta = [i for i in np.random.random(2)]
# teta = [1, 2]
eta = 0.1
e = 1

# history_w = [[], []]
# history_teta = [[], []]
# history_e = []

print("x: " + x.__str__())
print("o: " + o.__str__())
print("eta: " + eta.__str__())
print("w: " + w.__str__())
print("teta: " + teta.__str__())
print("----------------------------------------------------")

epoch = 0
while e > 0 and epoch < 50:
    e = 0
    i = 0
    # history_w[0].append(w[0])
    # history_w[1].append(w[1])
    #
    # history_teta[0].append(teta[0])
    # history_teta[1].append(teta[1])

    while i < len(x):
        y1 = np.inner(x[i], w[0])
        if y1 >= teta[0]:
            y1 = 1
        else:
            y1 = 0
        if y1 != o[0][i]:
            temp = eta * (o[0][i] - y1)
            teta[0] = teta[0] - temp
            temp_x = np.dot(temp, x[i])
            w = w + temp_x
            e = e + abs(o[0][i]-y1)

        y2 = np.inner(x[i], w[1])
        if y2 >= teta[1]:
            y2 = 1
        else:
            y2 = 0
        if y2 != o[1][i]:
            temp = eta * (o[1][i] - y2)
            teta[1] = teta[1] - temp
            temp_x = np.dot(temp, x[i])
            w = w + temp_x
            e = e + abs(o[1][i]-y2)

        i += 1

    # history_e.append(e)
    epoch += 1

    print("epoch: " + epoch.__str__())
    print("e: " + e.__str__())
    print("w: " + w.__str__())
    print("teta: " + teta.__str__())
    print("----------------------------------------------------")

# fig = plt.figure()
# ax = plt.axes(projection='3d')
#
# x = np.linspace
#
# np.meshgrid()
# i = 0
# while i < len(history_w[0]):
#     ax.plot_surface(history_w[0][i][0], history_w[0][i][1], history_w[0][i][2], color='green')
#     i += 1
#     plt.scatter(history_w[0], history_teta[0], "-ok", marker="o", c="green")

# plt.scatter(history_w[0], history_teta[0], "-ok", marker="o", c="green")
# plt.plot(history_w[0], history_teta[0], "-ok", marker="o", c="blue")
# plt.plot(history_w[1], history_teta[1], "-ok", marker="^", c="red")

# ax.set_xlabel("W")
# ax.set_ylabel("teta")
# ax.set_zlabel("E")

# plt.show()
