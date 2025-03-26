# Sickness Identification Using Hyperspectral Imaging - Wheat

### Key Findings from Literature:
1. **Fusarium (Wheat)**:
   - Infected wheat crops display lower reflectance in the green (500–570 nm) and higher reflectance in the shortwave infrared (SWIR) region (1000–1700 nm).
   - Changes in the red edge position (680–750 nm) indicate early-stage infection.

## Key Wavelengths Indicative of Diseases
Based on literature review, the most indicative wavelengths for disease detection in wheat are:

| Disease   | Wavelength Range (nm) | Affected Spectral Region |
|-----------|----------------------|-------------------------|
| Fusarium  | 500–570              | Green                   |
|   | 680–750              | Red Edge                |
|   | 1000–1700            | Shortwave Infrared (SWIR)|

## Pre-Processing Techniques for Hyperspectral Image Analysis
To improve disease detection accuracy in wheat, pre-processing techniques are crucial. Common methods include:

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
