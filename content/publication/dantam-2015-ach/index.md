---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'The ach library: a new framework for real-time communication'
subtitle: ''
summary: ''
authors:
- Neil T Dantam
- Daniel M Lofaro
- Ayonga Hereid
- Paul Y Oh
- Aaron D Ames
- Mike Stilman
tags: []
categories: []
date: '2015-01-01'
lastmod: 2023-08-01T13:49:25-04:00
featured: false
draft: false

links:
- name: IEEE
  url: https://ieeexplore.ieee.org/document/7012101

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
publishDate: '2023-08-01T17:49:25.643936Z'
publication_types:
- '2'
abstract: 
  'Correct real-time software is vital for robots in safety-critical roles such as service and disaster response. These systems depend on software for locomotion, navigation, manipulation, and even seemingly innocuous tasks such as safely regulating battery voltage. A multiprocess software design increases robustness by isolating errors to a single process, allowing the rest of the system to continue operation. This approach also assists with modularity and concurrency. For real-time tasks, such as dynamic balance and force control of manipulators, it is critical to communicate the latest data sample with minimum latency. There are many communication approaches intended for both general-purpose and real-time needs [9], [13], [15], [17], [19]. Typical methods focus on reliable communication or network transparency and accept a tradeoff of increased message latency or the potential to discard newer data. By focusing instead on the specific case of real-time communication on a single host, we reduce communication latency and guarantee access to the latest sample. We present a new interprocess communication (IPC) library, Ach which addresses this need, and discuss its application for real-time multiprocess control on three humanoid robots (Figure 1). (Ach is available at http://www.golems.org/projects/ach.html. The name Ach comes from the common abbreviation for the motor neurotransmitter Acetylcholine and the computer networking term ACK.)'
publication: '*IEEE Robotics & Automation Magazine*'
---
