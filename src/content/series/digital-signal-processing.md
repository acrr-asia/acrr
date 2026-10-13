---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
# Remove it from the Vietnamese translation (src/content/series/vi/digital-signal-processing.md) as well.
title: "Digital Signal Processing for Engineers"
description: "A planned series on processing sampled signals: discrete-time signals and systems, the z-transform, frequency analysis with the DFT and FFT, digital filter design, and the step from signal processing to digital control."
category: "Mathematical Foundations"
status: "planned"
objectives:
  - "Describe discrete-time signals and linear time-invariant systems by difference equations, impulse responses and convolution."
  - "Use the z-transform to analyse stability and frequency response."
  - "Compute and interpret spectra with the DFT and FFT, including leakage and windowing."
  - "Design FIR and IIR filters to a specification and implement them within hardware limits."
plannedEntries:
  - title: "Signals and Systems in Discrete Time"
    description: "Sequences, difference equations, impulse response, convolution and the properties that make linear time-invariant systems tractable."
  - title: "The z-Transform, Poles and Stability"
    description: "From difference equations to transfer functions, pole-zero plots and bounded-input bounded-output stability."
  - title: "Spectra: The DFT and the FFT"
    description: "What the discrete Fourier transform computes, why the FFT is fast, and how leakage and windowing affect a measured spectrum."
  - title: "Designing FIR and IIR Filters"
    description: "Window and bilinear-transform design methods, linear phase, and the effects of finite word length."
  - title: "From Signal Processing to Digital Control"
    description: "Discretising a controller, sampling-rate choices, and why a control loop is a signal-processing system with feedback."
---

This series is planned and has not started publishing. It assumes calculus, complex numbers and basic linear algebra. The outline below describes the intended scope and may change before any entry is written.
