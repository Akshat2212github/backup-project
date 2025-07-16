from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        message = request.form.get('message')
        try:
            response = requests.post("http://localhost:5001/receive", json={"message": message})
            if response.status_code == 200:
                result = "Message sent!"
            else:
                result = f"Failed with status {response.status_code}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(port=5000)
