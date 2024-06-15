from flask import Flask, request, jsonify
import pyperclip
import time 
import pyautogui

app = Flask(__name__)

@app.route('/paste', methods=['POST'])
def paste():
    data = request.data.decode('utf-8')
    pyperclip.copy(data)
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    return jsonify({'status':'success'}), 200

if __name__=='__main__':
    app.run(debug=True)


