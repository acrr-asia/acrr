---
title: "Embedded and Real-Time Systems"
description: "Follow data through the small computers inside machines, from microcontroller hardware and serial buses to real-time scheduling and timing measurement."
category: "Computing Systems"
status: "published"
objectives:
  - "Describe how a microcontroller's CPU, memory, timers, converters and peripherals work together."
  - "Choose between polling, interrupts and DMA for moving sensor data."
  - "Compare serial buses (UART, SPI, I2C, CAN) by topology, speed and error handling."
  - "Explain real-time scheduling, calculate worst-case response times and check them against measurements."
---

This series is for readers who know basic C programming (types, pointers, structures and bitwise operators) and basic digital logic (binary and hexadecimal numbers, gates, flip-flops and clocks), and who want to understand the small computers that control machines. It assumes no prior embedded experience.

The entries follow data through an embedded system and then turn to the question of time, each one removing a limit that the previous one exposes. The first entry defines the timing vocabulary of the whole series (events, deadlines, latency and jitter) and the parts of a microcontroller, and ends with the simplest firmware structure, the superloop, whose events wait for each other. The second replaces that waiting with polling, interrupts and direct memory access (DMA), and shows what each costs in latency and processor time. The third follows data off the chip over four serial buses: the universal asynchronous receiver-transmitter (UART), the Serial Peripheral Interface (SPI), Inter-Integrated Circuit (I2C) and the Controller Area Network (CAN). The fourth organizes the processing into prioritized tasks under a real-time operating system and calculates whether every deadline is met in the worst case. The fifth measures execution time, latency, jitter, processor load and memory use on real hardware, and checks the calculation against those measurements.

Shared conventions: code is C11 for a generic 32-bit Arm Cortex-M class microcontroller at 48 MHz, with peripheral register layouts invented for illustration; desktop examples use the Portable Operating System Interface (POSIX); calculations are in Python 3 with the standard library. Time uses SI prefixes and memory sizes use binary prefixes (1 KiB = 1024 bytes).
