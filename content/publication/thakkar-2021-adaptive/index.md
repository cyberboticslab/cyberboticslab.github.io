---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Adaptive feedback regulator for powered lower-limb exoskeleton under model
  uncertainty
subtitle: ''
summary: ''
authors:
- Kirtankumar Thakkar
- Victor Paredes
- Ayonga Hereid
tags: []
categories: []
date: '2021-01-01'
lastmod: 2023-08-01T13:49:27-04:00
featured: false
draft: false

links:
- name: arXiv
  url: https://arxiv.org/abs/2104.11775

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
publishDate: '2023-08-01T17:49:27.631025Z'
publication_types:
- '3'
abstract: 
  This paper presents a neural network (NN) based adaptive feedback regulator to ensure the lateral and longitudinal stability and regulate the desired walking velocity of a lower-limb exoskeleton under model uncertainty. The traditional model-based controllers for lower-limb exoskeletons often fail to stabilize the robot or accurately track the desired behaviors under model uncertainties or external disturbances. This paper proposes a neural network (NN) based online adaptive regulator that compensates for the unknown changes in model parameters and external disturbances by modifying the nominal joint trajectory. A gradient descent-based delta rule is implemented to update the weights of a single layer NN, which can be efficiently performed online by design. We demonstrate the performance of the presented regulator on ATALANTE, a fully actuated lower limb exoskeleton designed for paraplegic patients. The simulation results show that the proposed approach noticeably improves stability and the tracking performance of the system, despite significant changes in model parameters and large adversarial pushes.
publication: '*arXiv preprint arXiv:2104.11775*'
---
