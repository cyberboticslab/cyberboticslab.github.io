---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Work those arms: Toward dynamic and stable humanoid walking that optimizes
  full-body motion'
subtitle: ''
summary: ''
authors:
- Christian M Hubicki
- Ayonga Hereid
- Michael X Grey
- Andrea L Thomaz
- Aaron D Ames
tags: []
categories: []
date: '2016-01-01'
lastmod: 2023-08-01T13:49:24-04:00
featured: false
draft: false

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/document/7487293

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
publishDate: '2023-08-01T17:49:23.951249Z'
publication_types:
- '1'
abstract: 
  'Humanoid robots are designed with dozens of actuated joints to suit a variety of tasks, but walking controllers rarely make the best use of all of this freedom. We present a framework for maximizing the use of the full humanoid body for the purpose of stable dynamic locomotion, which requires no restriction to a planning template (e.g. LIPM). Using a hybrid zero dynamics (HZD) framework, this approach optimizes a set of outputs which provides requirements for the motion for all actuated links, including arms. These output equations are then rapidly solved by a whole-body inverse-kinematic (IK) solver, providing a set of joint trajectories to the robot. We apply this procedure to a simulation of the humanoid robot, DRC-HUBO, which has over 27 actuators. As a consequence, the resulting gaits swing their arms, not by a user defining swinging motions a priori or superimposing them on gaits post hoc, but as an emergent behavior from optimizing the dynamic gait. We also present preliminary dynamic walking experiments with DRC-HUBO in hardware, thereby building a case that hybrid zero dynamics as augmented by inverse kinematics (HZD+IK) is becoming a viable approach for controlling the full complexity of humanoid locomotion.'
publication: '*2016 IEEE International Conference on Robotics and Automation (ICRA)*'
---
