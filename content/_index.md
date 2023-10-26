---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  # - block: hero
  #   content:
  #     # video:
  #       # filename: welcome.mp4
  #     title: |
  #       Cyberbotics Lab 
  #     image:
  #       filename: 20230819_122609.jpg
  #     text: | 
  #       We are inspired to develop computationally tractable optimization-based control methodologies that unify formal control theory with advanced numerical optimization techniques and, ultimately, to realize versatile and dynamic maneuvers experimentally on a variety of robotic platforms 
  - block: slider
    content:
      slides:
      - title: __Cyber__ Phycical and Ro**botics** (Cyberbotics) Lab
        content: 
        align: center
        background:
          image:
            filename: cyberbotics-digit.gif
            filters:
              brightness: 0.4
          position: center 
          color: '#333'
        link:
          icon: robot #graduation-cap
          icon_pack: fas
          text: Explore Our Research
          url: ../projects/
      - title: __Join Us__
        content: 
        align: left
        background:
          image:
            filename: joinus.jpg
            filters:
              brightness: 0.4
          position: center
          color: '#555'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Meet Our Team
          url: ../people/
        # link:
        #   icon: graduation-cap
        #   icon_pack: fas
        #   text: Join Us
        #   url: ../contact/
      # - title: World-Class Semiconductor Lab
      #   content: 'Just opened last month!'
      #   align: right
      #   background:
      #     image:
      #       filename: welcome.png
      #       filters:
      #         brightness: 0.5
      #     position: center
      #     color: '#333'
        
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 2500      

  - block: collection
    content:
      title: Recent News
      subtitle: |-
        {{% callout hint %}}
        See all [news](./post/).
        {{% /callout %}}
      text:
      count: 3
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
      view: card-custom
      columns: '2'

  - block: collection
    id: projects
    content:
      title: Research Projects
      subtitle: |-
        {{% callout hint %}}
        See all [projects](./projects/).
        {{% /callout %}}
      filters:
        folders:
          - project
        featured_only: false
      text: 
      count: 3
    design:
      columns: '2'
      view: card-custom
      flip_alt_rows: false
     
  - block: collection
    id: featured
    content:
      title: Featured Publications
      subtitle: |-
        {{% callout hint %}}
        See all [publications](./publication/).
        {{% /callout %}}
      filters:
        folders:
          - publication
        featured_only: true
      text: 
      count: 3
    design:
      columns: '2'
      view: card-custom
  

  # - block: logos
  #   content:
  #     title: Section Title
  #     subtitle: Section Subtitle
  #     # Path to the logo images within the `assets/media/` folder
  #     logo_folder: logos
  #   design:
  #     columns: '1'  

  - block: tag_cloud
    content:
      title: Popular Topics
      # subtitle: My subtitle
      # text: Add any **markdown** formatted content here - text, images, videos, galleries - and even HTML code!
      # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
      taxonomy: tags
      # Choose how many tags you would like to display (0 = all tags)
      count: 15
    design:
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 1.0
      font_size_max: 2.0
      columns: '2'
  # - block: markdown
  #   content:
  #     title: Gallery
  #     subtitle: ''
  #     text: |-
  #       {{< gallery album="demo" >}}
  #   design:
  #     columns: 2
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
  #   design:
  #     columns: '2'
---