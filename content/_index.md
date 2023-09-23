---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      # video:
      #   filename: welcome.mp4
      title: |
        Cyberbotics Lab 
      image:
        filename: animation_llfwgvki_small.gif
      text: | 
        under construction
      #   <br>
        
      #   My research interests lie at the intersection of nonlinear control and optimization theory, with a particular focus on developing novel control solutions for complex robotic systems. The central objective of my research is to develop computationally tractable optimization-based control methodologies that unify formal control theory with advanced numerical optimization techniques and, ultimately, to realize versatile and dynamic maneuvers experimentally on a variety of robotic platforms including home assistant robots and robotic exoskeletons. 
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'

  # - block: markdown
  #   content:
  #     title: 👋 Welcome to Cyberbotics Lab
  #     subtitle: 'Cdad adlka ladfkadlk '
  #     text: 
  #   design:
  #     columns: '1'
  #     background:
  #       video:
  #         filename: welcome.mp4
  #         flip: false
  #         filters:
  #           brightness: 0.1
  #         position: center
  #         color: '#555'
  #       # image: 
  #       #   filename: coders.jpg
  #       #   parallax: false
  #       #   position: center
  #       #   size: cover
  #       #   text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen
     
  
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'

  # - block: logos
  #   content:
  #     title: Section Title
  #     subtitle: Section Subtitle
  #     # Path to the logo images within the `assets/media/` folder
  #     logo_folder: logos
  #   design:
  #     columns: '1'  
---