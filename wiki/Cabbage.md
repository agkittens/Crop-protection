# Sickness Identification Using Hyperspectral Imaging - Cabbage

## Disease Detection in Cabbage

### **Alternaria**
**Alternaria** disease appears in hyperspectral images in the following ways:

- **Increased reflectance in the NIR range**: Due to tissue damage caused by the fungus, cabbage leaves infected with **Alternaria** will have higher reflectance in the near-infrared range (800-1000 nm) compared to healthy plants. This can appear as lighter patches in this range.
- **Decreased reflectance in the visible ranges (blue and red)**: In the 450-495 nm (blue) and 620-750 nm (red) ranges, there is reduced reflectance. This results from a decrease in chlorophyll content, causing the plant to lose intensity in these wavelengths.

On hyperspectral images, the disease can manifest as:
- Darker, less saturated areas in the visible ranges, particularly blue and red, indicating reduced chlorophyll content.
- Lighter patches in the NIR range, where damaged tissues reflect more light.

### **Botrytis cinerea**
**Botrytis cinerea** disease appears in the following way:

- **Reduced reflectance in the visible range**: Infected cabbage plants have lower reflectance in the 400-700 nm (visible) range, which may appear as darker areas on the images.
- **Increased reflectance in the NIR range**: There is increased reflectance in the 750-900 nm range, which indicates changes in cell structure and the onset of chlorophyll degradation.

Symptoms on hyperspectral images:
- Darker areas in the visible range, especially in the blue and red spectra, due to a decrease in chlorophyll.
- Lighter patches in the NIR range, indicating advanced stages of infection where the plant's structural integrity is compromised.

## Harmful Symptoms on Images:
- **Color changes**: Pay attention to changes in intensity, especially in the blue and red bands.
- **Visible patches**: Clear patches will appear on images that differ from healthy, undamaged leaves.

## Detecting Alternaria and Botrytis cinerea in Cabbage:
To identify these diseases, focus on:
- Changes in reflectance in specific bands, especially those that show reduced or increased reflectance (e.g., changes in blue, red, and NIR colors).
- Use of classification algorithms that can detect subtle differences in the spectral image, including changes in plant cell structure.


## Key Wavelengths Indicative of Diseases
Based on literature review, the most indicative wavelengths for disease detection in cabbage are:

| Disease           | Wavelength Range (nm) | Affected Spectral Region |
|------------------|---------------------|-------------------------|
| Alternaria       | 450–495             | Blue                   |
|        | 620–750             | Red                    |
|        | 800–1000            | Near-Infrared (NIR)    |
| Botrytis cinerea | 400–700             | Visible                |
|  | 750–900             | Near-Infrared (NIR)    |

## Pre-Processing Techniques for Hyperspectral Image Analysis
To improve disease detection accuracy in cabbage, pre-processing techniques are crucial. Common methods include:

1. **Noise Reduction**:
   - Gaussian filtering
   - Savitzky-Golay smoothing
   - Principal Component Analysis (PCA)-based denoising

2. **Dimensionality Reduction**:
   - PCA: Reduces spectral redundancy and enhances classification accuracy.
   - Independent Component Analysis (ICA): Separates disease-specific spectral signatures.
   - Minimum Noise Fraction (MNF): Maximizes signal-to-noise ratio.

3. **Feature Selection Methods**:
   - Band selection based on disease-sensitive wavelengths.
   - Normalized Difference Vegetation Index (NDVI) for stress detection.

## References
https://www.sciencedirect.com/science/article/pii/S2589721720300295#bb0040
https://www.sciencedirect.com/science/article/abs/pii/S0168169910001262
https://www.sciencedirect.com/science/article/abs/pii/S0168169924003995
