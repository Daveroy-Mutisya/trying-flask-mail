from flask import Flask, render_template,request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change this to your SMTP server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'daveroy4life@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PASSWORD'] = 'fuxp ujko zpyx cqrc'
mail = Mail(app)

@app.route('/home', methods = ['GET', 'POST'])
@app.route('/',methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        msg = Message("Hey", sender='noreply@demo.com',
                      recipients=["daveroymutisya2@gmail.com"])
        msg.body = "Hey how are you? Is everything okay? This is just a Test"
        mail.send(msg)
        return "Sent Email."
    return render_template ('index.html')

if __name__ == '__main__':
    app.run(debug=  True)
