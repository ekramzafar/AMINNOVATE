
const technologyContainer = document.querySelector('.technology-container');
let scrollAmount = 0;

function scrollTechnologies() {
  scrollAmount -= 1;
  technologyContainer.style.transform = `translateX(${scrollAmount}%)`;

  if (scrollAmount < -100) {
    scrollAmount = 0;
  }
}

setInterval(scrollTechnologies, 50);
