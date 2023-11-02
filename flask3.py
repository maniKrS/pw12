from flask import Flask, render_template, request

app = Flask(__name__)

# Sample content-based recommendation function
def get_recommendations(user_preferences):
    # Replace this with your recommendation algorithm
    # For simplicity, this example returns a static list of recommendations
    recommendations = ["Item 1", "Item 2", "Item 3"]
    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_preferences = request.form.get('user_preferences')
    recommendations = get_recommendations(user_preferences)
    return render_template('recomend.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
