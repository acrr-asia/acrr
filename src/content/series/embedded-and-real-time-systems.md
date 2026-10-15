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

This series is for readers who know basic C programming (types, pointers, structures and bitwise operators) and basic digital logic (binary and hexadecimal numbers, gates, flip-flops and clocks), and who want to understand the small computers that control machines. It assumes no prior embedded experience. It treats single-core microcontrollers; multicore scheduling, embedded Linux, the API of any particular kernel, circuit design and safety certification are outside its scope.

The entries follow data through an embedded system and then turn to the question of time. The first entry defines the timing vocabulary of the whole series (events, deadlines, latency and jitter) and the parts of a microcontroller, and ends with the simplest firmware structure, the superloop, in which every event waits for the rest of the loop. The second analyzes the polling that the superloop performs and shows how interrupts and direct memory access (DMA) let hardware events be handled when they occur, with what each method costs in latency and processor time. The third follows data off the chip over four serial buses: the universal asynchronous receiver-transmitter (UART), the Serial Peripheral Interface (SPI), Inter-Integrated Circuit (I2C) and the Controller Area Network (CAN).

The fourth entry removes the limit the second leaves, processing that still runs in one loop, by organizing it into prioritized tasks under a real-time operating system, and calculates whether every deadline is met in the worst case. The fifth measures execution time, latency, jitter, processor load and memory use on real hardware, and checks the calculation against those measurements.

Shared conventions: code is C11 for a generic 32-bit Arm Cortex-M class microcontroller at 48 MHz, with peripheral register layouts invented for illustration; desktop examples use the Portable Operating System Interface (POSIX); calculations are in Python 3 with the standard library. Time uses SI prefixes and memory sizes use binary prefixes (1 KiB = 1024 bytes).
