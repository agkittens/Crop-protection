# Sickness Identification Using Hyperspectral Imaging - Cabbage

### Key Findings from Literature:
1. **Alternaria (Cabbage)**:
   - Infected cabbage leaves exhibit higher reflectance in the near-infrared (NIR) region due to tissue damage.
   - Decreases in reflectance in the visible range (400–700 nm), particularly in the blue (450–495 nm) and red (620–750 nm) spectra.
   
2. **Botrytis cinerea (Cabbage)**:
   - Infected cabbage plants show reduced reflectance in the visible spectrum.
   - Significant reflectance changes in the near-infrared (750–900 nm) region.

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
