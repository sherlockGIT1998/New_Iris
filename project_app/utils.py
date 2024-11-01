import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config

class SpeciesFlower():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def load_models(self):

        with open(config.MODEL_FILE_PATH ,"rb") as f:
            self.logistic_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.save_data  = json.load(f)

    def get_predicted_species(self):
        
        self.load_models()

        array = np.zeros(len(self.save_data['column_names']))

        array[0] = self.SepalLengthCm
        array[1] = self.SepalWidthCm
        array[2] = self.PetalLengthCm
        array[3] = self.PetalWidthCm

        print("Test Array -->\n", array)

        species_pred = self.logistic_model.predict([array])[0]

        return species_pred
    
if __name__ == "__main__":

    SepalLengthCm = 5.1
    SepalWidthCm = 3.5
    PetalLengthCm = 1.4
    PetalWidthCm = 0.2

    three_species = SpeciesFlower(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)

    species_pred = three_species.get_predicted_species()

    print("species preddiction:",species_pred)