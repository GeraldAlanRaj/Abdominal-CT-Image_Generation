# 🧠 Diffusion‑GAN for Synthetic Abdominal CT Generation

A concise PyTorch notebook that trains a **lightweight Diffusion‑GAN** to generate **128 × 128** synthetic abdominal CT slices from the CHAOS dataset(or any single‑channel CT dataset laid out as plain image files).

---

## ✨ Features

- ⏱️ **Time‑conditioned U‑Net generator** with sinusoidal embeddings  
- 🧩 **PatchGAN discriminator** with spectral normalization  
- 🎯 **Mixed loss function**:
  - Reconstruction loss (L1)
  - GAN loss (BCE)
  - Perceptual loss (VGG‑16)
  - MSE loss  
- 📉 **Cosine noise schedule** (1 000 steps) with progressive **time‑window curriculum**  
- ⚙️ **Simple helper routines** for:
  - Training
  - Inference
  - Image-quality metrics: **MAE**, **SSIM**, **PSNR**

---
## 📌 Note

- This project is designed for simplicity and clarity, perfect for research prototypes or academic exploration.
- Results may vary depending on dataset size, quality, and training duration.
