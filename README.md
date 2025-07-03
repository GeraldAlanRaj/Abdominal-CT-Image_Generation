🧠 Diffusion‑GAN for Synthetic Abdominal CT Generation

A concise and modular PyTorch notebook that trains a lightweight Diffusion‑GAN to generate 128 × 128 synthetic abdominal CT slices from the CHAOS dataset or any single‑channel CT dataset organized as plain image files.

<br/>
✨ Key Features

🎯 Time-conditioned U‑Net generator
Powered by sinusoidal timestep embeddings to guide the diffusion process.
🧩 PatchGAN Discriminator
Spectral normalization enabled for stable adversarial training.
🧠 Hybrid Loss Function
Combines Reconstruction (MSE), GAN loss, Perceptual loss (VGG‑16), and L1 Loss.
📉 Cosine Noise Schedule
Uses a 1 000-step cosine noise scheduler with progressive curriculum learning based on timestep windows.
📊 Built-in Image Quality Evaluation
Automatic evaluation using:
MAE (Mean Absolute Error)
SSIM (Structural Similarity Index)
PSNR (Peak Signal-to-Noise Ratio)
🛠️ Minimal Helper Routines
Includes streamlined functions for training, inference, checkpointing, and metric computation.
<br/>
