

function show_hide_password(icon) {
    const password = icon.previousElementSibling;
    if (password.type == 'password') {
        password.type = 'text'
        icon.src = '/static/images/hidePass.png'
    }
    else if (password.type == 'text') {
        password.type = 'password'
        icon.src = "/static/images/showPass.png"
    }
}
