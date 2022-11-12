from PIL import Image
import numpy as np

def npy2png4(name, i_size, j_size, y_size, x_size):
    weights = np.load(name + ".npy")

    img = Image.new(mode="RGB", size=(x_size*j_size, i_size*y_size))

    for i in range(i_size):
        for j in range(j_size):
            for y in range(y_size):
                for x in range(x_size):
                    v = round((weights[i][j_size - j - 1][y][x] + 1) * 127.5)
                    img.putpixel((j * x_size + x, i * y_size + y), (v, v, v))

    img.save(name + ".png")

def npy2png4_2(name, i_size, j_size, y_size, x_size):
    weights = np.load(name + ".npy")

    img = Image.new(mode="RGB", size=(x_size*j_size, i_size*y_size))

    for i in range(i_size):
        for j in range(j_size):
            for y in range(y_size):
                for x in range(x_size):
                    v = round((weights[i][j_size - j - 1][y_size - y - 1][x] + 1) * 127.5)
                    img.putpixel((j * x_size + x, i * y_size + y), (v, v, v))

    img.save(name + ".png")

def npy2png3(name, j_size, y_size, x_size):
    weights = np.load(name + ".npy")

    img = Image.new(mode="RGB", size=(x_size * j_size, y_size))

    for j in range(j_size):
        for y in range(y_size):
            for x in range(x_size):
                v = round((weights[j_size - j - 1][y][x] + 1) * 127.5)
                img.putpixel((j * x_size + x, y), (v, v, v))

    img.save(name + ".png")

def npy2png2(name, y_size, x_size):
    weights = np.load(name + ".npy")

    img = Image.new(mode="RGB", size=(x_size, y_size))

    for y in range(y_size):
        for x in range(x_size):
            v = round((weights[y][x] + 1) * 127.5)
            img.putpixel((x, y), (v, v, v))

    img.save(name + ".png")

npy2png4("weight1", 8, 1, 5, 5)
npy2png4("weight2", 16, 8, 5, 5)
npy2png4_2("weight3", 16, 4, 4, 10)
npy2png3("bias1", 8, 1, 1)
npy2png3("bias2", 16, 1, 1)
npy2png2("bias3", 1, 10)