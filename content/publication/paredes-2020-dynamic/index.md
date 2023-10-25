---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Dynamic locomotion of a lower-limb exoskeleton through virtual constraints
  based zmp regulation
subtitle: ''
summary: ''
authors:
- Victor Paredes
- Ayonga Hereid
tags: []
categories: []
date: '2020-10-01'
lastmod: 2023-08-01T13:49:27-04:00
featured: false
draft: false

url_video: https://youtu.be/WsZWf8C3ZgY
links:
- name: ASME
  url: https://asmedigitalcollection.asme.org/DSCC/proceedings-abstract/DSCC2020/1096497


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
projects: ["exoskeleton"]
publishDate: '2023-08-01T17:49:27.195985Z'
publication_types:
- '1'
abstract: 
 Robotic lower-limb exoskeletons have the potentials to assist individuals with paraplegia to perform normal ambulatory functions and to provide exceptional health benefits. While modern-day hardware for exoskeletons is becoming more powerful, there are still significant challenges in implementing a practical exoskeleton motion control framework that helps paraplegic individuals to complete regular ambulatory tasks stably, safely, and efficiently without the use of arm-crutches. Inspired by the current development in dynamic walking controllers for a bipedal robot, this paper proposes a Hybrid Zero Dynamics (HZD) based control approach for powered lower-limb exoskeletons to achieve dynamic hand-free locomotion. Due to the unmodelled dynamics and exerted forces from the user upon the exoskeleton, the model-based approaches such as Hybrid Zero Dynamics struggles when implementing on the actual hardware. In this paper, we systematically formulate a virtual-constraints-based regulation framework in order to robustly stabilize the system around a stable periodic gait within the HZD framework. This regulator is then used to regulate the zero moment point (ZMP) to improve the lateral stability of the bipedal robot by indirectly regulating the center of mass (CoM) position of the exoskeleton due to the lack of available force sensors at the bottom of the feet. The proposed approach presents a general structure with which the virtual constraints can be heuristically regulated to satisfy the stability condition imposed by the ZMP criteria without compromising the hybrid invariance of the walking gaits. The effectiveness of the regulators was demonstrated through stable walking of a powered lower-limb exoskeleton in simulation and experimentation.
publication: '*Dynamic Systems and Control Conference (DSCC)*'
---

{{< youtube WsZWf8C3ZgY>}}