Diffusion‑GAN for Synthetic Abdominal CT Generation

A concise PyTorch notebook that trains a lightweight Diffusion‑GAN to generate 128 × 128 synthetic abdominal CT slices from the CHAOS dataset (or any single‑channel CT dataset laid out as plain image files).

Features

Time‑conditioned U‑Net generator with sinusoidal embeddings

PatchGAN discriminator with spectral normalization

Mixed reconstruction, GAN, perceptual (VGG‑16), and MSE losses

Cosine noise schedule (1 000 steps) with progressive time‑window curriculum

Simple helper routines for training, inference, and image‑quality metrics (MAE, SSIM, PSNR)

