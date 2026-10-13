---
title: "Digital Signal Processing for Engineers"
description: "How to analyze sampled signals and systems with the z-transform and the DFT, design digital filters and carry the same tools into digital control."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Describe discrete-time signals and linear time-invariant systems by difference equations, impulse responses and convolution."
  - "Use the z-transform to analyze stability and frequency response."
  - "Compute and interpret spectra with the DFT and FFT, including leakage and windowing."
  - "Design FIR and IIR filters to a specification and implement them within hardware limits."
  - "Treat a digital control loop as a signal-processing system: discretize a plant and a controller, and account for the delays that sampling, holding and filtering add when choosing the sampling rate."
---

This series is for engineers who work with sampled signals and want the theory that lets them reason about what their code does to those signals. It assumes calculus, complex numbers and basic linear algebra, and the idea of sampling that [Sampling, Quantization and Data Conversion](/blog/sampling-quantization-and-data-conversion) introduces in the [Sensor Systems](/series/sensor-systems) series. The worked examples use Python 3 with NumPy.

The five entries are ordered so that each uses the tools of the one before. The first builds discrete-time signals and linear time-invariant (LTI) systems from first principles, in the time domain: difference equations, impulse responses and convolution. The second introduces the z-transform, which replaces those time-domain sums with algebra and reads stability and frequency response from the positions of poles and zeros. The third turns from systems to signals and measures spectra with the discrete Fourier transform (DFT) and the fast Fourier transform (FFT). The fourth combines all three to design finite and infinite impulse response (FIR and IIR) filters within the limits of finite word length. The fifth places a digital filter inside a feedback loop as a digital controller and treats the whole loop as a signal-processing system.

All entries share the notation table of the first entry: frequency in radians per sample, a single sign convention for difference equations and the assumption that systems start at rest.
