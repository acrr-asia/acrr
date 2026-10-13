---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
title: "Sensor Systems"
description: "A series on the measurement chain, from a physical quantity to a trustworthy number: what a measurement is, how sensors convert physical effects into signals, and how those signals are conditioned, converted, cleaned, calibrated and combined."
category: "Engineering"
status: "in-progress"
objectives:
  - "Describe a measurement system as a chain from measurand to number, and characterise a sensor by its static and dynamic properties."
  - "Explain the main physical principles by which sensors convert a quantity into an electrical signal."
  - "Design the analog front end of a sensor: excitation, bridges, amplification and filtering."
  - "Explain sampling, quantization and data conversion, and the noise that limits what can be detected."
  - "State and combine measurement uncertainties, and calibrate and fuse sensors."
plannedEntries:
  - title: "Signal Conditioning: Bridges, Amplifiers and Analog Filters"
    description: "Excitation, Wheatstone bridges, operational and instrumentation amplifiers, and filters that prepare a sensor signal for conversion."
  - title: "Sampling, Quantization and Data Conversion"
    description: "The sampling theorem, aliasing and anti-aliasing filters, quantization error, and how analog-to-digital converters work."
  - title: "Noise, Interference and the Limits of Detection"
    description: "Thermal, shot and flicker noise, interference and grounding, and how noise sets the smallest change a sensor system can detect."
  - title: "Smart Sensors and MEMS"
    description: "Microfabricated sensors, on-chip conditioning and self-calibration, and what changes when a sensor carries its own electronics."
  - title: "Calibration and Multisensor Fusion"
    description: "Calibration and traceability in practice, and combining several imperfect sensors into one better estimate."
---

This series is intended for readers who are comfortable with basic circuit analysis (Ohm's law, voltage dividers), calculus and elementary statistics. It starts with what a measurement is and follows the signal from the physical world to a number that can be trusted. Entries not yet written are listed as planned, and the outline may change as they are written.
