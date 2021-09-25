
let buttons = document.querySelectorAll('[name=viewer_rating]');
let buttonSetTwo = document.querySelectorAll('[name=user_viewer_rating]');
for (let button of Array.from(buttons)) {
    button.addEventListener('change', e=> selectStarFunction(e, buttons));
};
for (let button of Array.from(buttonSetTwo)) {
    button.addEventListener('change', e => selectStarFunction(e, buttonSetTwo));
};

let labels = document.querySelectorAll('#form-stars-label');
let labelSetTwo = document.querySelectorAll('#user-review-form-stars-label');

for (let label of Array.from(labels)) {
    label.addEventListener('mouseenter', e => starHoverEnterFunction(e,'data-counter', labels));
    label.addEventListener('mouseleave', e => starHoverLeaveFunction(e, labels));
};

for (let label of Array.from(labelSetTwo)) {
    label.addEventListener('mouseenter', e => starHoverEnterFunction(e,'data-counter', labelSetTwo));
    label.addEventListener('mouseleave', e => starHoverLeaveFunction(e, labelSetTwo));
};

function selectStarFunction(event, element) {
    for (let count = 0; count < event.target.value; count++){
        element[count].parentNode.parentNode.style.color = 'yellow';
        element[count].parentNode.parentNode.style.textShadow = '0 2px 5px rgba(0, 0, 0, .5)';
    };
    for (let count = 4; count >= event.target.value; count--){
        element[count].parentNode.parentNode.style.color = '';
        element[count].parentNode.parentNode.style.textShadow = ''; 
    };
};
function starHoverEnterFunction(event, attribute, element) {
    let eventTarget = event.target.getAttribute(attribute)
    for (let count = 0; count < eventTarget; count++) {
        element[count].className = 'bi bi-star-fill viewer-review-rating-hover';
    };
    for (let count = 4; count >= eventTarget; count--) {
        element[count].className = 'bi bi-star-fill viewer-review-rating-no-hover';
    }
}
function starHoverLeaveFunction(event, element) {
    for (let count = 0; count < 5; count++) {
        element[count].className = 'bi bi-star-fill';
    };
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
