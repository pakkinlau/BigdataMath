Wavelet transforms are mathematical transformations used in signal processing and image analysis to analyze and process signals and images at different scales. Unlike traditional Fourier transforms, which analyze signals in terms of sinusoidal basis functions, wavelet transforms use wavelets, which are small, localized functions with limited duration in both time and frequency domains. Wavelet transforms have the advantage of capturing both high and low-frequency components of a signal or an image with better localization.

Here's a brief explanation of the wavelet transforms you mentioned:

1. **Haar Wavelet:** Haar wavelet is the simplest wavelet function. It consists of two values, +1 and -1, and is used for basic wavelet analysis due to its simplicity. Haar wavelet transform is often used for educational purposes and as a building block for more complex wavelets.

2. **Bior Wavelets:** Bior wavelets, short for "Biorthogonal wavelets," use two different wavelet functions: one for decomposition and another for reconstruction. These wavelets are designed to provide a balance between frequency localization and time localization, making them suitable for various applications in signal and image processing.

3. **Mexican Hat Wavelet:** The Mexican Hat wavelet, also known as Ricker wavelet, is characterized by its bell-shaped waveform. It is often used in the analysis of seismic signals and is particularly good at representing transient phenomena due to its shape.

These are just a few examples. There are many other types of wavelets, each with specific properties suited for different applications. Wavelet transforms find applications in areas such as data compression, denoising, feature extraction, and pattern recognition, among others. Different wavelet functions are used based on the specific requirements of the application and the characteristics of the signals or images being analyzed.

---
## Process:
- 1. Load data
- 2. Take the transformed data: `coeffs3 = pywt.wavedec2(im, 'haar')`
- 3. Get the image we want: `cA2 = coeffs[0]`


---
## Examples:

- 2b multilevel decomposition
	- `pywt.wavedec2()`: produces a list of stuffs  and we store it in `coeffis`.
		- `LL`: `coeffs[0]` represents the approximation coefficients at the highest level of resolution.
		- `LH`: `coeffs[1]` represents  the horizontal detail coefficients. 
		- `HL`:  `coeffs[2]` represents the vertical detail coefficients
		- `HH`:`coeffs[3]` represents the diagonal detail coefficients
```python
coeffs3 = pywt.wavedec2(im, 'haar') # performs a two-dimensional wavelet decomposition of an input image im using the Haar wavelet

coeffs3[-1] = tuple([np.zeros_like(v) for v in coeffs3[-1]]) # corresponds to the coefficents at the finest level. The code replaces these coefficients with zeros of the same shape as the original coefficients. Essentially, it removes the highest-frequency details from the signal.
coeffs3[-2] = tuple([np.zeros_like(v) for v in coeffs3[-2]]) # replacing signals for the second finest level. 

```

```python
# Iterate through each image in the images dataframe
for idx, row in images.iterrows():
    # idx: the index of the current row
    # row: the data of the current row
    
    # Reshape the image to 64x64
    image = row.values.reshape(64, 64)
    
    # Perform 2-level discrete wavelet transform
    coeffs = pywt.wavedec2(image, 'haar', level=num_levels)
    
    # Extract the approximation coefficients at the highest level
    cA2 = coeffs[0]
    
    # Flatten the coefficients and append them to Theta_columns
    flattened_coeffs = cA2.flatten() # flattening means converting a multi-dimensional array into a 1D array
    Theta_columns.append(flattened_coeffs)
```

