---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Unified Path and Gait Planning for Safe Bipedal Robot Navigation
subtitle: ''
summary: ''
authors:
- Chengyang Peng
- Victor Paredes
- Guillermo A Castillo
- Ayonga Hereid
tags: 
- control barrier function
- path planning
categories: []
date: '2024-09-01'
lastmod: 2023-09-01T13:49:29-04:00
featured: false
draft: false

links:
- name: arXiv
  url: https://arxiv.org/abs/2403.17347

url_video: 'https://youtu.be/ES-Fmx3TOQs'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["perceptive-locomotion"]
publishDate: '2024-08-01T17:49:29.313793Z'
publication_types:
- '3'
abstract: 
    Safe path and gait planning are essential for bipedal robots to navigate complex real-world environments. The prevailing approaches often plan the path and gait separately in a hierarchical fashion, potentially resulting in unsafe movements due to neglecting the physical constraints of walking robots. A safety-critical path must not only avoid obstacles but also ensure that the robot's gaits are subject to its dynamic and kinematic constraints. This work presents a novel approach that unifies path planning and gait planning via a Model Predictive Control (MPC) using the Linear Inverted Pendulum (LIP) model representing bipedal locomotion. This approach considers environmental constraints, such as obstacles, and the robot's kinematics and dynamics constraints. By using discrete-time Control Barrier Functions for obstacle avoidance, our approach generates the next foot landing position, ensuring robust walking gaits and a safe navigation path within clustered environments. We validated our proposed approach in simulation using a Digit robot in 20 randomly created environments. The results demonstrate improved performance in terms of safety and robustness when compared to hierarchical path and gait planning frameworks. 
publication: '*Submitted to 2025 IEEE International Conference on Robotics and Automation (ICRA)*'
---

{{< youtube ES-Fmx3TOQs>}}