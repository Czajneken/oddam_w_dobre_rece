function filterInstitutions() {
    document.querySelectorAll('[data-step="3"] .form-group--checkbox')
        .forEach(function (element) {
        element.style.display = 'none';
    });

    let selectedCategories = Array.from(document.querySelectorAll
        ('[data-step="1"] input[name="categories"]:checked')).map(function(element) {
        return element.value;
    });

    let institutions = document.querySelectorAll
        ('[data-step="3"] .form-group--checkbox');

    institutions.forEach(function(element) {
        let categoriesInInstitutionArray = element.querySelector
            ('input[name="institution"]').className.split(' ');
        
        let institutionToShow = selectedCategories.every(function(element) {
            return categoriesInInstitutionArray.includes(element);
        });

        if (institutionToShow) {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    });
}


function submitForm() {
    document.getElementById('donation-form').submit();
}


function goToStep(step) {
    document.querySelectorAll('[data-step]')
        .forEach(function (element) {
        element.style.display = 'none';
    });
    document.querySelector('[data-step="' + step + '"]').style.display = 'block';
}


function getDataForSummary() {
    let quantity = document.querySelector('input[name="quantity"]').value;
    let institution = document.querySelector('input[name="institution"]:checked').parentNode.querySelector('.title').innerText;
    let address = document.querySelector('input[name="address"]').value;
    let city = document.querySelector('input[name="city"]').value;
    let zipCode = document.querySelector('input[name="zip_code"]').value;
    let phoneNumber = document.querySelector('input[name="phone_number"]').value;
    let pickUpDate = document.querySelector('input[name="pick_up_date"]').value;
    let pickUpTime = document.querySelector('input[name="pick_up_time"]').value;
    let pickUpComment = document.querySelector('textarea[name="pick_up_comment"]').value;

    document.getElementById('summary-quantity').innerText = quantity + ' worki';
    document.getElementById('summary-institution').innerText = 'Dla fundacji "' + institution;
    document.getElementById('summary-address').innerText = 'Ulica: ' + address;
    document.getElementById('summary-city').innerText = 'Miasto: ' + city;
    document.getElementById('summary-zip-code').innerText = 'Kod pocztowy: ' + zipCode;
    document.getElementById('summary-phone-number').innerText = 'Numer telefonu: ' + phoneNumber;
    document.getElementById('summary-pick-up-date').innerText = 'Data: ' + pickUpDate;
    document.getElementById('summary-pick-up-time').innerText = 'Godzina: ' + pickUpTime;
    document.getElementById('summary-pick-up-comment').innerText = 'Uwagi dla kuriera: ' + pickUpComment;

    goToStep(5);
}