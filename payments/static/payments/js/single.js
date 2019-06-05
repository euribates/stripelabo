function main() {
    console.log("ok, it wotks");
    console.log('button#card-button is', cardButton);

    var stripe = Stripe('pk_test_z5iKKMpHKcB2jm0iXgDrzW7p');

    var elements = stripe.elements();
    var cardButton = document.getElementById('card-button');
    var cardElement = elements.create('card');
    cardElement.mount('#card-element');

    var cardholderName = document.getElementById('cardholder-name');
    var clientSecret = cardButton.dataset.secret;

    cardButton.addEventListener('click', function(ev) {
        console.log('click on cardButton starts');
        stripe.handleCardPayment(
            clientSecret, cardElement, {
            payment_method_data: {
                billing_details: {name: cardholderName.value}
            }
        }).then(function(result) {
            if (result.error) {
                console.log('Error');
                console.log(result.error);
            // Display error.message in your UI.
            } else {
                console.log('Allright');
                console.log('result:', result);
                console.log(result.message);
            // The payment has succeeded. Display a success message.
            }
        });
    });
    console.log("main ends");
}

main();
