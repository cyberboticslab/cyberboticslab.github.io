---
# Retain the CMS stub, but do not build the unused admin page.
type: wowchemycms
private: true
_build:
  render: never
  list: never
outputs:
  - HTML
---
