import matplotlib.pyplot as plt
import numpy as np
import time

from PIL import Image
import os
import sys


def compressImg(filename):
    img = Image.open(filename)
    imggray = img.convert('LA')
    imggray.show()
    plt.figure(figsize=(9, 6))
    plt.imshow(imggray)

    imgmat = np.array(list(imggray.getdata(band=0)), float)
    imgmat.shape = (imggray.size[1], imggray.size[0])
    imgmat = np.matrix(imgmat)
    plt.figure(figsize=(9, 6))
    plt.imshow(imgmat, cmap='gray')
    plt.show()

    U, sigma, V = np.linalg.svd(imgmat)

    print(U)
    print(sigma)
    print(V)

    reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
    plt.imshow(reconstimg, cmap='gray')

    for i in range(2, 4):
        reconstimg = np.matrix(U[:, :i]) * \
            np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
        plt.show()

    for i in range(5, 51, 5):
        reconstimg = np.matrix(U[:, :i]) * \
            np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
        plt.show()


def compressTxt(filename):
    # convert file to bits using standard format

    # figure out row length to maximize multiplicity of 0s
    
    # run svd on the output
    pass


def compress(dir):
    print(dir)
    tempcwd = os.getcwd()
    if os.path.isdir(os.path.join(tempcwd, dir)):
        for d in os.listdir(os.path.join(tempcwd, dir)):
            os.chdir(os.path.join(tempcwd, dir))
            extension = d.split(".")[1]
            if extension == "txt":
                compressTxt(d)
            elif extension == "jpg" or extension == "png":
                compressImg(d)
            else:
                print("filetype not supported, " + d + " was not compressed")
            compress(d)
            os.chdir(tempcwd)


def main():
    if len(sys.argv) != 2:
        print("use file")
    else:
        compress(str(sys.argv[1]))


if __name__ == "__main__":
    main()
