---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Template model inspired task space learning for robust bipedal locomotion
subtitle: ''
summary: ''
authors:
- Guillermo A Castillo
- Bowen Weng
- Shunpeng Yang
- Wei Zhang
- Ayonga Hereid
tags: 
- reinforcement learning
- template model
- whole body control
categories: []
date: '2023-10-01'
lastmod: 2023-09-15T13:49:28-04:00
featured: true
draft: false

url_video: https://youtu.be/YTjMgGka4Ig?si=ryb5Cb7ePW4Xy3fZ

links:
- name: arXiv
  url: https://arxiv.org/abs/2309.15442

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
projects: []
publishDate: '2023-10-01T17:49:27.912459Z'
publication_types:
- '1'
abstract: 
  This work presents a hierarchical framework for bipedal locomotion that combines a Reinforcement Learning (RL)-based high-level (HL) planner policy for the online generation of task space commands with a model-based low-level (LL) controller to track the desired task space trajectories. Different from traditional end-to-end learning approaches, our HL policy takes insights from the angular momentum-based linear inverted pendulum (ALIP) to carefully design the observation and action spaces of the Markov Decision Process (MDP). This simple yet effective design creates an insightful mapping between a low-dimensional state that effectively captures the complex dynamics of bipedal locomotion and a set of task space outputs that shape the walking gait of the robot. The HL policy is agnostic to the task space LL controller, which increases the flexibility of the design and generalization of the framework to other bipedal robots. This hierarchical design results in a learning-based framework with improved performance, data efficiency, and robustness compared with the ALIP model-based approach and state-of-the-art learning-based frameworks for bipedal locomotion. The proposed hierarchical controller is tested in three different robots, Rabbit, a five-link underactuated planar biped; Walker2D, a seven-link fully-actuated planar biped; and Digit, a 3D humanoid robot with 20 actuated joints. The trained policy naturally learns human-like locomotion behaviors and is able to effectively track a wide range of walking speeds while preserving the robustness and stability of the walking gait even under adversarial conditions. 
publication: '*IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*'
---

{{< youtube YTjMgGka4Ig >}}