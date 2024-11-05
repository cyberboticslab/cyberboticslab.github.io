---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Moving past point-contacts: Extending the ALIP model to humanoids with non-trivial feet using hierarchical, full-body momentum control'
subtitle: ''
summary: ''
authors:
- Victor Paredes
- Daniel Hagen
- Samual Chesebrough
- Riley Swann
- Denis Garagic
- Ayonga Hereid
tags: 
- whole body control
- exoskeleton
categories: []
date: '2024-10-01'
lastmod: 2024-10-01T13:49:27-04:00
featured: true
draft: false

url_video: https://youtu.be/vNTIcODR6cI
links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/10644609


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
projects: ["hybrid-exo-humanoids"]
publishDate: '2024-10-01T17:49:27.195985Z'
publication_types:
- '1'
abstract: 
 The Angular-Momentum Linear Inverted Pendulum (ALIP) model is a promising motion planner for bipedal robots. However, it relies on two assumptions (1) the robot has point-contact feet or passive ankles, and (2) the angular momentum around the center of mass, known as centroidal angular momentum, is negligible. This paper addresses the question of whether the ALIP paradigm can be applied to more general bipedal systems with complex foot geometry (e.g., flat feet) and nontrivial torso/limb inertia and mass distribution (e.g., non-centralized arms). In such systems, the dynamics introduce non-negligible centroidal momentum and contact wrenches at the feet, rendering the assumptions of the ALIP model invalid. This paper presents the ALIP planner for general bipedal robots with non-point-contact feet through the use of a task-space whole-body controller that regulates centroidal momentum, thereby ensuring that the robot's behavior aligns with the desired template dynamics. To demonstrate the effectiveness of our proposed approach, we conduct simulations using the Sarcos © Guardian® XO ® robot, which is a hybrid humanoid/exoskeleton with large, offset feet. The results demonstrate the practicality and effectiveness of our approach in achieving stable and versatile bipedal locomotion.
publication: '*American Control Conference*'
---

{{< youtube vNTIcODR6cI>}}