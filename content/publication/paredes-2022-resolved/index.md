---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Resolved motion control for 3d underactuated bipedal walking using linear inverted
  pendulum dynamics and neural adaptation
subtitle: ''
summary: ''
authors:
- Victor C Paredes
- Ayonga Hereid
tags: 
- adaptive learning
- linear inverted pendulum
- inverse kinematics
categories: []
date: '2022-01-01'
lastmod: 2023-08-01T13:49:28-04:00
featured: false
draft: false


links:
- name: IEEE
  url: https://ieeexplore.ieee.org/abstract/document/9982009

url_video: 'https://youtu.be/7ym2gm3XiOE?si=7e_We4BFv7onOJNZ'

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
publishDate: '2023-08-01T17:49:28.189029Z'
publication_types:
- '1'
abstract: 
  We present a framework to generate periodic trajectory references for a 3D under-actuated bipedal robot, using a linear inverted pendulum (LIP) based controller with adaptive neural regulation. We use the LIP template model to estimate the robot's center of mass (CoM) position and velocity at the end of the current step, and formulate a discrete controller that determines the next footstep location to achieve a desired walking profile. This controller is equipped on the frontal plane with a Neural-Network-based adaptive term that reduces the model mismatch between the template and physical robot that particularly affects the lateral motion. Then, the foot placement location computed for the LIP model is used to generate task space trajectories (CoM and swing foot trajectories) for the actual robot to realize stable walking. We use a fast, real-time QP-based inverse kinematics algorithm that produces joint references from the task space trajectories, which makes the formulation independent of the knowledge of the robot dynamics. Finally, we implemented and evaluated the proposed approach in simulation and hardware experiments with a Digit robot obtaining stable periodic locomotion for both cases.
publication: '*2022 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)*'
---

{{< youtube 7ym2gm3XiOE>}}