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
      - title: Welcome to **Cyber** Phycical and Ro**botics** Lab
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
          text: Explore Our Research Projects
          url: ../Project/
      - title: Join Us
        content: 
        align: left
        background:
          image:
            filename: contact.jpg
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
      interval: 5000      

  - block: collection
    content:
      title: Recent News
      subtitle:
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
      view: card
      columns: '1'
  - block: portfolio
    id: projects
    content:
      title: Research
      filters:
        folders:
          - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      buttons:
        - name: All
          tag: '*'
        - name: Deep Learning
          tag: Deep Learning
        - name: Other
          tag: Demo
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
      view: showcase
      # For Showcase view, flip alternate rows?
      flip_alt_rows: false
     
  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - publication
        featured_only: true
      text: |-
        {{% callout note %}}
        See all [publications](./publication/).
        {{% /callout %}}
    design:
      columns: '2'
      view: card
  

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
      count: 0
    design:
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 1.0
      font_size_max: 3.0
      columns: 1
  # - block: markdown
  #   content:
  #     title: Gallery
  #     subtitle: ''
  #     text: |-
  #       {{< gallery album="demo" >}}
  #   design:
  #     columns: '1'
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
  #   design:
  #     columns: '2'
---