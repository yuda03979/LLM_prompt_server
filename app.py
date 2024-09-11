from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variables to save input data
user_message = ""
prompt_message = ""
backend_message = "Waiting for input..."

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    global user_message, prompt_message, backend_message

    # Get the user input from the form
    user_message = request.form['user_message']
    prompt_message = request.form['prompt_message']

    # Simulate backend processing and generate a response
    backend_message = f"Backend received user message: '{user_message}' and prompt: '{prompt_message}'"

    # Return JSON response
    return jsonify({
        'backend_message': backend_message
    })

if __name__ == "__main__":
    app.run(debug=True)