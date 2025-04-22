const animatedItems = document.querySelectorAll('.card');
let currentIndex = 0;

function animateNext() {
  if (currentIndex < animatedItems.length) {
    animatedItems[currentIndex].classList.add('animate');

    animatedItems[currentIndex].addEventListener('animationend', function handler(){
      animatedItems[currentIndex].removeEventListener('animationend', handler);
      currentIndex++;
      animateNext();
    });

  }
}

animateNext(); // Start the sequence