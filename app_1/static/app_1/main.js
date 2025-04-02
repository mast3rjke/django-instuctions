const LOGOUT_BTN_SELECTOR = 'logout';
const CSRF_INPUT_SELECTOR = 'csrfmiddlewaretoken';

const CSRF_VALUE = document.getElementsByName(CSRF_INPUT_SELECTOR)[0].value;
const LOGOUT_BTN = document.getElementById(LOGOUT_BTN_SELECTOR);

if (LOGOUT_BTN) {
    LOGOUT_BTN.addEventListener('click', () => {
        fetch('/admin/logout/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': CSRF_VALUE
            }
        })
            .then(() => location.reload())
            .catch((err) => console.log(err));
    });
}