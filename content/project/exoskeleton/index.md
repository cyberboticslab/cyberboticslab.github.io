---
title: Dynamic Locomotion Control for Self-Balancing Lower-Limb Exoskeletons
summary: We strive to advancing the field of lower-limb exoskeletons and developing innovative solutions to enhance mobility and independence for individuals with paraplegia.
tags:
  - learning
  - control
  - optimization
  - exoskeleton
date: '2020-10-01T00:00:00Z'
featured: true

image:
  caption: 
  focal_point: Smart
  preview_only: false

reading_time: true
profile: false
pager: true
---


### Introduction

Individuals with paraplegia face significant challenges in walking independently due to the loss of lower-limb function. Traditional assistive devices, such as wheelchairs, provide mobility but limit the user's ability to walk naturally. Lower-limb exoskeletons offer a promising solution by providing powered assistance, but they often require additional support, such as crutches, for balance and stability. Our research aims to overcome these challenges by developing self-balancing control algorithms for powered exoskeletons.


### Benefits of Crutchless Dynamic Walking

1. **Improved Mobility and Independence**: By eliminating the need for crutches or additional support, individuals can experience a more natural and independent walking experience. This enhances their mobility and allows them to navigate various environments with greater ease.

2. **Enhanced Physical and Psychological Well-being**: Crutchless dynamic walking promotes a more active lifestyle, which can have positive effects on physical health and overall well-being. Additionally, the restoration of natural walking patterns can boost self-confidence and improve psychological well-being.

3. **Functional Rehabilitation**: The ability to walk dynamically without crutches facilitates functional rehabilitation for individuals with paraplegia. By engaging in natural walking movements, users can potentially regain strength, improve balance, and enhance their overall physical function.
   


<!-- ### Challenges and Our Approaches -->

### Research Focus

Despite modern-day exoskeleton devices becoming lighter, stronger, and more power-dense, the existing approaches of controlling powered leg devices are rudimentary and driven by non-smooth finite-state machines.  These controllers often require numerous hand-tuned parameters, offer no formal guarantees of either stability or safety, and typically need additional aids such as crutches for walking.

{{< youtube V30HsyUD4fs>}}

In our work, we holistically translated formal control methodologies from bipedal robots to lower-limb exoskeletons. We have realized, for the first time, dynamic stable walking for people with paraplegia without the use of crutches or any other kind of assistance using ATALATNE by translating formal HZD and G-HZD control design from bipedal robots to exoskeletons. Our approach combines trajectory optimization and supervised learning to synthesis stable exoskeleton gaits that can smoothly transition between different walking speeds. This work was achieved on three separate human subjects and has since been repeated with over 20 subjects in a clinical setting by Wandercraft. We also developed adaptive neural network control for ATALANTE to augment the classic HZD walking control under model uncertainty, thereby augmenting the unknown changes in human users' dynamics and external disturbances.



### Applications

The impact of our work extends beyond research and development. The self-balancing control design for powered exoskeletons has the potential to revolutionize mobility assistance for individuals with paraplegia. Some of the applications and future directions of our research include:

1. **Assistive Technology**: Our self-balancing exoskeletons can be used as assistive devices for individuals with paraplegia, providing them with enhanced mobility and independence in their daily lives.

2. **Rehabilitation**: The crutchless dynamic walking enabled by our exoskeletons can be integrated into rehabilitation programs, facilitating functional recovery and improving the overall rehabilitation outcomes for individuals with paraplegia.

3. **Personalized Control**: We are exploring the development of personalized control algorithms that adapt to the specific needs and abilities of individual users. This customization can further enhance the user experience and optimize the performance of the exoskeleton.
   
### Summary
Our work on self-balancing control design for powered exoskeletons aims to provide individuals with paraplegia the opportunity to walk dynamically without the need for crutches or additional support. By leveraging advanced machine learning technologies and control algorithms, we strive to enhance mobility, independence, and overall well-being for individuals with mobility impairments. Through collaborative partnerships and ongoing research, we are committed to advancing the field of lower-limb exoskeletons and improving the quality of life of millions. We believe that our research on self-balancing control design for powered exoskeletons will contribute to the development of more accessible and effective mobility solutions for individuals with impaired mobility.
