---
title: Perceptive Humanoid Locomotion and Autonomous Navigation
display_title: Perceptive Locomotion & Navigation
overview: A humanoid must choose where to go and where to step. We connect terrain perception, reduced-order walking models, and constrained planning to make those decisions together.
hero_image_page: video/perceptive-variable-timing-footstep-planning
hero_video: /video/perceptive-variable-timing-footstep-planning/
hero_alt: Digit hardware validation on separated wooden platforms, shown in the October 2026 lab video.
hero_caption: Perceptive footstep planning on Digit hardware · October 2026 lab video.
method_steps:
  - Identify paths and steppable terrain
  - Plan footsteps, subgoals, and timing
  - Coordinate walking and navigation
method_figure: true
method_figure_label: Explore the planning framework
summary: Perception-aware footstep planning and navigation for humanoid robots.
tags:
  - perception
  - planning
  - learning
  - humanoid
date: "2023-04-27T00:00:00Z"
featured: true

# Optional external URL for project (replaces project detail page).
# external_link: https://example.org

image:
  caption: Digit locomotion and navigation research.
  focal_point: Smart
  preview_only: false

reading_time: false
profile: false
pager: true
# show_related: true
# show_breadcrumb: true
lastmod: 2026-10-10
---

## The problem

A walking robot must choose steps that respect both its dynamics and the environment. Obstacle-free paths can still demand infeasible foot placements, and disconnected footholds leave little room for timing errors.

## Our approach

We connect reduced-order walking models with constrained planning. This includes joint path and gait planning with control barrier functions, adaptive step duration for restricted footholds, and depth-based construction of steppable regions.

## Results and experimental setting

- **Footstep planning:** The adaptive-timing and perceptive-planning manuscripts evaluate Digit in simulation, including restricted footholds, depth sensing, and stepping-stone layouts.
- **Navigation:** The linked studies connect path or subgoal selection with a walking planner and evaluate obstacle-navigation scenarios in simulation.
- **Recent lab demonstrations:** The October 2026 videos show Digit hardware demonstrations of perceptive stepping and learned-subgoal navigation. These later clips are presented alongside the original papers' reported evaluations.

> **Scope:** Results describe the models, terrain, obstacles, and experimental conditions in the linked studies and demonstrations.

## Papers and demonstrations

- [Perceptive variable-timing footstep planning (2026 preprint)](/publication/xiang-2026-perceptive/)
- [Learning navigation with dynamic subgoals (2025 preprint)](/publication/peng-2025-reinforcement/)
- [Adaptive step duration (IROS 2025)](/publication/xiang-2024-adaptive/)
- [Real-time safe navigation (ICRA 2025)](/publication/peng-2024-real/)
- [Unified path and gait planning (2024 preprint)](/publication/peng-2024-unified/)

[Watch perceptive footstep planning](/video/perceptive-variable-timing-footstep-planning/) and [learned-subgoal navigation](/video/dynamic-subgoal-navigation/). The earlier [adaptive-timing simulation](https://youtu.be/DjH69m1kbnM) shows the planning method on restricted footholds.
