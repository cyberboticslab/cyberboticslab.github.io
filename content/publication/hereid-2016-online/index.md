---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Online optimal gait generation for bipedal walking robots using legendre pseudospectral
  optimization
subtitle: ''
summary: ''
authors:
- Ayonga Hereid
- Shishir Kolathaya
- Aaron D Ames
tags: []
categories: []
date: '2016-01-01'
lastmod: 2023-08-01T13:49:25-04:00
featured: false
draft: false

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/7799218

url_video: https://youtu.be/wm9Td43HiMc
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
publishDate: '2023-08-01T17:49:25.783229Z'
publication_types:
- '1'
abstract: 
  'This paper presents an optimal gait synthesis method that exploits the full body dynamics of robots using the Hybrid Zero Dynamics (HZD) control framework and-for the first time-experimentally realizes online HZD gait generation for a planar underactuated robot. Hybrid zero dynamics is an established theoretical framework that formally enables stable control of dynamic locomotion by enforcing virtual constraints through feedback controllers. An essential part of successfully realizing dynamic walking with HZD framework is determining parameters of the virtual constraints that satisfy hybrid invariant condition via nonlinear constrained optimization. Due to the complexity of the full hybrid system model of the robot, these optimization problems often suffer from slow convergence and local minima. In this paper, we improve the reliability of the HZD gait optimization and significantly increase the convergence speed by taking advantage of the direct transcription formulation and the exponential convergence of the global orthogonal collocation (a.k.a. pseudospectral) method. As a result, generating HZD gaits online becomes feasible with an average computation time less than 0.5 seconds, as will be demonstrated experimentally on a bipedal robot.'
publication: '*Decision and Control (CDC), 2016 IEEE 55th Conference on*'
---

{{< youtube wm9Td43HiMc >}}
