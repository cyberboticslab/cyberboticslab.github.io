---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Time-Varying Foot-Placement Control for Underactuated Humanoid Walking on Swaying Rigid Surfaces
subtitle: ''
summary: ''
authors:
- Yuan Gao
- Victor Paredes 
- Yukai Gong
- Zijian He
- Ayonga Hereid
- Yan Gu
tags: 
- dynamic rigid surface
- template model
- foot placement
categories: []
date: '2024-08-31'
lastmod: 2024-09-01T13:49:29-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
# image:
#   caption: 'Illustration of the proposed hybrid AIP model a) during a continuous swing phase and b) at a discrete foot-landing event.'
#   focal_point: Smart
#   preview_only: false

url_video: https://www.youtube.com/watch?v=NtAT0DFtMCY

links:
- name: arXiv
  url: https://arxiv.org/abs/2409.08371

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["whole-body-control"]
publishDate: '2024-08-31T17:49:29.175380Z'
publication_types:
- '3'
abstract: Locomotion on dynamic rigid surface (i.e., rigid surface accelerating in an inertial frame) presents complex challenges for controller design, which are essential for deploying humanoid robots in dynamic real-world environments such as moving trains, ships, and airplanes. This paper introduces a real-time, provably stabilizing control approach for underactuated humanoid walking on periodically swaying rigid surface. The first key contribution is the analytical extension of the classical angular momentum-based linear inverted pendulum model from static to swaying grounds. This extension results in a time-varying, nonhomogeneous robot model, which is fundamentally different from the existing pendulum models. We synthesize a discrete footstep control law for the model and derive a new set of sufficient stability conditions that verify the controller's stabilizing effect. Another key contribution is the development of a hierarchical control framework that incorporates the proposed footstep control law as its higher-layer planner to ensure the stability of underactuated walking. The closed-loop stability of the complete hybrid, full-order robot dynamics under this control framework is provably analyzed based on nonlinear control theory. Finally, experiments conducted on a Digit humanoid robot, both in simulations and with hardware, demonstrate the framework's effectiveness in addressing underactuated bipedal locomotion on swaying ground, even in the presence of uncertain surface motions and unknown external pushes. 
publication: '*Submitted to IEEE Transactions on Robotics*'
---

{{< youtube NtAT0DFtMCY >}}