
# coding: utf-8

# In[2]:


import numpy as np
from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Dropout, Input
from keras.layers.recurrent import LSTM
import matplotlib.pyplot as plt


X_train = np.load(r"/Users/lukangjin/Desktop/Train_2016.npy")
Y_train = np.load(r"/Users/lukangjin/Desktop/Label_2016.npy")

Y_train /= np.max(Y_train)

X_test = np.load(r"/Users/lukangjin/Desktop/Train_2016.npy")
Y_test = np.load(r"/Users/lukangjin/Desktop/Label_2016.npy")

Y_test /= np.max(Y_test)


lstm_model_input = Input((5, 62))


lstm_model_lstm_1 = LSTM(128, return_sequences=True)(lstm_model_input)


lstm_model_dropout_1 = Dropout(0.2)(lstm_model_lstm_1)


lstm_model_lstm_2 = LSTM(512, return_sequences=False)(lstm_model_dropout_1)


lstm_model_dropout_2 = Dropout(0.2)(lstm_model_lstm_2)


lstm_model_output = Dense(1, activation='sigmoid')(lstm_model_dropout_2)


lstm_model = Model(inputs=lstm_model_input, outputs=lstm_model_output)


lstm_model.compile(loss='mse', optimizer='Adam')



training_set_input = np.array([X_train[i: i + 5] for i in range(len(X_train) - 5)])
testing_set_input = np.array([X_test[i: i + 5] for i in range(len(X_test) - 5)])


training_set_output = np.array([Y_train[i + 5] for i in range(len(Y_train) - 5)])
testing_set_output = np.array([Y_test[i + 5] for i in range(len(Y_test) - 5)])


lstm_model.fit(training_set_input, training_set_output, epochs=2)


print('\nTesting-------')
cost = lstm_model.evaluate(testing_set_input, testing_set_output)
print('test cost:', cost)


X = np.linspace(0, len(testing_set_output), len(testing_set_output))
Y_pred = lstm_model.predict(testing_set_input)

print(Y_pred)
plt.scatter(X, testing_set_output, color = 'blue')
plt.plot(X, Y_pred, color = 'green')
plt.show()
















