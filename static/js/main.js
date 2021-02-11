var form = document.querySelector('#submit-form');
var email = document.querySelector('#email');
var address = document.querySelector('#address');
var phone = document.querySelector('#phone');



form.addEventListener('click', function() {
    console.log(email)
    email.value='';
    address.value='';
    phone.value='';
})