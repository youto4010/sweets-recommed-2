from flask import Flask, render_template, request
# from flask import Flask, render_template, request, session, redirect, url_for
# from flask_session import Session
# from question import shuffle_question, yes_1, yes_2
from facebook import input_answer
import pandas as pd
# from datetime import timedelta 

app = Flask(__name__)
# app.secret_key = 'user'
# app.config['SESSION_TYPE'] = 'filesystem'
# app.permanent_session_lifetime = timedelta(minutes=3) 
# Session(app)

# df=pd.read_csv('question.csv')
# df=df.fillna(0)

@app.route('/', methods=['GET'])
def index():
    # question_1, question_2 = shuffle_question(df)
    # session['question_1'] = question_1
    # session['question_2'] = question_2
    # return render_template('index.html',question_1=question_1, question_2=question_2)
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    # question_1 = session.get('question_1', '')
    # question_2 = session.get('question_2', '')
    
    # if request.method == 'POST':
    #     input_text = request.form['input_text']
    #     session['input_text'] = input_text
    
    # input_text = session.get('input_text', '')  # セッションからinput_textを取得

    # sweets_categoryの各要素をtext1に入れてinput_answerを呼び出し
    # input_result = input_answer(input_text)  # text2はここで未定義です
    # session['input_result'] = input_result
    # return render_template('result.html', question_1=question_1, question_2=question_2, input_text=input_text, input_result=input_result)
    if request.method == "GET":
        return render_template('result.html')
    elif request.method  == "POST":
        text = request.form["input_text"]
        print(text)
        result = input_answer(text)
        return render_template('result.html',result_sweets=result)



# @app.route('/yes_1', methods=['GET'])
# def yes_1_route():
#     results_1 = yes_1()
#     session['results_1'] = results_1
#     print(session['result_1'])
#     return redirect(url_for('result'))

# @app.route('/yes_2', methods=['GET'])
# def yes_2_route():
#     results_2 = yes_2()
#     session['results_2'] = results_2
#     return redirect(url_for('result'))

# @app.route('/complete',methods=['GET'])
# def complete():
#     result_1 = session.get('results_1', [])
#     result_2 = session.get('results_2', [])
#     input_result = session.get('input_result', [])

#     all_results = result_1+result_2+input_result
#     session['all_results'] = all_results

#     return redirect(url_for('result'))

if __name__ == "__main__":
    app.run(debug=True)