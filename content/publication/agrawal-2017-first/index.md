---
# Documentation: https://wowchemy.com/docs/managing-content/

title: First steps towards translating HZD control of bipedal robots to decentralized
  control of exoskeletons
subtitle: ''
summary: ''
authors:
- Ayush Agrawal
- Omar Harib
- Ayonga Hereid
- Sylvain Finet
- Matthieu Masselin
- Laurent Praly
- Aaron D Ames
- Koushil Sreenath
- Jessy W Grizzle
tags: []
categories: []
date: '2017-01-01'
lastmod: 2023-08-01T13:49:25-04:00
featured: false
draft: false

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/document/7891605

url_video: https://www.youtube.com/watch?v=VXP7DKY6Trc
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
publishDate: '2023-08-01T17:49:25.084155Z'
publication_types:
- '2'
abstract: 
  'This paper presents preliminary results toward translating gait and control design for bipedal robots to decentralized control of an exoskeleton aimed at restoring mobility to patients with lower limb paralysis, without the need for crutches. A mathematical hybrid dynamical model of the human-exoskeleton system is developed and a library of dynamically feasible periodic walking gaits for different walking speeds is found through nonlinear constrained optimization using the full-order dynamical system. These walking gaits are stabilized using a centralized (i.e., full-state information) hybrid zero dynamics-based controller, which is then decentralized (i.e., control actions use partial state information) so as to be implementable on the exoskeleton subsystem. A control architecture is then developed so as to allow the user to actively control the exoskeleton speed through his/her upper body posture. Numerical simulations are carried out to compare the two controllers. It is found that the proposed decentralized controller not only preserves the periodic walking gaits but also inherits the robustness to perturbations present in the centralized controller. Moreover, the proposed velocity regulation scheme is able to reach a steady state and track desired walking speeds under both, centralized, and decentralized schemes.'
publication: '*IEEE Access*'
---

{{< youtube VXP7DKY6Trc>}}