// Global form submission handler for Web3Forms (Silent Push / AJAX)
document.addEventListener("DOMContentLoaded", function () {
    // Find all forms that submit to Web3Forms
    const forms = document.querySelectorAll('form[action="https://api.web3forms.com/submit"]');

    forms.forEach(form => {
        // Skip the financing form as it has its own custom interception logic on its page
        if (form.id === 'financingForm') return;

        form.addEventListener('submit', function (e) {
            e.preventDefault();

            // Find the submit button
            const submitBtn = form.querySelector('button[type="submit"]') || form.querySelector('input[type="submit"]');
            const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Submit';

            // Visual feedback: disable button and change text
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = "Sending...";
            }

            // Gather all form data
            const formData = new FormData(form);

            // Extract redirect URL if present
            const redirectInput = form.querySelector('input[name="redirect"]');
            let redirectUrl = redirectInput ? redirectInput.value : null;

            // Make redirect work locally if testing
            if (redirectUrl) {
                try {
                    const urlObj = new URL(redirectUrl);
                    // Standardize to relative path so it redirects correctly regardless of local/staging/live
                    if (urlObj.hostname === 'echoavu.ca') {
                        redirectUrl = urlObj.pathname + urlObj.search;
                    }
                } catch (e) {
                    // Ignore URL parsing errors, use original string
                }
            }

            // Perform silent AJAX submission
            fetch('https://api.web3forms.com/submit', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json'
                },
                body: formData
            })
                .then(async (response) => {
                    if (response.status === 200 || response.ok) {
                        if (redirectUrl) {
                            // Redirect silently
                            window.location.href = redirectUrl;
                        } else {
                            // Show a success message inline if no redirect is specified
                            const successMsg = form.querySelector('#form-success');
                            if (successMsg) {
                                successMsg.classList.remove('hidden');
                                form.reset();
                                if (submitBtn) {
                                    submitBtn.disabled = false;
                                    submitBtn.innerHTML = originalBtnText;
                                }
                            } else {
                                // Replace form with a stylish success block
                                form.innerHTML = `
                                <div class="text-center py-10 bg-echoRed/10 border border-echoRed/30 rounded-xl">
                                    <svg class="w-12 h-12 text-echoRed mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                    </svg>
                                    <h3 class="text-white font-bold text-2xl mb-2 italic">Message Sent</h3>
                                    <p class="text-gray-400 font-body">Thank you for your inquiry. Our team will be in touch shortly.</p>
                                </div>
                            `;
                            }
                        }
                    } else {
                        console.error("Form submission failed", await response.text());
                        if (submitBtn) {
                            submitBtn.disabled = false;
                            submitBtn.innerHTML = "Error. Try Again.";
                        }
                    }
                })
                .catch(error => {
                    console.error("Form error:", error);
                    if (submitBtn) {
                        submitBtn.disabled = false;
                        submitBtn.innerHTML = "Error. Try Again.";
                    }
                });
        });
    });
});
