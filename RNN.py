#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from sklearn.preprocessing import MinMaxScaler

#PART 1:Data Preprocessing


#Importing the training set & Splitting to opening price,2D import to fit the RNN

#**********GOOGLE**********
google_train_set=pd.read_csv("Google_Stock_Price_Train.csv")
google_train_set=google_train_set.iloc[:,1:2].values


#Scaling the training set,Normalize for a value between 0 and 1
google_scaler=MinMaxScaler()
google_train_set=google_scaler.fit_transform(google_train_set)

#x_train -> Stock price of day x,used for predicting the stock price of day x+k,where k is the timeframe
#y_train -> Stock price of day x+k

google_x_train=google_train_set[0:1257]
google_y_train=google_train_set[1:1258]


#Reshaping the training set,Including the timeframe value
google_x_train=np.reshape(google_x_train,(1257,1,1))

#**********APPLE**********
apple_train_set=pd.read_csv("Apple_Stock_Price_Train.csv")
apple_train_set=apple_train_set.iloc[:,1:2]

apple_scaler=MinMaxScaler()
apple_train_set=apple_scaler.fit_transform(apple_train_set)

apple_x_train=apple_train_set[0:1257]
apple_y_train=apple_train_set[1:1258]

apple_x_train=np.reshape(apple_x_train,(1257,1,1))

#**********AMAZON**********


#**********MICROSOFT**********


#**********TESLA**********



#PART 2:Neural Network

#**********GOOGLE**********

#Initalizing the RNN
google_rnn=Sequential()

#Adding the LSTM RNN Input layer
#Input shape:timeframe and number of input nodes
google_rnn.add(LSTM(units=4,activation='sigmoid',input_shape=(1,1)))

#Adding the output layer
google_rnn.add(Dense(units=1))

#Compiling the RNN
google_rnn.compile(optimizer='adam',loss='mean_squared_error')

#Fitting the RNN
google_rnn.fit(google_x_train,google_y_train,batch_size=16,epochs=200)

#**********APPLE**********


#**********AMAZON**********


#**********MICROSOFT**********


#**********TESLA**********



#PART 3:Prediction


#Importing the test set
google_test_set=pd.read_csv("Google_Stock_Price_Test.csv")
#Splitting the opening price
google_real_stock_price=google_test_set.iloc[:,1:2].values

#Scaling the real prices,int the same format of training set

#**********GOOGLE**********
google_inputs=google_real_stock_price
google_inputs=google_scaler.transform(google_inputs)
google_inputs=np.reshape(google_inputs,(20,1,1))

#Prediciting the stock prices for first 20 days of January 2017
google_predicted_stock_price=google_rnn.predict(google_inputs)
#Inverse scaling the predicted prices
google_predicted_stock_price=google_scaler.inverse_transform(google_predicted_stock_price)

#**********APPLE**********


#**********AMAZON**********


#**********MICROSOFT**********


#**********TESLA**********



#PART 4:Plotting

#**********GOOGLE**********
plt.plot(google_real_stock_price,color='red',label='Real Price')
plt.plot(google_predicted_stock_price,color='blue',label='Predicted Price')
plt.xlabel("Days")
plt.ylabel("Stock Price($)")
plt.title("Google Stock Price Prediction (Jan 2017)")
plt.legend()
plt.show()

#**********APPLE**********


#**********AMAZON**********


#**********MICROSOFT**********


#**********TESLA**********


