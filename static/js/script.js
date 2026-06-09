document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('emailForm');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const errorMessage = document.getElementById('errorMessage');
    const errorText = document.getElementById('errorText');
    const findEmailBtn = document.getElementById('findEmailBtn');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Hide previous results and errors
        results.style.display = 'none';
        errorMessage.style.display = 'none';

        // Show loading spinner
        loading.style.display = 'block';
        findEmailBtn.disabled = true;

        try {
            // Get form data
            const firstName = document.getElementById('firstName').value.trim();
            const lastName = document.getElementById('lastName').value.trim();
            const companyName = document.getElementById('companyName').value.trim();
            const showAll = document.getElementById('showAll').checked;

            // Send request to backend
            const response = await fetch('/find_email', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    first_name: firstName,
                    last_name: lastName,
                    company_name: companyName,
                    show_all: showAll
                })
            });

            const data = await response.json();

            if (response.ok) {
                // Display results
                displayResults(data);
            } else {
                // Show error
                showError(data.error || 'An unknown error occurred');
            }

        } catch (error) {
            showError('Failed to connect to the server. Please try again.');
            console.error('Error:', error);
        } finally {
            // Hide loading spinner
            loading.style.display = 'none';
            findEmailBtn.disabled = false;
        }
    });

    function displayResults(data) {
        // Show results container
        results.style.display = 'block';

        // Display best result
        const bestEmail = document.getElementById('bestEmail');
        const statusBadge = document.getElementById('statusBadge');
        const patternUsed = document.getElementById('patternUsed');
        const domainResolved = document.getElementById('domainResolved');

        bestEmail.textContent = data.best_email || 'No email found';
        patternUsed.textContent = data.pattern || 'N/A';
        domainResolved.textContent = data.domain || 'N/A';

        // Set status badge
        const status = data.status || 'invalid';
        statusBadge.textContent = getStatusText(status);
        statusBadge.className = 'status-badge status-' + status;

        // Display all candidates if requested
        const allCandidates = document.getElementById('allCandidates');
        const candidatesContainer = document.getElementById('candidatesContainer');

        if (data.candidates && data.candidates.length > 0) {
            allCandidates.style.display = 'block';
            candidatesContainer.innerHTML = '';

            data.candidates.forEach(candidate => {
                const candidateItem = document.createElement('div');
                candidateItem.className = 'candidate-item';

                const emailSpan = document.createElement('span');
                emailSpan.className = 'candidate-email';
                emailSpan.textContent = candidate.email;

                const statusSpan = document.createElement('span');
                statusSpan.className = 'candidate-status status-' + candidate.status;
                statusSpan.textContent = getStatusText(candidate.status);

                candidateItem.appendChild(emailSpan);
                candidateItem.appendChild(statusSpan);


                candidatesContainer.appendChild(candidateItem);
            });
        } else {
            allCandidates.style.display = 'none';
        }

        // Scroll to results
        results.scrollIntoView({ behavior: 'smooth' });
    }

    function showError(message) {
        errorText.textContent = message;
        errorMessage.style.display = 'block';
        errorMessage.scrollIntoView({ behavior: 'smooth' });
    }

    function getStatusText(status) {
        const statusMap = {
            'verified': '✅ Verified',
            'likely': '🟡 Likely (catch-all)',
            'invalid': '❌ Not Found'
        };
        return statusMap[status] || status;
    }
});

function copyToClipboard() {
    const bestEmail = document.getElementById('bestEmail');
    if (bestEmail && bestEmail.textContent !== 'No email found') {
        navigator.clipboard.writeText(bestEmail.textContent).then(() => {
            // Show temporary feedback
            const originalText = bestEmail.textContent;
            bestEmail.textContent = 'Copied! ' + originalText;

            setTimeout(() => {
                bestEmail.textContent = originalText;
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy: ', err);
        });
    }
}