// Form submission handling
document.addEventListener('DOMContentLoaded', function() {
    // Workflow tab switching
    const tabButtons = document.querySelectorAll('.tab-button');
    const workflowContents = document.querySelectorAll('.workflow-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetWorkflow = this.getAttribute('data-workflow');

            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            workflowContents.forEach(content => content.classList.remove('active'));

            // Add active class to clicked button
            this.classList.add('active');

            // Show corresponding workflow
            const targetContent = document.getElementById(`${targetWorkflow}-workflow`);
            if (targetContent) {
                targetContent.classList.add('active');
            }

            // Track workflow tab switch in analytics
            if (typeof gtag !== 'undefined') {
                gtag('event', 'workflow_tab_switch', {
                    'event_category': 'engagement',
                    'event_label': targetWorkflow
                });
            }
        });
    });

    const signupForm = document.getElementById('signup-form');

    if (signupForm) {
        signupForm.addEventListener('submit', function(e) {
            // Track signup attempt in Google Analytics
            if (typeof gtag !== 'undefined') {
                gtag('event', 'signup_attempt', {
                    'event_category': 'engagement',
                    'event_label': 'Beta Signup'
                });
            }

            // You can add custom validation or processing here
            console.log('Form submitted');
        });
    }

    // Track navigation clicks
    const navLinks = document.querySelectorAll('.nav-links a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'navigation_click', {
                    'event_category': 'engagement',
                    'event_label': this.textContent
                });
            }
        });
    });

    // Track CTA button clicks
    const ctaButtons = document.querySelectorAll('.button');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'cta_click', {
                    'event_category': 'engagement',
                    'event_label': this.textContent
                });
            }
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add intersection observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all section elements
    document.querySelectorAll('.problem-card, .solution-card, .feature-item, .use-case-card, .timeline-item').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Mobile menu toggle (if you add a hamburger menu later)
function toggleMobileMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}
