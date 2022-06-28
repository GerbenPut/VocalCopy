from __future__ import absolute_import, division, print_function
from tabnanny import verbose
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from tensorflow import keras
from tensorflow.keras import layers

ffdata = np.genfromtxt('ffdata.csv', delimiter=',')
fftrain = ffdata[:len(ffdata)*7//10]
fftest = ffdata[len(ffdata)*7//10:]
wavdata = np.genfromtxt('wavdata.csv', delimiter=',')
wavtrain = wavdata[:len(wavdata)*7//10]
wavtest = wavdata[len(wavdata)*7//10:]
y_data = np.genfromtxt('labels.txt')
cats = max(y_data)+1
y_data = np.array([np.array([i,i]) for i in y_data])
y_train  = y_data[:len(y_data)*7//10]
y_test = y_data[len(y_data)*7//10:]

normalizer = StandardScaler()
classifier = OneHotEncoder()
fftrain_norm = normalizer.fit_transform(fftrain)
fftest_norm = normalizer.fit_transform(fftest)
wavtrain_norm = normalizer.fit_transform(wavtrain)
wavtest_norm = normalizer.fit_transform(wavtest)
X_train = np.array([[ff, wav] for ff, wav in zip(fftrain_norm, wavtrain_norm)])
X_test = np.array([[ff, wav] for ff, wav in zip(fftest_norm, wavtest_norm)])

input = keras.Input(shape=(2, 44100), name='input')
flatten = layers.Flatten()(input)
subcomponents = layers.Dense(28, activation='relu', name='subcomponents')(flatten)
components = layers.Dense(8, activation='relu', name='components')(subcomponents)
categories = layers.Dense(3, activation='relu', name='categories')(components)
output = layers.Dense(cats, activation='softmax', name='output')(categories)
model = keras.Model(inputs=input, outputs=output, name="voice_classifier")

model.summary()

epochs, learning_rate = (4000, 0.003)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=["accuracy"])
run_hist = model.fit(X_train, y_train, batch_size=500, epochs=epochs)
test_scores = model.evaluate(X_test, y_test, verbose=2)