from flask import Flask, render_template, request, jsonify
from respond import Respond

app = Flask(__name__)
responder = Respond()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    menu = request.args.get('menu')
    payloadstr = request.args.get('payloadstr')
    reply, menu, payloadstr = responder.get_reply(msg=userText, menu=menu, payloadstr=payloadstr)
    return jsonify(reply=reply, menu=menu, payloadstr=payloadstr)

    
if __name__ == '__main__':
    app.run(debug=True)
