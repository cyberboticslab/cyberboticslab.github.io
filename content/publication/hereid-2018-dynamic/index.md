---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Dynamic humanoid locomotion: A scalable formulation for HZD gait optimization'
subtitle: ''
summary: ''
authors:
- Ayonga Hereid
- Christian M Hubicki
- Eric A Cousineau
- Aaron D Ames
tags: []
categories: []
date: '2018-01-01'
lastmod: 2023-08-01T13:49:25-04:00
featured: true
draft: false

url_video: https://youtu.be/1fC7b2LjVW4?si=scbzz3OeWTMHITUh
links:
- name: IEEE
  url: https://ieeexplore.ieee.org/document/8260563

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
publishDate: '2023-08-01T17:49:25.497743Z'
publication_types:
- '2'
abstract: 
  'Hybrid zero dynamics (HZD) has emerged as a popular framework for dynamic walking but has significant implementation difficulties when applied to the high degrees of freedom humanoids. The primary impediment is the process of gait design-it is difficult for optimizers to converge on a viable set of virtual constraints defining a gait. This paper presents a methodology that allows for fast and reliable generation of dynamic robotic walking gaits through the HZD framework, even in the presence of underactuation. Specifically, we describe an optimization formulation that builds upon the novel combination of HZD and direct collocation methods. Furthermore, achieving a scalable implementation required developing a defect-variable substitution formulation to simplify expressions, which ultimately allows us to generate compact analytic Jacobians of the constraints. We experimentally validate our methodology on an underactuated humanoid, DURUS, a spring-legged machine designed to facilitate energy-economical walking. We show that the optimization approach, in concert with the HZD framework, yields dynamic and stable walking gaits in hardware with a total electrical cost of transport of 1.33.'
publication: '*IEEE Transactions on Robotics*'
---

{{< youtube ipWNSeGRPls >}}

{{< youtube N9Mpq94HKf0  >}}

{{< youtube HHnqatPvU6Q  >}}