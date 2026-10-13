---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
# Remove it from the Vietnamese translation (src/content/series/vi/introduction-to-robotics.md) as well.
title: "Introduction to Robotics"
description: "Learn how a robot is built and reasoned about: its subsystems, the geometry of frames, arm kinematics and estimating its state from noisy sensors."
category: "Robotics and Control"
status: "published"
objectives:
  - "Describe a robot as mechanical structure, actuators, sensors, and computation connected by a control loop."
  - "Represent the position and orientation of rigid bodies using coordinate frames and rotation matrices."
  - "Explain forward and inverse kinematics for a simple planar arm."
  - "Outline the sense, plan, and act structure used in many robot software architectures."
  - "Explain why a robot must estimate its state, and how a Kalman filter combines a motion model with noisy measurements."
---

This series is intended for readers who are comfortable with basic linear algebra, trigonometry and calculus (derivatives), and who have met torque and inertia in introductory mechanics. The probability it needs is introduced in the last entry, where it is used. No earlier robotics is assumed; the idea of feedback is taken from the [Foundations of Control Systems](/series/foundations-of-control-systems) series, but the entries can be read without it.

The four entries go from the whole machine to the mathematics that every robot depends on, in the order in which each idea becomes necessary:

1. **What a robot is.** A robot as mechanical structure, actuation, sensing and computation joined by feedback loops that run at different rates, and the main ways its software is organized. This entry fixes the vocabulary (degrees of freedom, redundancy, proprioceptive and exteroceptive sensing) used by the others.
2. **Coordinate frames and transformations.** Before any part of a robot can be located, positions and orientations need a precise language: rotation matrices, Euler angles, quaternions, homogeneous transformations and the frame tree.
3. **Kinematics of a planar arm.** The transformations of entry 2 applied to a two-link arm, in both directions: forward kinematics, closed-form and numerical inverse kinematics, the Jacobian and singular configurations.
4. **Sensing and state estimation.** Entries 2 and 3 assume that joint angles and poses are known; this entry explains how a robot estimates them from noisy, delayed measurements, with a worked Kalman filter.

The entries share their conventions: SI units, right-handed coordinate frames, column vectors, and angles in radians in every computation (examples show degrees for readability). The worked examples are small enough to check by hand.
