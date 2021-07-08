
let buttons = document.querySelectorAll('[name=viewer_rating]');

for (let button of Array.from(buttons)) {
    button.addEventListener('change', event => {
        for (let count = 0; count < event.target.value; count++){
            buttons[count].parentNode.parentNode.style.color = 'yellow';
            buttons[count].parentNode.parentNode.style.textShadow = '0 2px 5px rgba(0, 0, 0, .5)';
        };
        for (let count = 4; count >= event.target.value; count--){
            buttons[count].parentNode.parentNode.style.color = '';
            buttons[count].parentNode.parentNode.style.textShadow = ''; 
        };
    });
};

let labels = document.querySelectorAll('#form-stars-label');

for (let label of Array.from(labels)) {
    label.addEventListener('mouseenter', event => {
        let eventTarget = event.target.getAttribute('data-counter')
        for (let count = 0; count < eventTarget; count++) {
            labels[count].className = 'bi bi-star-fill viewer-review-rating-hover';
        };
        for (let count = 4; count >= eventTarget; count--) {
            labels[count].className = 'bi bi-star-fill viewer-review-rating-no-hover';
        }
    });
    label.addEventListener('mouseleave', event => {
        for (let count = 0; count < 5; count++) {
            labels[count].className = 'bi bi-star-fill';
        };
    });
};

let nodes = document.querySelectorAll('#date-posted');
for (let node of Array.from(nodes)) {
    let dateTime = myDateTimeFormatter(node.textContent);
    node.textContent = `${dateTime['day']} ${dateTime['month']} ${dateTime['year']}, ` + 
                        `${dateTime['hour']}:${dateTime['minutes']} ${dateTime['follower']}`;
};
