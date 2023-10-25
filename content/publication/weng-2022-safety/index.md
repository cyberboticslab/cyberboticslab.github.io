---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'On safety testing, validation, and characterization with scenario-sampling:
  A case study of legged robots'
subtitle: ''
summary: ''
authors:
- Bowen Weng
- Guillermo A Castillo
- Wei Zhang
- Ayonga Hereid
tags: []
categories: []
date: '2022-01-01'
lastmod: 2023-08-01T13:49:28-04:00
featured: false
draft: false

url_video:
links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/9981359

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
projects: ["safety-testing"]
publishDate: '2023-08-01T17:49:28.050687Z'
publication_types:
- '1'
abstract: 
  The dynamic response of the legged robot locomotion is non-Lipschitz and can be stochastic due to environmental uncertainties. To test, validate, and characterize the safety performance of legged robots, existing solutions on observed and inferred risk can be incomplete and sampling inefficient. Some formal verification methods suffer from the model precision and other surrogate assumptions. In this paper, we propose a scenario sampling based testing framework that characterizes the overall safety performance of a legged robot by specifying (i) where (in terms of a set of states) the robot is potentially safe, and (ii) how safe the robot is within the specified set. The framework can also help certify the commercial deployment of the legged robot in real-world environment along with human and compare safety performance among legged robots with different mechanical structures and dynamic properties. The proposed framework is further deployed to evaluate a group of state-of-the-art legged robot locomotion controllers from various model-based, deep neural network involved, and reinforcement learning based methods in the literature. Among a series of intended work domains of the studied legged robots (e.g. tracking speed on sloped surface, with abrupt changes on demanded velocity, and against adversarial push-over disturbances), we show that the method can adequately capture the overall safety characterization and the subtle performance insights. Many of the observed safety outcomes, to the best of our knowledge, have never been reported by the existing work in the legged robot literature.
publication: '*2022 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)*'
---
