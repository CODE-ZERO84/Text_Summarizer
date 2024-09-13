from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    level = 0
    
    return render_template('text.html', level=level)

if __name__ == '__main__':
    app.run(debug=True)
    
    
