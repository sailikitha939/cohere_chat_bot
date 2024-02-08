from flask import Flask, render_template, request
import cohere

# Initialize Cohere client
api_key = ''
co = cohere.Client(api_key)

app = Flask(__name__)

def analyze_question(text):
    response = co.chat(text, model="command", temperature=0.0)
    answer = response.text
    return answer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        question = request.form['question']
        answer = analyze_question(question)
        return render_template('index.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
