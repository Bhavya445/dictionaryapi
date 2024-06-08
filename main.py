import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")

@app.route("/")
def home():
    return (render_template("home.html"))

@app.route("/api/v1/<word>")
def dict(word):

    return {"definition": df.loc[df["word"]==word]["definition"].squeeze(),
            "word": word
            }
if __name__ == "__main__": # website run only if main is executed directly and not imported
    app.run(debug=True,port=5001)
