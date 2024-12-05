import matplotlib.pyplot as plt

# Apply Fourier Transform to identify dominant frequencies in vibration data
vibration_fft = fft(df['vibration_smooth'].dropna())
frequencies = np.fft.fftfreq(len(vibration_fft))

# Plot the FFT results
plt.figure(figsize=(10, 6))
plt.plot(frequencies, np.abs(vibration_fft))
plt.title("Frequency Analysis of Vibration Data")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()
