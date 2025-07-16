function getNewQuote() {
    fetch('/quote')
        .then(response => response.json())
        .then(data => {
            document.getElementById('quote').textContent = data.quote;
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
