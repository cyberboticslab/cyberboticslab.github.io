---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Robust feedback motion policy design using reinforcement learning on a 3d digit
  bipedal robot
subtitle: ''
summary: ''
authors:
- Guillermo A Castillo
- Bowen Weng
- Wei Zhang
- Ayonga Hereid
tags: []
categories: []
date: '2021-10-01'
lastmod: 2023-08-01T13:49:27-04:00
featured: false
draft: false

url_video: https://youtu.be/j8KbW-a9dbw
links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/9636467

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
projects: ["hierarchical-reinforcement-learning"]
publishDate: '2023-08-01T17:49:27.355710Z'
publication_types:
- '1'
abstract: 
  In this paper, a hierarchical and robust framework for learning bipedal locomotion is presented and successfully implemented on the 3D biped robot Digit built by Agility Robotics. We propose a cascade-structure controller that combines the learning process with intuitive feedback regulations. This design allows the framework to realize robust and stable walking with a reduced-dimensional state and action spaces of the policy, significantly simplifying the design and increasing the sampling efficiency of the learning method. The inclusion of feedback regulation into the framework improves the robustness of the learned walking gait and ensures the success of the sim-to-real transfer of the proposed controller with minimal tuning. We specifically present a learning pipeline that considers hardware-feasible initial poses of the robot within the learning process to ensure the initial state of the learning is replicated as close as possible to the initial state of the robot in hardware experiments. Finally, we demonstrate the feasibility of our method by successfully transferring the learned policy in simulation to the Digit robot hardware, realizing sustained walking gaits under external force disturbances and challenging terrains not incurred during the training process. To the best of our knowledge, this is the first time a learning-based policy is transferred successfully to the Digit robot in hardware experiments.
publication: '*2021 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)*'
---

{{< youtube j8KbW-a9dbw >}}