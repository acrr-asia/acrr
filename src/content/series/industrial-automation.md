---
title: "Industrial Automation"
description: "A five-entry series on automating physical processes, from Boolean logic and PLCs through fieldbuses and PID loops to OPC UA and digital twins."
category: "Engineering"
status: "published"
objectives:
  - "Express control tasks as Boolean logic and as sequential, state-based programs."
  - "Describe how a programmable logic controller executes a program, and the languages defined for it."
  - "Compare fieldbus and industrial Ethernet systems by timing, topology and determinism."
  - "Tune PID loops for typical process variables such as temperature, level, flow and pressure."
  - "Explain how plant data reach higher-level systems through the ISA-95 levels and OPC UA, and how a digital twin uses residuals to detect faults."
---

This series is for readers with basic electrical engineering (voltage, current, switches and relays) who want to understand how physical processes are automated. It assumes no prior knowledge of digital logic or programmable controllers. The entry on proportional–integral–derivative (PID) control also uses the feedback ideas of the Foundations of Control Systems series.

The entries build a plant's automation from the bottom up, and each one relies on the one before it. The first develops the logic of automation: Boolean functions, latches, timers, counters and state machines. The second describes the programmable logic controller (PLC) that executes that logic: its scan cycle, its digital and 4–20 mA inputs and outputs, and the IEC 61131-3 languages. The third extends the PLC's input and output timing across fieldbuses and industrial Ethernet, which connect controllers to devices with bounded delay. The fourth closes continuous feedback loops through those inputs and outputs, with PID control of temperature, level, flow and pressure, including tuning and the practical problems of real loops. The fifth looks upward: how the ISA-95 levels and OPC UA connect the control layer to higher-level systems, how that connection is secured, and how a digital twin running alongside the plant can estimate what no instrument measures.

The entries share three conventions. The programming examples follow the third edition of IEC 61131-3 (2013), and the second entry notes what the 2025 edition changes. The fourth entry expresses process signals and controller outputs in percent of span, as process control systems display them. Worked examples are checked with short Python 3 programs that use only the standard library, and their real output is shown.
