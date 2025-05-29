// Update these with your actual Whop app credentials
const WHOP_CLIENT_ID = 'your_whop_client_id';
const WHOP_REDIRECT_URI = encodeURIComponent('https://your-webapp.onrender.com/auth/callback');
const WHOP_AUTH_URL = `https://whop.com/oauth/authorize?client_id=${WHOP_CLIENT_ID}&redirect_uri=${WHOP_REDIRECT_URI}&response_type=code&scope=read`;

function handleLogin() {
    window.location.href = WHOP_AUTH_URL;
}

// Add this to check for auth code in URL
function checkForAuthCode() {
    const params = new URLSearchParams(window.location.search);
    const code = params.get('code');
    
    if (code) {
        // Exchange code for token
        exchangeCodeForToken(code);
    }
}

async function exchangeCodeForToken(code) {
    try {
        const response = await fetch('/api/auth/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ code })
        });
        
        const data = await response.json();
        if (data.access_token) {
            localStorage.setItem('whop_token', data.access_token);
            checkAuthState();
        }
    } catch (error) {
        console.error('Auth error:', error);
    }
}

// Call this on page load
checkForAuthCode();