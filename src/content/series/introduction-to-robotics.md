---
# Authoring note: when a planned entry is written, publish it as an article in
# src/content/blog (with `series` and `seriesOrder`) and remove it from plannedEntries.
# Remove it from the Vietnamese translation (src/content/series/vi/introduction-to-robotics.md) as well.
title: "Introduction to Robotics"
description: "A series that introduces robots as systems of structure, actuation, sensing, and computation connected by feedback."
category: "Robotics and Control"
status: "published"
objectives:
  - "Describe a robot as mechanical structure, actuators, sensors, and computation connected by a control loop."
  - "Represent the position and orientation of rigid bodies using coordinate frames and rotation matrices."
  - "Explain forward and inverse kinematics for a simple planar arm."
  - "Outline the sense, plan, and act structure used in many robot software architectures."
  - "Explain why a robot must estimate its state, and how a Kalman filter combines a motion model with noisy measurements."
---

This series is intended for readers who are comfortable with basic linear algebra, trigonometry and calculus (derivatives), and who have met torque and inertia in introductory mechanics. The probability it needs is introduced where it is used. It starts from what a robot is and works down to the geometry, kinematics and estimation that every robot depends on.
