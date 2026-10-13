---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
title: "Embedded and Real-Time Systems"
description: "A planned series on the computers inside machines: microcontroller architecture, interrupts and DMA, on-board and in-vehicle buses, real-time operating systems and scheduling, and measuring timing."
category: "Computing Systems"
status: "planned"
objectives:
  - "Describe how a microcontroller's CPU, memory, timers, converters and peripherals work together."
  - "Choose between polling, interrupts and DMA for moving sensor data."
  - "Compare serial buses (UART, SPI, I2C, CAN) by topology, speed and error handling."
  - "Explain real-time scheduling and verify that deadlines are met by measurement."
plannedEntries:
  - title: "Inside a Microcontroller"
    description: "CPU, memory map, clocks, timers, analog-to-digital converters and general-purpose I/O, and how firmware drives them."
  - title: "Interrupts, Polling and DMA"
    description: "Three ways to move data between peripherals and memory, and how each affects latency and CPU load."
  - title: "Serial Buses: UART, SPI, I2C and CAN"
    description: "How each bus frames, addresses and checks data, and where each is used, from sensor boards to vehicles."
  - title: "Real-Time Operating Systems and Scheduling"
    description: "Tasks, priorities, synchronisation and the scheduling theory that says whether deadlines can be met."
  - title: "Measuring Timing, Latency and Resource Use"
    description: "Instrumenting embedded software to verify execution time, jitter and memory use on real hardware."
---

This series is planned and has not started publishing. It assumes basic C programming and digital logic. The outline below describes the intended scope and may change before any entry is written.
