---
alias: FFT
---

- faster computation
	- FFT transform the whole industry. 
		- $n^2$ multiplication of DFT downs to $n\ log(n)$
	

---

## FFTSHIFT over an image

The primary reason for using fftshift is for visualization purposes. It makes it easier to interpret the Fourier transform by having the low frequencies centered in the output. 

When you perform a 2D Fourier transform on an image, you obtain a complex-valued array representing the frequency components of the image. In this Fourier spectrum:

- The element at index `[0, 0]` (top-left corner) represents the DC component, i.e., the average intensity of the image.
- The high-frequency components are located at the corners of the Fourier spectrum, and the low-frequency components are located at the center.

The arrangement looks something like this, assuming `N` is the size of the Fourier transform array (assuming it's a square array for simplicity):

```
[High Freq] [         ] [High Freq]
[          ] [          ] [          ]
[          ] [          ] [          ]
[High Freq] [          ] [High Freq]
```

In many applications, especially in image processing and analysis, it's useful to rearrange the Fourier spectrum so that the DC component (low-frequency component) is at the center of the spectrum. This rearrangement facilitates analysis and visualization, making it easier to identify various frequency components.

Mathematically, if `F(u, v)` represents the Fourier spectrum at position `(u, v)`, where `u` and `v` are indices in the range `[0, N-1]`, `fftshift()` performs the following transformation:

\[ \text{fftshift}(F(u, v)) = F(u - \lfloor N/2 \rfloor, v - \lfloor N/2 \rfloor) \]

In other words, it shifts the indices by half of the size of the array. This operation ensures that the DC component is at the center, and the high-frequency components are at the corners.

By using `fftshift()`, you bring the low-frequency components to the center, making it more intuitive to analyze and process the Fourier spectrum, especially in tasks like filtering and visualization.


---
