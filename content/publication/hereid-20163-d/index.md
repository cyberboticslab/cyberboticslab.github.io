---
# Documentation: https://wowchemy.com/docs/managing-content/

title: '3D dynamic walking with underactuated humanoid robots: A direct collocation
  framework for optimizing hybrid zero dynamics'
subtitle: ''
summary: ''
authors:
- Ayonga Hereid
- Eric A Cousineau
- Christian M Hubicki
- Aaron D Ames
tags: []
categories: []
date: '2016-01-01'
lastmod: 2023-08-01T13:49:24-04:00
featured: true
draft: false

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/document/7487279

url_video: https://youtu.be/wWELfUsNuGU

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
publishDate: '2023-08-01T17:49:24.227847Z'
publication_types:
- '1'
abstract: 
  'Hybrid zero dynamics (HZD) has emerged as a popular framework for dynamic and underactuated bipedal walking, but has significant implementation difficulties when applied to the high degrees of freedom present in humanoid robots. The primary impediment is the process of gait design-it is difficult for optimizers to converge on a viable set of virtual constraints defining a gait. This paper presents a methodology that allows for the fast and reliable generation of efficient multi-contact robotic walking gaits through the framework of HZD, even in the presence of underactuation. To achieve this goal, we unify methods from trajectory optimization with the control framework of multi-domain hybrid zero dynamics. By formulating a novel optimization problem in the context of direct collocation and generating analytic Jacobians for the constraints, solving the resulting nonlinear program becomes tractable for large-scale nonlinear programming solvers, even for systems as high-dimensional as humanoid robots. We experimentally validated our methodology on the spring-legged prototype humanoid, DURUS, showing that the optimization approach yields dynamic and stable 3D walking gaits.'
publication: '*2016 IEEE International Conference on Robotics and Automation (ICRA)*'
---

{{< youtube wWELfUsNuGU>}}