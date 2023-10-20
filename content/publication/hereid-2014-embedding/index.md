---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Embedding of slip dynamics on underactuated bipedal robots through multi-objective
  quadratic program based control
subtitle: ''
summary: ''
authors:
- Ayonga Hereid
- Matthew J Powell
- Aaron D Ames
tags: []
categories: []
date: '2014-01-01'
lastmod: 2023-08-01T13:49:23-04:00
featured: false
draft: false

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/document/7039843

url_video:  https://youtu.be/3I6YtCxt-UA
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
publishDate: '2023-08-01T17:49:23.384309Z'
publication_types:
- '1'
abstract: 
  'This paper presents a method for achieving stable periodic walking, consisting of phases of single and double support, on underactuated walking robots by embedding Spring Loaded Inverted Pendulum (SLIP) dynamics. Beginning with a SLIP model, the dynamics are stabilized to a constant energy level and periodic walking gaits are found; an equality constraint on torque can be used to shape the dynamics of the full-order robot to obey the corresponding SLIP dynamics. To transition these gaits to full-order robots, the essential elements of SLIP walking gaits, i.e., the swing leg touchdown angle, are utilized to synthesis control Lyapunov functions that result in inequality constraints in torque. Finally, the desired force interactions with the environment as dictated by SLIP dynamics are utilized to obtain inequality constraints in the reaction forces. Combining these equality and inequality constraints results in a multi-objective quadratic program based controller that is implemented on a multi-domain hybrid system model of an underactuated bipedal robot. The end result is stable periodic walking on the full-order model that shows remarkable similarity to the SLIP gait from which it was derived.'
publication: '*53rd IEEE Conference on Decision and Control*'
---

{{< youtube 3I6YtCxt-UA>}}