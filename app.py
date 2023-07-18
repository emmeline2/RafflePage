from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/raffle')
def raffle():
   return render_template('5050Raffle.html')

@app.route('/moveAThon')
def moveAThon():
   return render_template('MoveAThon.html')

if __name__ == '__main__':
   app.run()