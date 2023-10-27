---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'FROST*: Fast Robot Optimization and Simulation Toolkit'
subtitle: ''
summary: ''
authors:
- Ayonga Hereid
- Aaron D Ames
tags: 
- frost
- trajectory optimization
- simulation
categories: []
date: '2017-01-01'
lastmod: 2023-08-01T13:49:25-04:00
featured: false
draft: false


url_video: https://youtu.be/BEckrqY2MfM
url_code: https://github.com/ayonga/frost-dev

links: 
- name: IEEE
  url: https://ieeexplore.ieee.org/document/8202230
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
projects: ["frost"]
publishDate: '2023-08-01T17:49:25.360540Z'
publication_types:
- '1'
abstract: 
  'This paper presents FROST, an open-source MATLAB toolkit for modeling, trajectory optimization and simulation of hybrid dynamical systems with a particular focus in dynamic locomotion. The design objective of FROST is to provide a unified software environment for developing model-based control and motion planning algorithms for robotic systems whose dynamics is hybrid in nature. In particular, FROST uses directed graphs to describe the underlying discrete structure of hybrid system models, which renders it capable of representing a wide variety of robotic systems. Equipped with a custom symbolic math toolbox in MATLAB using Wolfram Mathematica, one can rapidly prototype the mathematical model of robot kinematics and dynamics and generate optimized code of symbolic expressions to boost the speed of optimization and simulation in FROST. In favor of agile and dynamic behaviors, we utilize virtual constraint based motion planning and feedback controllers for robotic systems to exploit the full-order dynamics of the model. Moreover, FROST provides a fast and tractable framework for planning optimal trajectories of hybrid dynamical systems using advanced direct collocation algorithms. FROST has been successfully used to synthesize dynamic walking in multiple bipedal robots. Case studies of such applications are considered in this paper, wherein different types of walking gaits are generated for two specific humanoid robots and validated in simulation.'
publication: '*2017 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)*'
---

{{< youtube BEckrqY2MfM>}}