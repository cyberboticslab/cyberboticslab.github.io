---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Data-driven latent space representation for robust bipedal locomotion learning
subtitle: ''
summary: ''
authors:
- Guillermo A Castillo
- Bowen Weng
- Wei Zhang
- Ayonga Hereid
tags: 
- latent space
- autoencoder
- reinforcement learning
categories: []
date: '2023-09-15'
lastmod: 2023-10-04T13:49:28-04:00
featured: false
draft: false

url_video: https://youtu.be/SUIkrigsrao?si=sxHFlpPmWIKNP-J4

links:
- name: arXiv
  url: https://arxiv.org/abs/2309.15740

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
publishDate: '2023-08-01T17:49:27.912459Z'
publication_types:
- '3'
abstract: 
  This paper presents a novel framework for learning robust bipedal walking by combining a data-driven state representation with a Reinforcement Learning (RL) based locomotion policy. The framework utilizes an autoencoder to learn a low-dimensional latent space that captures the complex dynamics of bipedal locomotion from existing locomotion data. This reduced dimensional state representation is then used as states for training a robust RL-based gait policy, eliminating the need for heuristic state selections or the use of template models for gait planning. The results demonstrate that the learned latent variables are disentangled and directly correspond to different gaits or speeds, such as moving forward, backward, or walking in place. Compared to traditional template model-based approaches, our framework exhibits superior performance and robustness in simulation. The trained policy effectively tracks a wide range of walking speeds and demonstrates good generalization capabilities to unseen scenarios. 
publication: '*arXiv preprint*'
---

{{< youtube SUIkrigsrao >}}
