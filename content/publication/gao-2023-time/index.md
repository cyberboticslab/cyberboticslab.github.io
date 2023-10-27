---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Time-Varying ALIP Model and Robust Foot-Placement Control for Underactuated
  Bipedal Robotic Walking on a Swaying Rigid Surface
subtitle: ''
summary: ''
authors:
- Yuan Gao
- Yukai Gong
- Victor Paredes
- Ayonga Hereid
- Yan Gu
tags: 
- dynamic rigid surface
- template model
- foot placement
categories: []
date: '2023-05-31'
lastmod: 2023-08-01T13:49:29-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: 'Illustration of the proposed hybrid AIP model a) during a continuous swing phase and b) at a discrete foot-landing event.'
  focal_point: Smart
  preview_only: false

# url_video: https://youtu.be/dhHMfnl7YlU?si=trb-IK-otANCK_9E

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/10156254
- name: arXiv
  url: https://arxiv.org/abs/2210.13371v2

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["whole-body-control"]
publishDate: '2023-05-31T17:49:29.175380Z'
publication_types:
- '1'
abstract: Controller design for bipedal walking on dynamic rigid surfaces (DRSes), which are rigid surfaces moving in the inertial frame (e.g., ships and airplanes), remains largely underexplored. This paper introduces a hierarchical control approach that achieves stable underactuated bipedal walking on a horizontally oscillating DRS. The highest layer of our approach is a real-time motion planner that generates desired global behaviors (i.e., center of mass trajectories and footstep locations) by stabilizing a reduced-order robot model. One key novelty of this layer is the derivation of the reduced-order model by analytically extending the angular momentum based linear inverted pendulum (ALIP) model from stationary to horizontally moving surfaces. The other novelty is the development of a discrete-time foot-placement controller that exponentially stabilizes the hybrid, linear, time-varying ALIP. The middle layer translates the desired global behaviors into the robot’s full-body reference trajectories for all directly actuated degrees of freedom, while the lowest layer exponentially tracks those reference trajectories based on the full-order, hybrid, nonlinear robot model. Simulations confirm that the proposed framework ensures stable walking of a planar underactuated biped under different swaying DRS motions and gait types.
publication: '*2023 American Control Conference (**ACC**)*'
---

<!-- {{< youtube dhHMfnl7YlU >}} -->