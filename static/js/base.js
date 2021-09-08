
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
let avgReviewContainer = document.querySelectorAll(".child-holder-filled");
for (let container of Array.from(avgReviewContainer)) {
    let avgReviewWidth = container.firstElementChild.textContent/5*100;
    if (avgReviewWidth) {
        container.style.width = avgReviewWidth + '%';
    } else {
        container.style.width = '0';
    };
};

function myDateTimeFormatter(isoDate) {
    let months = [
    'January',
    'February', 
    'March', 
    'April', 
    'May', 
    'June', 
    'July', 
    'August', 
    'September', 
    'October', 
    'November', 
    'December'
    ]
    let nodeDate = new Date(isoDate);
    let theYear = nodeDate.getFullYear();
    let theMonth = months[nodeDate.getMonth()];
    let theDay = nodeDate.getDate();
    let simpleHour = nodeDate.getHours();
    let theHour = hourConverter(simpleHour);
    let theMinute = (nodeDate.getMinutes()<10?'0':'') + nodeDate.getMinutes();
    
    return {
        year: theYear,
        month: theMonth,
        day: theDay,
        hour: theHour['hour'],
        minutes: theMinute,
        follower: theHour['follower']
    };
};

function hourConverter(time) {
    if (time == 0) {
        return {hour: 12, follower: 'a.m.'};
    } else if (0 < time && time <= 11) {
        return {hour: time, follower: 'a.m.'};
    } else if (time == 12) {
        return {hour: time, follower: 'p.m.'};
    } else {
        return {hour: time-12, follower: 'p.m.'};
    }
};
