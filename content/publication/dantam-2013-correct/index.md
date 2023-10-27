---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Correct software synthesis for stable speed-controlled robotic walking
subtitle: ''
summary: ''
authors:
- Neil Dantam
- Ayonga Hereid
- Aaron Ames
- Mike Stilman
tags: 
- speed regulation
- motion primitives
categories: []
date: '2013-01-01'
lastmod: 2023-08-01T13:49:23-04:00
featured: false
draft: false

url_video: https://youtu.be/rRt05_NbKm0

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
publishDate: '2023-08-01T17:49:23.102005Z'
publication_types:
- '1'
abstract: 
  'We present a software synthesis method for speed- controlled robot walking based on supervisory control of a context-free Motion Grammar. First, we use Human-Inspired control to identify parameters for fixed speed walking and for transitions between fixed speeds, guaranteeing dynamic stability. Next, we build a Motion Grammar representing the discrete-time control for this set of speeds. Then, we synthesize C code from this grammar and generate supervisors1 online to achieve desired walking speeds, guaranteeing correctness of discrete computation. Finally, we demonstrate this approach on the Aldebaran NAO, showing stable walking transitions with dynamically selected speeds.'
publication: '*Robotics: Science and Systems*'
---

{{< youtube rRt05_NbKm0>}}