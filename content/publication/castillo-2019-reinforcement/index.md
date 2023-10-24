---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Reinforcement Learning Meets Hybrid Zero Dynamics: A case study for RABBIT'
subtitle: '' #'*2019 International Conference on Robotics and Automation (**ICRA**)*'
summary: ''
publication: '*2019 International Conference on Robotics and Automation (**ICRA**)*'
authors:
- Guillermo A Castillo
- Bowen Weng
- Ayonga Hereid
- Zheng Wang
- Wei Zhang
tags: 
- rabbit
- reinforcement learning
- hybrid zero dynamics
- underactuated robots
categories: []
date: '2019-05-31'
lastmod: 2023-08-01T13:49:26-04:00
featured: true
draft: false

# url_pdf: https://arxiv.org/pdf/1810.01977.pdf
# url_code: ''
# url_dataset: ''
# url_poster: ''
# url_project: ''
# url_slides: ''
# url_source: https://arxiv.org/abs/1810.01977
url_video: https://youtu.be/dhHMfnl7YlU?si=trb-IK-otANCK_9E

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/document/8793627
- name: arXiv
  url: https://arxiv.org/abs/1810.01977
  # icon_pack: fab
  # icon: arXiv

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
projects: 
- "hierarchical-reinforcement-learning"
publishDate: '2023-08-01T17:49:26.493474Z'
publication_types:
- '1'
abstract: The design of feedback controllers for bipedal robots is challenging due to the hybrid nature of its dynamics and the complexity imposed by high-dimensional bipedal models. In this paper, we present a novel approach for the design of feedback controllers using Reinforcement Learning (RL) and Hybrid Zero Dynamics (HZD). Existing RL approaches for bipedal walking are inefficient as they do not consider the underlying physics, often requires substantial training, and the resulting controller may not be applicable to real robots. HZD is a powerful tool for bipedal control with local stability guarantees of the walking limit cycles. In this paper, we propose a non traditional RL structure that embeds the HZD framework into the policy learning. More specifically, we propose to use RL to find a control policy that maps from the robot's reduced order states to a set of parameters that define the desired trajectories for the robot's joints through the virtual constraints. Then, these trajectories are tracked using an adaptive PD controller. The method results in a stable and robust control policy that is able to track variable speed within a continuous interval. Robustness of the policy is evaluated by applying external forces to the torso of the robot. The proposed RL framework is implemented and demonstrated in OpenAI Gym with the MuJoCo physics engine based on the well-known RABBIT robot model. 



# publication_short: "**ICRA**"
---

{{< youtube dhHMfnl7YlU >}}

<!-- <iframe width="720" height="405" src="https://www.youtube.com/embed/dhHMfnl7YlU?si=trb-IK-otANCK_9E?autoplay=1&loop=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> -->