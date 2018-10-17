# -*- coding: UTF-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

#�_�~�[�f�[�^
data = np.random.random((1000, 784))
labels = np.random.randint(10, size=(1000, 1))
labels = to_categorical(labels, 10)#���x���̕ϊ�

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=784))
model.add(Dense(64, activation='relu')
model.add(Dense(10, activation='softmax'))

#���f���̃R���p�C��
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
#�w�K���s��
model.fit(data, labels)