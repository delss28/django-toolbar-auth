"use strict"
new Swiper('.image-slider',{
    breakpoints: {
        '@0.75': {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        '@1.00': {
          slidesPerView: 2,
          spaceBetween: 40,
        },
        '@1.50': {
          slidesPerView: 3,
          spaceBetween: 50,
        },
    },
    autoplay: {
      delay: 5000,
    },
    navigation:{
        nextEl:'.swiper-button-next',
        prevEl:'.swiper-button-prev'
    },
    simulateTouch:false,
    
    loop:true,
    
    
});



var today = new Date().toISOString().split('T')[0];
document.getElementsByName("appointment_date")[0].setAttribute('min', today);

  
const menuButton = document.getElementById('menu-button');
const accessibilityOptions = document.getElementById('accessibility-options');

menuButton.addEventListener('click', () => {
  accessibilityOptions.style.display = accessibilityOptions.style.display === 'none' ? 'block' : 'none';
});

// Добавляем обработчики для выбора опции
const options = document.querySelectorAll('.option');
options.forEach(option => {
  option.addEventListener('click', () => {
    const scheme = option.dataset.scheme;
    applyScheme(scheme);
    
  });
});

function applyScheme(scheme) {
  // Удаляем все предыдущие классы
  document.documentElement.classList.remove('high-contrast', 'invert', 'daltonism', 'sepia', 'high-contrast-text', 'low-saturation', 'default');

  // Добавляем выбранный класс
  document.documentElement.classList.add(scheme);
}



const slides = document.querySelectorAll('.slide');
    const navButtons = document.querySelectorAll('.slider-nav button');
    let currentSlide = 0;

    function showSlide(n) {
        slides.forEach((slide, index) => {
            if (index === n) {
                slide.classList.add('active');
            } else {
                slide.classList.remove('active');
            }
        });

        navButtons.forEach((button, index) => {
            if (index === n) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });

        currentSlide = n;
    }

    navButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            showSlide(index);
        });
    });

    setInterval(() => {
        showSlide((currentSlide + 1) % slides.length);
    }, 3000);