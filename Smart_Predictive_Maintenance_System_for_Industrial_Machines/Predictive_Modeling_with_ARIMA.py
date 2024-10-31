from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Scale the data for LSTM
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df[['vibration_smooth']].dropna())

# Prepare the training data for LSTM
sequence_length = 50
X_train, y_train = [], []

for i in range(sequence_length, len(scaled_data)):
    X_train.append(scaled_data[i-sequence_length:i, 0])
    y_train.append(scaled_data[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(units=1))

# Compile and train the model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=20, batch_size=32)

# Predict future values using the trained LSTM
predicted_vibration = model.predict(X_train[-sequence_length:])
predicted_vibration = scaler.inverse_transform(predicted_vibration)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'].iloc[-len(predicted_vibration):], df['vibration_smooth'].iloc[-len(predicted_vibration):], label='True Vibration')
plt.plot(df['timestamp'].iloc[-len(predicted_vibration):], predicted_vibration, label='LSTM Prediction', color='orange')
plt.title("LSTM Prediction of Vibration Data")
plt.legend()
plt.show()
