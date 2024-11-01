# Updates to keyboard shortcuts … On Thursday 1 August 2024, Drive keyboard shortcuts will be updated to give you first-letter navigation.Learn more
from flask import Flask, render_template, request

from utils import SpeciesFlower

app = Flask(__name__)

@app.route("/") 
def hello_flask():
    print("Species Found")   
    return render_template("index.html")

@app.route("/predict_species", methods = ["POST", "GET"])

def species_info():
    if request.method == "GET":
        print("GET Method")

        SepalLengthCm = eval(request.args.get('SepalLengthCm'))
        SepalWidthCm = eval(request.args.get('SepalWidthCm'))
        PetalLengthCm = eval(request.args.get('PetalLengthCm'))
        PetalWidthCm  = eval(request.args.get('PetalWidthCm'))

        three_species = SpeciesFlower(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)

        species_pred = three_species.get_predicted_species()

        if species_pred == 'Iris-setosa':
            species_pred = "Predicted SPECIES of FLOWER Is --> IRIS-SETOSA"
        elif species_pred == 'Iris-versicolor':
            species_pred = "Predicted SPECIES of FLOWER Is --> IRIS-VERSICOLOR"
        else:
            species_pred = "Predicted SPECIES of FLOWER Is --> IRIS-VIRGINICA"


        return render_template("index.html", prediction = species_pred)
    
if __name__ == "__main__":
    app.run()