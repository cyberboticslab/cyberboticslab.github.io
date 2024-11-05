---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Real-Time Safe Bipedal Robot Navigation using Linear Discrete Control Barrier Functions
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
    Safe navigation in real-time is an essential task for humanoid robots in real-world deployment. Since humanoid robots are inherently underactuated thanks to unilateral ground contacts, a path is considered safe if it is obstacle-free and respects the robot's physical limitations and underlying dynamics. Existing approaches often decouple path planning from gait control due to the significant computational challenge caused by the full-order robot dynamics. In this work, we develop a unified, safe path and gait planning framework that can be evaluated online in real-time, allowing the robot to navigate clustered environments while sustaining stable locomotion. Our approach uses the popular Linear Inverted Pendulum (LIP) model as a template model to represent walking dynamics. It incorporates heading angles in the model to evaluate kinematic constraints essential for physically feasible gaits properly. In addition, we leverage discrete control barrier functions (DCBF) for obstacle avoidance, ensuring that the subsequent foot placement provides a safe navigation path within clustered environments. To guarantee real-time computation, we use a novel approximation of the DCBF to produce linear DCBF (LDCBF) constraints. We validate the proposed approach in simulation using a Digit robot in randomly generated environments. The results demonstrate that our approach can generate safe gaits for a non-trivial humanoid robot to navigate environments with randomly generated obstacles in real-time. 
publication: '*Submitted to 2025 IEEE International Conference on Robotics and Automation (ICRA)*'
---

{{< youtube ES-Fmx3TOQs>}}