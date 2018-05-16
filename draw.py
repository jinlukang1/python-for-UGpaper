import os
import numpy as np
import matplotlib.pyplot as plt

def main():
	f = open(r"/Users/lukangjin/Desktop/Label_2018.npy", "rb")
	X = np.load(f)
	X[786] = 0
	print(X)
	Y = np.linspace(0, len(X), len(X))
	plt.figure()
	plt.scatter(Y, X)
	plt.show()

if __name__ == '__main__':
	main()