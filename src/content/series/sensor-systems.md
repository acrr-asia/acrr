---
title: "Sensor Systems"
description: "Follow a measurement from a physical quantity to a trustworthy number: sensing, signal conditioning, conversion, noise, smart sensors, calibration and fusion."
category: "Engineering"
status: "published"
objectives:
  - "Describe a measurement system as a chain from measurand to number, and characterize a sensor by its static and dynamic properties."
  - "Explain the main physical principles by which sensors convert a quantity into an electrical signal."
  - "Design the analog front end of a sensor: excitation, bridges, amplification and filtering."
  - "Explain sampling, quantization and data conversion, and the noise that limits what can be detected."
  - "State and combine measurement uncertainties, and calibrate and fuse sensors."
---

The series is written for readers who are comfortable with basic circuit analysis (Ohm's law, voltage dividers), calculus and elementary statistics. It follows a measurement from the physical world to a number that can be trusted, and its order is the order of the measurement chain that the first entry sets out.

The first entry supplies the vocabulary that every later entry uses: measurand, sensor characteristics, error and uncertainty. The next four entries follow the signal stage by stage. The sensing principles come first, then the analog signal conditioning that makes a small sensor signal measurable, then sampling and analog-to-digital conversion, and then the noise and interference that limit what the whole chain can detect. The sixth entry shows how smart sensors and microelectromechanical systems (MEMS) build that chain in a single package. The last entry closes the loop with calibration, which makes a channel's numbers traceable, and with the fusion of several imperfect sensors into one better estimate.

Two examples run through the series. A PT100 platinum resistance thermometer illustrates nonlinearity in the first entry, excitation and lead-wire errors in the third and calibration-curve fitting in the last. A load-cell weighing channel is designed in the third entry, digitized in the fourth, given a noise budget in the fifth and calibrated in the seventh.

Units are SI, with accelerations also given in multiples of the standard gravity *g* and bridge outputs in millivolts per volt. The terms for measurement and uncertainty follow the *International Vocabulary of Metrology* (VIM) and the *Guide to the Expression of Uncertainty in Measurement* (GUM), as the first entry explains. Noise voltages and currents are root-mean-square values, computed at 300 K unless stated otherwise. The code examples of the last entry use Python 3 with NumPy.
