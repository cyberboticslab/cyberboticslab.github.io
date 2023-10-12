---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Reinforcement learning-based cascade motion policy design for robust 3D bipedal
  locomotion
subtitle: ''
summary: ''
authors:
- Guillermo A Castillo
- Bowen Weng
- Wei Zhang
- Ayonga Hereid
tags: []
categories: []
date: '2022-01-01'
lastmod: 2023-08-01T13:49:28-04:00
featured: false
draft: false

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/9714352

url_video: https://youtu.be/ocAZtHr07Fw

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
publishDate: '2023-08-01T17:49:27.912459Z'
publication_types:
- '2'
abstract: 
  This paper presents a novel reinforcement learning (RL) framework to design cascade feedback control policies for 3D bipedal locomotion. Existing RL algorithms are often trained in an end-to-end manner or rely on prior knowledge of some reference joint or task space trajectories. Unlike these studies, we propose a policy structure that decouples the bipedal locomotion problem into two modules that incorporate the physical insights from the nature of the walking dynamics and the well-established Hybrid Zero Dynamics approach for 3D bipedal walking. As a result, the overall RL framework has several key advantages, including lightweight network structure, sample efficiency, and less dependence on prior knowledge. The proposed solution learns stable and robust walking gaits from scratch and allows the controller to realize omnidirectional walking with accurate tracking of the desired velocity and heading angle. The learned policies also perform robustly against various adversarial forces applied to the torso and walking blindly on a series of challenging and unstructured terrains. These results demonstrate that the proposed cascade feedback control policy is suitable for navigation of 3D bipedal robots in indoor and outdoor environments.
publication: '*IEEE Access*'
---

{{< youtube ocAZtHr07Fw >}}