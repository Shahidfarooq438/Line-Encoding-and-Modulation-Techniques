import numpy as np
import matplotlib.pyplot as plt

def pcm_encoding(analog_signal, quantization_levels):
    # Normalize the analog signal to the range [0, 1]
    normalized_signal = (analog_signal - min(analog_signal)) / (max(analog_signal) - min(analog_signal))

    # Quantize the normalized signal
    quantized_signal = np.round(normalized_signal * (quantization_levels - 1))

    return quantized_signal

# Example usage:
# Generate a sample analog signal (sine wave)
time = np.arange(0, 1, 0.001)
amp=float(input("Enter Amplitude of signal:\n"))
freq=float(input("Enter frequency of signal:\n"))
analog_signal = amp * np.sin(2 * np.pi * freq * time) + amp * np.sin(2 * np.pi * (2*freq) * time)

# Set the number of quantization levels (bits per sample)
quantization_levels = 8

# PCM encoding
pcm_encoded_signal = pcm_encoding(analog_signal, quantization_levels)

# Plot the original analog signal and the PCM encoded signal
plt.subplot(2, 1, 1)
plt.plot(time, analog_signal)
plt.title('Original Analog Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.step(time, pcm_encoded_signal, linewidth=1)
plt.title('PCM Encoded Signal')
plt.xlabel('Time')
plt.ylabel('Quantized Level')

plt.tight_layout()
plt.show()

print(pcm_encoded_signal)
