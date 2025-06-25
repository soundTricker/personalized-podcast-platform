import os

from ppp.settings import Settings

# Google OAuth2 endpoints
GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"


def generate_auth_url(settings: Settings, listener_id: str, scopes: list[str]):
    # Construct the redirect URI
    redirect_uri = f"{os.environ.get('API_BASE_URL', 'http://localhost:3000')}/api/v1/google-oauth2/callback"
    # Construct the authorization URL
    auth_params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": " ".join(scopes),
        "access_type": "offline",  # Request a refresh token
        "prompt": "consent",  # Force the consent screen to appear
        "state": listener_id,  # Pass the user ID as state to retrieve it in the callback
    }
    auth_url = f"{GOOGLE_AUTH_URL}?{'&'.join(f'{k}={v}' for k, v in auth_params.items())}"
    return auth_url
