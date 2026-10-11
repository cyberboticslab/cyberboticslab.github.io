---
title: Hierarchical Reinforcement Learning (HRL) for Safe Dynamic Legged Locomotion
display_title: Safe Learning for Legged Robots
overview: Walking policies must handle changing contacts, terrain, and disturbances. We combine structured control and reduced-order models with learning, then evaluate the resulting behavior in simulation and robot experiments.
hero_image_page: video/model-informed-safe-reinforcement-learning
hero_video: /video/model-informed-safe-reinforcement-learning/
hero_alt: Digit simulation used to demonstrate model-informed safe reinforcement learning.
hero_caption: Model-informed safe learning in Digit simulation · October 2026 lab video.
method_steps:
  - Structure policies with walking models
  - Learn control behavior in simulation
  - Evaluate performance and safety conditions
method_figure: true
method_figure_label: Explore the original project-goals diagram
summary: Model-informed learning methods for dynamic bipedal locomotion.
tags:
  - learning
  - humanoid
  - exoskeleton
date: '2022-04-15T00:00:00Z'
featured: true

image:
  caption: Illustration of proposed project goals.
  alt_text: Original project-goals diagram connecting inverse reinforcement learning, navigation, stepping, gait policies, and proposed robot transfer.
  focal_point: Smart
  preview_only: false

reading_time: false
profile: false
pager: true
lastmod: 2026-10-10
---

## The problem

Learning a locomotion policy must address changing contact dynamics, disturbances, and the gap between training and robot experiments. Safety properties also depend on the model and conditions under which they are derived.

## Our approach

We combine structured control policies and reduced-order walking models with reinforcement learning. Work includes cascade motion policies, compact terrain representations, and model-informed step-to-step prediction for safe learning.

## Results and experimental setting

- **Learned walking on hardware:** The cascade-policy work includes Digit walking experiments, with a linked lab demonstration.
- **Terrain-aware representations:** The TCST 2026 journal paper evaluates locomotion in high-fidelity simulation and reports preliminary hardware sensor comparisons.
- **Model-informed safe learning:** The 2026 study evaluates full-order Digit in MuJoCo, using step-to-step predictions to inform policy learning and runtime foot-placement filtering.

> **Safety conditions:** The safe-learning certificate applies to the reduced-order model under the paper's assumptions. Each study identifies its own training, simulation, and hardware evaluation conditions.

## Papers and demonstrations

- [Cascade motion policy design (IEEE Access, 2022)](/publication/castillo-2022-reinforcement/)
- [Terrain-aware locomotion representations (TCST 2026)](/publication/castillo-2025-terrain-aware/)
- [Model-informed safe reinforcement learning (2026)](/publication/paredes-2026-model-informed/)

[Watch model-informed safe learning](/video/model-informed-safe-reinforcement-learning/) and the earlier [learned Digit walking experiments](/video/digit-learning-to-walk-robustly/).
