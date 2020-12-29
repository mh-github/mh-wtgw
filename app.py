import random
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

data_list = []
with open('data.txt', 'r') as data_file:
    data_list = data_file.readlines()

@app.route("/", methods=['GET'])
def index():     
    index = random.randint(1, len(data_list) - 1)
    clue  = data_list[index].split('|')[0]

    return render_template('game.html',
                            clue=clue.strip(),
                            index=index)

@app.route("/check")
def checkAnswer():
    ind = int(request.args.get("index"))
    ans = request.args.get("answer").strip().upper()
    correct_answer = data_list[ind].split('|')[1].strip()

    return "You got it right!" if (ans == correct_answer) else "Wrong Answer! Please try again!!"


@app.route("/show")
def showAnswer():
    ind = int(request.args.get("index"))
    return data_list[ind].split('|')[1].strip()

@app.route("/new")
def newClue():
    index = random.randint(1, len(data_list) - 1)
    clue  = data_list[index].split('|')[0].strip()
    response = {
        'index': index,
        'clue': clue
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')