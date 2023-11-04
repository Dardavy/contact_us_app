const buttons = document.querySelectorAll("[data-carousel-button]")  
/* the reason we use the data attribute here instead of class is because it makes working with javascript so much easier because you dont have to worry about overlap between your classes and javascript
*/


/*
* here we loop through each of the buttons
* The forEach() method calls a function (a callback function) once for each array element*/

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const offset = button.dataset.carouselButton === "next" ? 1 : -1

    const slides = button.closest("[data-carousel]").querySelector("[data-slides]")

    const activeSlide = slides.querySelector("[data-active]")

    let newIndex = [...slides.children].indexOf(activeSlide) + offset

    if (newIndex < 0) newIndex = slides.children.length - 1

    if (newIndex >= slides.children.length) newIndex = 0

    slides.children[newIndex].dataset.active = true
    delete activeSlide.dataset.active
  })
})