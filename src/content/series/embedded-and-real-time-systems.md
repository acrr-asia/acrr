---
title: "Embedded and Real-Time Systems"
description: "A series on the computers inside machines: microcontroller architecture, interrupts and DMA, on-board and in-vehicle buses, real-time operating systems and scheduling, and measuring timing."
category: "Computing Systems"
status: "published"
objectives:
  - "Describe how a microcontroller's CPU, memory, timers, converters and peripherals work together."
  - "Choose between polling, interrupts and DMA for moving sensor data."
  - "Compare serial buses (UART, SPI, I2C, CAN) by topology, speed and error handling."
  - "Explain real-time scheduling and verify that deadlines are met by measurement."
---

This series is for readers who know basic C programming (types, pointers, structures and bitwise operators) and basic digital logic (binary and hexadecimal numbers, gates, flip-flops and clocks), and who want to understand the small computers that control machines. It starts from the vocabulary of real-time systems (deadlines, latency and jitter) and the parts of a microcontroller, then follows data from peripherals into memory by polling, interrupts and DMA, and between chips and controllers over UART, SPI, I2C and CAN. It then shows how a real-time operating system organizes firmware into prioritized tasks and how scheduling analysis predicts whether every deadline is met, and ends by measuring execution time, latency, jitter, processor load and memory use on real hardware to check those predictions. Examples are in C11 for a generic 32-bit Arm Cortex-M class microcontroller, with calculations in Python.
