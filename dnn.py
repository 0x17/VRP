from keras.models import Sequential
from keras.layers import Dense

import numpy as np

np.random.seed(7)

'''NUM_INPUT_FIELDS = 8

def extract_training_data(fn='pima-indians-diabetes.csv'):
    dataset = np.loadtxt(fn, delimiter=",")
    inputs = dataset[:, 0:NUM_INPUT_FIELDS]  # Zugehörige Daten (ohne Indikatorbit)
    expected_outputs = dataset[:, NUM_INPUT_FIELDS]  # Array mit Indikatorbits
    return inputs, expected_outputs


def construct_model_topology():
    model = Sequential([
        Dense(12, input_dim=NUM_INPUT_FIELDS, activation='relu'),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def train_model(model, training_data):
    inputs, expected_outputs = training_data
    model.fit(inputs, expected_outputs, epochs=40, batch_size=10, verbose=2)


def evaluate_model(model, validation_data):
    inputs, expected_outputs = validation_data
    scores = model.evaluate(inputs, expected_outputs)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))


model = construct_model_topology()
training_data = extract_training_data()
train_model(model, training_data)
#evaluate_model(model, training_data)
'''