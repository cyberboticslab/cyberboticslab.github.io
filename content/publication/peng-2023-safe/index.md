---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Safe Bipedal Path Planning via Control Barrier Functions for Polynomial Shape
  Obstacles Estimated Using Logistic Regression
subtitle: ''
summary: ''
authors:
- Chengyang Peng
- Octavian Donca
- Guillermo Castillo
- Ayonga Hereid
tags: []
categories: []
date: '2023-01-01'
lastmod: 2023-08-01T13:49:29-04:00
featured: false
draft: false

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/10160671

url_video: 'https://youtu.be/r_hkuK5cMw4?si=28I-RzWm5TYgS7eT'

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
publishDate: '2023-08-01T17:49:29.313793Z'
publication_types:
- '1'
abstract: 
    Safe path planning is critical for bipedal robots to operate in safety-critical environments. Common path planning algorithms, such as RRT or RRT*, typically use geometric or kinematic collision check algorithms to ensure collision-free paths toward the target position. However, such approaches may generate non-smooth paths that do not comply with the dynamics constraints of walking robots. It has been shown that the control barrier function (CBF) can be integrated with RRT/RRT*to synthesize dynamically feasible collision-free paths. Yet, existing work has been limited to simple circular or elliptical shape obstacles due to the challenging nature of constructing appropriate barrier functions to represent irregularly shaped obstacles. In this paper, we present a CBF-based RRT* algorithm for bipedal robots to generate a collision-free path through space with multiple polynomial-shaped obstacles. In particular, we used logistic regression to construct polynomial barrier functions from a grid map of the environment to represent irregularly shaped obstacles. Moreover, we developed a multi-step CBF steering controller to ensure the efficiency of free space exploration. The proposed approach was first validated in simulation for a differential drive model, and then experimentally evaluated with a 3D humanoid robot, Digit, in a lab setting with randomly placed obstacles.
publication: '*2023 IEEE International Conference on Robotics and Automation (ICRA)*'
---

{{< youtube r_hkuK5cMw4>}}