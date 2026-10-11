---
title: Fast Robot Optimization and Simulation Toolkit (FROST)
display_title: FROST
overview: Dynamic walking requires models that capture motion and contact transitions. FROST brings hybrid-system modeling, constrained gait optimization, and simulation into an open-source MATLAB toolkit.
hero_alt: A collection of robot platforms associated with FROST modeling and optimization research.
hero_caption: Fast Robot Optimization and Simulation Toolkit.
resource_anchor: use-the-toolkit
method_steps:
  - Model hybrid robot dynamics
  - Optimize constrained trajectories
  - Simulate and evaluate the motion
summary: Open-source modeling, trajectory optimization, and simulation for hybrid robot dynamics.
tags:
  - planning
  - optimization
date: '2018-02-27T00:00:00Z'
featured: false

image:
  caption: Robot platforms that use FROST.
  focal_point: Smart
  preview_only: false

reading_time: false
profile: false
pager: true
lastmod: 2026-10-10
---

## The problem

Dynamic walking combines continuous motion with discrete contact transitions. Generating a gait requires a model that represents this hybrid structure and enforces the robot's dynamics and constraints.

## Our approach

FROST is an open-source MATLAB toolkit for hybrid-system modeling, trajectory optimization, and simulation. It represents discrete structure using directed graphs, supports symbolic model generation, and uses direct collocation to formulate constrained trajectory optimization problems.

## Results and experimental setting

The FROST paper describes gait synthesis for multiple bipedal models and presents simulation case studies. Optimization performance and deployment requirements depend on the model, formulation, solver, and computing environment.

## Use the toolkit

- [Code and installation requirements](https://github.com/ayonga/frost-dev)
- [Documentation](https://ayonga.github.io/frost-dev/)
- [Examples](https://github.com/ayonga/frost-dev/tree/master/example)
- [Paper and citation](/publication/hereid-2017-frost/)

Start with an example that matches your robot model and record the software version, solver settings, and problem formulation when reporting results.
