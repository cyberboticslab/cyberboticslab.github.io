---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Efficient HZD gait generation for three-dimensional underactuated humanoid
  running
subtitle: ''
summary: ''
authors:
- Wen-Loong Ma
- Ayonga Hereid
- Christian M Hubicki
- Aaron D Ames
tags: 
- humanoid running
- hybrid zero dynamics
- direct collocation
categories: []
date: '2016-01-01'
lastmod: 2023-08-01T13:49:24-04:00
featured: false
draft: false


links:
- name: IEEE
  url: https://ieeexplore.ieee.org/document/7759856

url_video: https://youtu.be/Izs4TN0puto
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
publishDate: '2023-08-01T17:49:24.796790Z'
publication_types:
- '1'
abstract: 
  'Dynamic humanoid locomotion is a challenging control problem, and running is especially difficult to achieve, given the underactuation inherent to aerial domains. Previous work developed a gait-generating optimization framework for dynamic locomotion in the context of hybrid zero dynamics, producing stable 3D walking on the humanoid hardware platform DURUS. Here, we demonstrate that this optimization method also extends to stable 3D running. Gaits generated from the optimization, which utilizes the dynamics of all 23 degrees of freedom to maximize energy economy, results in stable running in a DURUS simulation model. Notably, the presented running is underactuated in all domains, due to DURUS spring-legged design. Further, we generate 25 different running gaits, over a range of speeds (1.5-3.0 m/s), to demonstrate the reliability of solving the large-scale nonlinear program. We report statistical performance of the optimization in successfully generating stable running (average computation time: 323 seconds) in an effort to establish a benchmark for large-scale gait generation. We inspected this array of gaits across speeds, noting recognizable trends in optimized strategies from prior studies on lower-order models-e.g., both increased step frequency and step length with speed-along with the first reported cost-of-transport curve for a 3D humanoid running model. We consider this result an important step toward humanoid running on the DURUS hardware platform.'
publication: '*2016 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)*'
---

{{< youtube Izs4TN0puto>}}
