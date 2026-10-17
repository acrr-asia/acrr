---
title: "Motion Planning for Robots"
description: "A five-entry course on how a robot finds a collision-free motion: configuration space, graph search, sampling-based planners, trajectories and path tracking."
category: "Robotics and Control"
status: "published"
objectives:
  - "State a motion planning problem in configuration space, and explain how obstacles in the workspace become obstacles in configuration space."
  - "Plan on a grid or graph with Dijkstra's algorithm and A*, and explain when a heuristic keeps A* optimal."
  - "Explain how probabilistic roadmaps and rapidly-exploring random trees find paths in high-dimensional spaces, and what their completeness and optimality guarantees mean."
  - "Turn a geometric path into a trajectory that respects velocity and acceleration limits."
  - "Follow a planned path on a mobile robot with a tracking controller, and avoid obstacles that the plan did not know about."
---

This series is for engineers and students who want to understand how a robot decides where to move: a mobile robot crossing a room, or an arm reaching around an obstacle. It continues the [Introduction to Robotics](/series/introduction-to-robotics) series, which ends by naming motion planning as one of the topics that build on frames, kinematics and state estimation. It assumes the two-link planar arm and the coordinate frames of that series, basic linear algebra and calculus, and the ability to read Python. The idea of feedback comes from the [Foundations of Control Systems](/series/foundations-of-control-systems) series and is used in the last entry.

The order follows the question a planner answers, from the most abstract statement to the robot's wheels. The first entry states the problem in configuration space, where a robot of any shape becomes a point and its obstacles become regions to avoid. The second entry discretizes that space into a graph and searches it with Dijkstra's algorithm and A*, which find the cheapest path on that graph and are practical when the space has few dimensions. The third entry handles spaces with many dimensions, such as those of a robot arm, with planners that sample configurations at random instead of covering the space with a grid. A planner returns a geometric path, so the fourth entry adds time: velocity and acceleration profiles that a robot can follow. The fifth entry closes the loop, with controllers that track the plan on a mobile robot and with reactive methods that avoid obstacles the plan did not know about.

The series treats static obstacles and plans geometry first and timing second; it does not treat planning with dynamics or differential constraints (kinodynamic planning), trajectory optimization beyond a mention in the first entry, moving obstacles or tracking control of arms.

All entries share a few conventions. Units are SI, angles are in radians in every computation, and coordinate frames are right-handed, as in the Introduction to Robotics series. A configuration is written $q$, the configuration space $\mathcal{C}$, its free part $\mathcal{C}_{\mathrm{free}}$ and its obstacle region $\mathcal{C}_{\mathrm{obs}}$. The dimension of $\mathcal{C}$ is $d$; a path is $\sigma : [0, 1] \to \mathcal{C}_{\mathrm{free}}$, and a trajectory is $q(t) = \sigma(s(t))$ with a time scaling $s(t)$. The examples use a point or disk robot in a plane, the two-link arm with link lengths $l_1 = 1.0$ m and $l_2 = 0.7$ m from the Introduction to Robotics series, and a differential-drive mobile robot. The code is Python 3.13 with NumPy 2.5, and every quoted output comes from running it; results that depend on random sampling state the random seed.
