// =====================================================
// 3D HOVER EFFECT
// =====================================================

const cards = document.querySelectorAll(".card");

cards.forEach((card) => {

    card.addEventListener("mousemove", (e) => {

        const rect = card.getBoundingClientRect();

        const x = e.clientX - rect.left;

        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;

        const centerY = rect.height / 2;

        const rotateX = ((y - centerY) / 20);

        const rotateY = ((centerX - x) / 20);

        card.style.transform = `
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            translateY(-8px)
        `;
    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = `
            rotateX(0deg)
            rotateY(0deg)
            translateY(0px)
        `;
    });
});

// =====================================================
// BUTTON RIPPLE EFFECT
// =====================================================

const buttons = document.querySelectorAll(".btn, .home-btn");

buttons.forEach((button) => {

    button.addEventListener("click", function (e) {

        const ripple = document.createElement("span");

        ripple.classList.add("ripple");

        this.appendChild(ripple);

        const x = e.clientX - e.target.offsetLeft;

        const y = e.clientY - e.target.offsetTop;

        ripple.style.left = `${x}px`;

        ripple.style.top = `${y}px`;

        setTimeout(() => {

            ripple.remove();

        }, 600);
    });
});

// =====================================================
// LOADING ANIMATION
// =====================================================

window.addEventListener("load", () => {

    document.body.style.opacity = "1";
});

// =====================================================
// AUTO PACK YEAR CALCULATOR
// =====================================================

const smokeday = document.querySelector('input[name="smokeday"]');

const smokeyr = document.querySelector('input[name="smokeyr"]');

const pkyr = document.querySelector('input[name="pkyr"]');

function calculatePackYears() {

    const cigs = parseFloat(smokeday.value) || 0;

    const years = parseFloat(smokeyr.value) || 0;

    const result = ((cigs / 20) * years).toFixed(1);

    pkyr.value = result;
}

if(smokeday && smokeyr && pkyr){

    smokeday.addEventListener("input", calculatePackYears);

    smokeyr.addEventListener("input", calculatePackYears);
}