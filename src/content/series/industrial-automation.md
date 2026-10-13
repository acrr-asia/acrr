---
title: "Industrial Automation"
description: "A series on automating physical processes: logic and sequential control, programmable logic controllers, fieldbuses and industrial Ethernet, PID control of process variables, and networked automation with digital twins."
category: "Engineering"
status: "published"
objectives:
  - "Express control tasks as Boolean logic and as sequential, state-based programs."
  - "Describe how a programmable logic controller executes a program, and the languages defined for it."
  - "Compare fieldbus and industrial Ethernet systems by timing, topology and determinism."
  - "Tune PID loops for typical process variables such as temperature, level, flow and pressure."
---

This series is for readers with basic electrical engineering (voltage, current, switches and relays) who want to understand how physical processes are automated. It assumes no prior knowledge of digital logic or programmable controllers; the entry on PID control also uses the feedback ideas of the control systems series. It moves from the bottom of a plant upward: Boolean logic, latches, timers and state machines; the programmable logic controller, its scan cycle, its inputs and outputs and the IEC 61131-3 languages; the fieldbuses and industrial Ethernet networks that connect controllers to devices with bounded delay; PID control of temperature, level, flow and pressure, including tuning and the practical problems of real loops; and finally the connection of automation systems to higher-level systems through ISA-95 and OPC UA, and digital twins that run alongside the plant. Worked examples are checked with short Python programs.
