function getNewQuote() {
    const quoteElement = document.getElementById('quote');
    quoteElement.classList.add('fade-out');

    fetch('/quote')
        .then(response => response.json())
        .then(data => {
            setTimeout(() => {
                quoteElement.textContent = data.quote;
                quoteElement.classList.remove('fade-out');
                quoteElement.classList.add('fade-in');
            }, 300);
        })
        .catch(error => console.error('Error fetching quote:', error));
}


function shareQuote() {
    const quoteText = document.getElementById('quote').textContent;

    if (navigator.share) {
        navigator.share({
            title: 'Daily Quote',
            text: quoteText,
            url: window.location.href
        }).then(() => {
            console.log('Quote shared successfully');
        }).catch(err => {
            console.error('Error sharing:', err);
        });
    } else {
        alert('Sharing not supported on this device. Try copying instead.');
    }
}
