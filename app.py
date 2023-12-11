import pandas as pd
import processor
import os
import tempfile
from flask import Flask, render_template, request

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/", methods=["GET", "POST"])
def index():

    report = None

    if request.method == "POST":
        file = request.files["file"]

        if file and file.filename.endswith(".csv"):
            path = save_temp_file(file)
            print('Lendo arquivo salvo...')
            df = pd.read_csv(path)
            report = processor.report(df)

    return render_template("index.html", report=report)


def save_temp_file(file):
    print('Salvando arquivo temporário...')
    
    temp_dir = tempfile.mkdtemp()

    temp_path = os.path.join(temp_dir, file.filename)
    file.save(temp_path)

    return temp_path
