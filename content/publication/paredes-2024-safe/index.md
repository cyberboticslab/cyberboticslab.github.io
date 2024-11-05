---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Safe Whole-Body Task Space Control for Humanoid Robots
subtitle: ''
summary: ''
authors:
- Victor Paredes
- Ayonga Hereid
tags: 
- whole body control
- control barrier function
categories: []
date: '2024-10-01'
lastmod: 2024-10-01T13:49:27-04:00
featured: true
draft: false

url_video: https://youtu.be/vNTIcODR6cI
links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/10644227


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
projects: ["whole-body-control"]
publishDate: '2024-10-01T17:49:27.195985Z'
publication_types:
- '1'
abstract: 
 Complex robotic systems require whole-body controllers to handle contact interactions, handle closed kinematic chains, and track task-space control objectives. However, for many applications, safety-critical controllers are essential to steer away from undesired robot configurations and prevent unsafe behaviors. A prime example is legged robotics, where we can have tasks such as balance control, regulation of torso orientation, and, most importantly, walking. As the coordination of multi-body systems is non-trivial, following a combination of those tasks might lead to configurations that are deemed dangerous, such as stepping on its support foot during walking, leaning the torso excessively, or producing excessive centroidal momentum, resulting in non-human-like walking. To address these challenges, we propose a formulation of an inverse dynamics control enhanced with control barrier functions that allow general higher-order relative degree safe sets for robotic systems with numerous degrees of freedom. Our approach utilizes a quadratic program that respects closed kinematic chains, minimizes the control objectives, and imposes desired constraints on the Zero Moment Point, friction cone, and torque. More importantly, it also ensures the forward invariance of a general user-defined high Relative-Degree safety set. We demonstrate the effectiveness of our method by applying it to the 3D biped robot Digit, both in simulation and with hardware experiments.
publication: '*American Control Conference*'
---

{{< youtube vNTIcODR6cI>}}