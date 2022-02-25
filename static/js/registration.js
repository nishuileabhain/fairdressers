const username = document.getElementById('username')
const password = document.getElementById('password')
const form = document.getElementById('registration')
const errorElement = document.getElementById('error')
// let hints = document.getElementsByClassName('inputRequirements')
// let inp = document.getElementsByClassName('input-field')


// inp.addEventListener('mouseover', (e) => {hints.style.display = "block";})


// prevent the page from getting submitted if there are errors
form.addEventListener('submit', (e) => {
    let messages = []
    if (username.value ==='' || username.value == null) {
        messages.push('Name is required')
    }

    if (password.value.length <= 6) {
        messages.push('Passwords must be longer than 6 characters')
    }

    if (password.value === 'password') {
        messages.push('That\'s a terrible password. Make a real one please.')
    }


    if (password.value === username.value) {
        messages.push('Your password needs to be different from your name, ' + username.value + '.')
    }

    if (messages.length > 0) {
            e.preventDefault()
        errorElement.innerText = messages.join(', ')

    }
})


