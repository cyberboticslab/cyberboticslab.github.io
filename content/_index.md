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
      - title: Welcome to Cyberbotics Lab
        content: Our research focuses on __Cyber__-Physical and Ro**botics** (Cyberbotics) systems, with a primary emphasis on bipedal walking robots.
        align: center
        background:
          image:
            filename: cyberbotics-digit.gif
            filters:
              brightness: 0.4
          position: center 
          color: '#333'
        link:
          icon: book-open-reader #graduation-cap
          icon_pack: fas
          text: Explore Our Research
          url: ../projects/
      - title: __Meet Our Team__
        content: A diverse and talented group of researchers dedicated to scientific excellence.
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
      - title: Meet Our Robots
        content: 'Uniquely equipped to support groundbreaking discoveries.'
        align: right
        background:
          image:
            filename: osu-robots.png
            filters:
              brightness: 0.4
          position: center
          color: '#555'
        link:
          icon: robot
          icon_pack: fas
          text: Robot Videos
          url: ../videos/
        
        
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 5000      

  - block: collection
    content:
      title: Recent News
      # subtitle: |-
        # {{% callout hint %}}
        # See all [news](./post/).
        # {{% /callout %}}
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
      view: compact
      columns: 1'

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
        featured_only: true
      text: 
      count: 3
    design:
      columns: '1'
      view: showcase
      flip_alt_rows: false
     
  - block: collection
    id: featured
    content:
      title: Featured Publications
      # subtitle: |-
      #   {{% callout hint %}}
      #   See all [publications](./publication/).
      #   {{% /callout %}}
      filters:
        folders:
          - publication
        featured_only: true
      text: 
      count: 5
    design:
      columns: '1'
      view: custom
  

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
      count: 20
    design:
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 0.8
      font_size_max: 2.5
      columns: '1'
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