---
title: "Digital Signal Processing for Engineers"
description: "A series on processing sampled signals: discrete-time signals and systems, the z-transform, frequency analysis with the DFT and FFT, digital filter design, and the step from signal processing to digital control."
category: "Mathematical Foundations"
status: "published"
objectives:
  - "Describe discrete-time signals and linear time-invariant systems by difference equations, impulse responses and convolution."
  - "Use the z-transform to analyze stability and frequency response."
  - "Compute and interpret spectra with the DFT and FFT, including leakage and windowing."
  - "Design FIR and IIR filters to a specification and implement them within hardware limits."
  - "Treat a digital control loop as a signal-processing system: discretize a plant and a controller, and account for the delays that sampling, holding and filtering add when choosing the sampling rate."
---

This series is for engineers who work with sampled signals and want the theory that lets them reason about what their code does to those signals. It assumes calculus, complex numbers and basic linear algebra, and the idea of sampling that the sensor series introduces; the worked examples use Python 3 with NumPy. In five entries it builds discrete-time signals and linear time-invariant systems from first principles, analyses them with the z-transform, measures spectra with the DFT and FFT, designs FIR and IIR filters within the limits of finite word length, and ends by placing a digital filter inside a feedback loop as a digital controller.
