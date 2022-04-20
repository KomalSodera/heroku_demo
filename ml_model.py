import pickle
import numpy as np


def model_prediction(Weight,Length1,Length2,Length3,Height,Width):

    # import the classifier pickle object
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    X_new = np.array([[Weight,Length1,Length2,Length3,Height,Width]])

    prediction = model.predict(X_new)
    print(prediction)

    species = ['Bream', 'Parkki', 'Perch', 'Pike', 'Roach', 'Smelt', 'Whitefish']

    result = species[int(prediction)]

    #print(result)

    return result


if __name__ == '__main__':
    print(model_prediction(242.0,23.2,25.4,30.0,11.5200,4.0200))
