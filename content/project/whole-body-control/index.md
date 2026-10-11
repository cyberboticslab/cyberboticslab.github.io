---
title: Safe Task Space Controller for Underactuated Robotic Systems
display_title: Whole-Body Control
overview: A humanoid must balance while coordinating many competing motion tasks. We formulate controllers that account for dynamics, contacts, actuator limits, and model-based safety constraints.
hero_image_page: video/safe-whole-body-task-space-control
hero_video: /video/safe-whole-body-task-space-control/
hero_alt: Lab demonstration of whole-body task-space control for a humanoid robot.
hero_caption: Whole-body task-space control · Digit simulation and hardware experiments.
method_steps:
  - Define balance and motion tasks
  - Enforce dynamics and contact constraints
  - Compute whole-body control inputs
method_figure: true
method_figure_label: Explore the controller illustration
summary: Task-space control with dynamic, contact, and safety constraints for humanoid robots.
tags:
  - learning
  - control
date: '2021-06-01T00:00:00Z'
featured: false

image:
  caption: 
  focal_point: Smart
  preview_only: false

reading_time: false
profile: false
pager: true
lastmod: 2026-10-10
---

## The problem

A humanoid controller must coordinate balance and motion while respecting actuator limits, unilateral contacts, friction, and closed kinematic chains. Competing tasks can drive the robot toward undesirable configurations.

## Our approach

We formulate inverse-dynamics quadratic programs with task-space objectives and control barrier functions. Related foot-placement work accounts for periodically swaying ground using a time-varying reduced-order model.

## Results and experimental setting

Safe whole-body task-space control was evaluated on Digit in simulation and hardware experiments. Swaying-ground foot-placement control was also tested in both settings. The mathematical results apply under the models and sufficient conditions stated in each paper; the experiments cover the reported tasks and disturbances.

## Papers and demonstrations

- [Safe whole-body task-space control (ACC 2024)](/publication/paredes-2024-safe/)
- [Walking on swaying rigid surfaces](/publication/gao-2024-time/)

[Watch the whole-body control experiments](/video/safe-whole-body-task-space-control/) and [the swaying-ground experiments](https://www.youtube.com/watch?v=NtAT0DFtMCY).
