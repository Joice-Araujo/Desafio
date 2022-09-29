from flask import Flask, render_template

app = Flask("__name__")

@app.route ("/")
def Home():
    return render_template("Home.html")

@app.route ("/QuemSomos")
def QuemSomos():
    return render_template("QuemSomos.html")

@app.route ("/Contato")
def Contato():
    return render_template("Contato.html")

if __name__=="__main__":
    app.run(debug=True)
   
    