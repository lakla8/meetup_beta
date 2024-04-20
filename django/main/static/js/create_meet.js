function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', function () {
    let form = document.getElementById('restaurant-filter-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        sendData();
    });
});

function sendData() {
    let features = document.querySelector('select[name="features"]').value;
    let cuisine = document.querySelector('select[name="cuisine"]').value;
    let client = {
        'features': features,
        'cuisine': cuisine
    };

    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    var theUrl = "/fakefastapi/";
    xmlhttp.open("POST", theUrl);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.setRequestHeader('X-CSRFTOKEN', csrftoken);
    xmlhttp.send(JSON.stringify(client));
}