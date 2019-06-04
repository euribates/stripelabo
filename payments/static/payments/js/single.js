function main() {
    console.log("ok, it wotks");

    var stripe = Stripe('pk_live_vK6s28I2oClOGtckptjyYn4c');

    var elements = stripe.elements();
    var cardElement = elements.create('card');
    cardElement.mount('#card-element');

    var cardholderName = document.getElementById('cardholder-name');
    var cardButton = document.getElementById('card-button');
    var clientSecret = cardButton.dataset.secret;

    cardButton.addEventListener('click', function(ev) {
    stripe.handleCardPayment(
        clientSecret, cardElement, {
        payment_method_data: {
            billing_details: {name: cardholderName.value}
        }
        }
    ).then(function(result) {
        if (result.error) {
            console.log('Error');
            console.log(result.error);
        // Display error.message in your UI.
        } else {
            console.log('Allright');
        // The payment has succeeded. Display a success message.
        }
    });
    });


    console.log("main ends");
}

main();
