---
publication_year: 2024
publication_short: "arXiv preprint"
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Unified path and gait planning for safe bipedal robot navigation"
subtitle: ''
summary: "Unified path and gait planning evaluated in Digit simulation with randomly generated obstacles."
authors: ["Chengyang Peng", "Victor Paredes", "Ayonga Hereid"]
tags: 
- control barrier function
- path planning
categories: []
date: "2024-03-26"
lastmod: "2026-10-10"
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
publication_types: ["3"]
abstract: 
    Safe path and gait planning are essential for bipedal robots to navigate complex real-world environments. The prevailing approaches often plan the path and gait separately in a hierarchical fashion, potentially resulting in unsafe movements due to neglecting the physical constraints of walking robots. A safety-critical path must not only avoid obstacles but also ensure that the robot's gaits are subject to its dynamic and kinematic constraints. This work presents a novel approach that unifies path planning and gait planning via a Model Predictive Control (MPC) using the Linear Inverted Pendulum (LIP) model representing bipedal locomotion. This approach considers environmental constraints, such as obstacles, and the robot's kinematics and dynamics constraints. By using discrete-time Control Barrier Functions for obstacle avoidance, our approach generates the next foot landing position, ensuring robust walking gaits and a safe navigation path within clustered environments. We validated our proposed approach in simulation using a Digit robot in 20 randomly created environments. The results demonstrate improved performance in terms of safety and robustness when compared to hierarchical path and gait planning frameworks. 
publication: "arXiv preprint arXiv:2403.17347"
---

{{< youtube ES-Fmx3TOQs>}}