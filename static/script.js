function getNewQuote() {
    fetch('/quote')
        .then(response => response.json())
        .then(data => {
            document.getElementById('quote').textContent = data.quote;
        })
        .catch(error => console.error('Error fetching quote:', error));
}
