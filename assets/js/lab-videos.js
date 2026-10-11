// All cards are readable without JavaScript; topic buttons enhance the archive.
document.querySelectorAll('[data-video-gallery]').forEach((gallery) => {
  const filters = gallery.querySelector('[data-video-filters]');
  const buttons = Array.from(filters.querySelectorAll('[data-video-topic]'));
  const cards = Array.from(gallery.querySelectorAll('[data-video-topics]'));
  const count = gallery.querySelector('[data-video-count]');

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const topic = button.dataset.videoTopic;
      let visible = 0;
      cards.forEach((card) => {
        const matches = topic === 'all' || card.dataset.videoTopics.split(/\s+/).includes(topic);
        card.hidden = !matches;
        if (matches) visible += 1;
      });
      buttons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
      count.textContent = `${visible} ${visible === 1 ? 'video' : 'videos'} · ${topic === 'all' ? 'newest first' : button.textContent.trim()}`;
    });
  });

  filters.hidden = false;
});
