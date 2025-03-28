# Sickness Identification Using Hyperspectral Imaging - Wheat

## Disease Detection in Wheat

### **Fusarium (Wheat)**
**Fusarium** disease in wheat is detected as follows:

- **Decreased reflectance in the green range (500–570 nm)**: Infected wheat plants show lower reflectance in this range because **Fusarium** causes tissue damage and reduces chlorophyll content.
- **Shift in the "red edge" (680–750 nm)**: **Fusarium** causes a shift in the red edge, which is one of the first symptoms of the disease. This change results from a decrease in the plant's ability to absorb light in this range.
- **Increased reflectance in the SWIR range (1000–1700 nm)**: Stress caused by **Fusarium** infection can increase reflectance in the shortwave infrared (SWIR) range, which can appear as lighter patches on hyperspectral images.

![red edge](img/rededge.png)

On images, symptoms of **Fusarium** will look like:
- Darker patches in the green range, indicating chlorophyll damage.
- A shift in the red edge, visible as a change in the 680-750 nm region.
- Lighter patches in the SWIR range (1000–1700 nm) associated with cellular damage.

### Detecting **Fusarium** in Wheat:
To detect **Fusarium**, focus on:
- Decreased reflectance in the green range, which indicates damage to photosynthesizing plant cells.
- Changes in the red edge, which can be used to detect early signs of the disease.
- Increased reflectance in the SWIR range, which may indicate plant stress and structural damage caused by the infection.


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
