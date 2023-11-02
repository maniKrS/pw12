from flask import Flask, redirect, url_for, session
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name)
app.secret_key = 'your_secret_key'  # Replace with your secret key
google_bp = make_google_blueprint(client_id='YOUR_GOOGLE_CLIENT_ID',
                                   client_secret='YOUR_GOOGLE_CLIENT_SECRET',
                                   redirect_to='google_login')

app.register_blueprint(google_bp, url_prefix='/google_login')

@app.route('/')
def home():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/plus/v1/people/me')
    assert resp.ok, resp.text
    return f'Logged in as: {resp.json()["displayName"]}'

if __name__ == '__main__':
    app.run()
