from flask import Flask, render_template, request, send_file
import json
import pandas as pd
import subprocess
import io
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':

        data = request.form.to_dict()

        #form data to JSON
        json_data = json.dumps(data, indent=4)

        with open("generation_config.json", "w") as outfile:
            outfile.write(json_data)

        #running generation
        subprocess.call(['python', 'run_generation.py'])

        time = np.load("time.npy")
        signal = np.load("signal.npy")

        data = {
            "time" : time,
            "signal" : signal
        }

        df = pd.DataFrame(data)

        df.to_csv("output/ecg.csv")

        # Pobierz plik CSV
        return send_file('output/ecg.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)