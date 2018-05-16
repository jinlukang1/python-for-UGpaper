import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
import matplotlib.pyplot as plt

X_train = np.load(r"/Users/lukangjin/Desktop/Train_2016.npy")
Y_train = np.load(r"/Users/lukangjin/Desktop/Label_2016.npy")

Y_train /= np.max(Y_train)

X_test = np.load(r"/Users/lukangjin/Desktop/Train_2017.npy")
Y_test = np.load(r"/Users/lukangjin/Desktop/Label_2017.npy")

Y_test /= np.max(Y_test)

#Y_test[786] = 0
least = 10

model = Sequential()
model.add(Dense(output_dim = 119, input_dim = 62, activation = 'sigmoid'))
model.add(Dense(output_dim = 74, activation = 'sigmoid'))
model.add(Dense(output_dim = 1, activation = 'sigmoid'))

model.compile(loss = 'mse', optimizer = 'Adam')

print('Training-------')
#for step in range(3001):
#	cost = model.train_on_batch(X_train, Y_train)
#	if step % 50 == 0:
#		print('train cost', cost)
model.fit(X_train, Y_train, epochs = 20)


print('\nTesting-------')
cost = model.evaluate(X_test, Y_test, batch_size = 20)
print('test cost:', cost)


X = np.linspace(0, len(Y_test), len(Y_test))
Y_pred = model.predict(X_test)


plt.scatter(X, Y_test, color = 'blue')
plt.plot(X, Y_pred, color = 'green')
plt.show()



