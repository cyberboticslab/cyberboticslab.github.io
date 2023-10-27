---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Linear policies are sufficient to realize robust bipedal walking on challenging
  terrains
subtitle: ''
summary: ''
authors:
- Lokesh Krishna
- Guillermo A Castillo
- Utkarsh A Mishra
- Ayonga Hereid
- Shishir Kolathaya
tags: 
- linear policy
- robust locomotion
- rough terrain
categories: []
date: '2022-01-01'
lastmod: 2023-08-01T13:49:27-04:00
featured: false
draft: false

url_video: https://youtu.be/IK9BSHnNQrk?si=m4ca01ZEO-58b7A3
links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/9682564

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
publishDate: '2023-08-01T17:49:27.769756Z'
publication_types:
- '2'
abstract: 
  In this work, we demonstrate robust walking in the bipedal robot Digit on uneven terrains by just learning a single linear policy. In particular, we propose a new control pipeline, wherein the high-level trajectory modulator shapes the end-foot ellipsoidal trajectories, and the low-level gait controller regulates the torso and ankle orientation. The foot-trajectory modulator uses a linear policy and the regulator uses a linear PD control law. As opposed to neural network based policies, the proposed linear policy has only 13 learnable parameters, thereby not only guaranteeing sample efficient learning but also enabling simplicity and interpretability of the policy. This is achieved with no loss of performance on challenging terrains like slopes, stairs and outdoor landscapes. We first demonstrate robust walking in the custom simulation environment, MuJoCo, and then directly transfer to hardware with no modification of the control pipeline. We subject the biped to a series of pushes and terrain height changes, both indoors and outdoors, thereby validating the presented work.
publication: '*IEEE Robotics and Automation Letters (RA-L)*'
---

{{< youtube IK9BSHnNQrk >}}