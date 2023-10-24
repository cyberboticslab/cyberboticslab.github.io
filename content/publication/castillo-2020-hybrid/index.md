---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Hybrid zero dynamics inspired feedback control policy design for 3d bipedal
  locomotion using reinforcement learning
subtitle: ''
summary: ''
authors:
- Guillermo A Castillo
- Bowen Weng
- Wei Zhang
- Ayonga Hereid
tags: []
categories: []
date: '2020-05-01'
lastmod: 2023-08-01T13:49:27-04:00
featured: false
draft: false

url_video: https://youtu.be/GOT6bnxqwuU
links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/9197175
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
publishDate: '2023-08-01T17:49:26.914807Z'
publication_types:
- '1'
abstract: 
  This paper presents a novel model-free reinforcement learning (RL) framework to design feedback control policies for 3D bipedal walking. Existing RL algorithms are often trained in an end-to-end manner or rely on prior knowledge of some reference joint trajectories. Different from these studies, we propose a novel policy structure that appropriately incorporates physical insights gained from the hybrid nature of the walking dynamics and the well-established hybrid zero dynamics approach for 3D bipedal walking. As a result, the overall RL framework has several key advantages, including lightweight network structure, short training time, and less dependence on prior knowledge. We demonstrate the effectiveness of the proposed method on Cassie, a challenging 3D bipedal robot. The proposed solution produces stable limit walking cycles that can track various walking speed in different directions. Surprisingly, without specifically trained with disturbances to achieve robustness, it also performs robustly against various adversarial forces applied to the torso towards both the forward and the backward directions. 
publication: '*2020 IEEE International Conference on Robotics and Automation (ICRA)*'
---

{{< youtube GOT6bnxqwuU >}}