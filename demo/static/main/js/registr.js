function agreeForm(f) {
    if (f.Agreement.checked) f.patronymic.disabled = 1 
    else 
    f.patronymic.disabled = 0
    patronymic=""
}