11-A.M
# Eng sodda Perceptron (AND mantiqiy funksiyasi)
import numpy as np

# Kirish ma'lumotlari (AND truth table)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Kutilgan chiqishlar
y = np.array([0, 0, 0, 1])

# Boshlang'ich og'irliklar va bias
w = np.zeros(2)
b = 0

# O'rganish tezligi
lr = 1

# Aktivatsiya funksiyasi
def step_function(z):
    return 1 if z >= 0 else 0

# O'qitish (training)
epochs = 10

for epoch in range(epochs):
    print(f"\nEpoch {epoch+1}")
    for i in range(len(X)):
        z = np.dot(X[i], w) + b
        y_pred = step_function(z)
        error = y[i] - y_pred
        
        # Og'irliklarni yangilash
        w = w + lr * error * X[i]
        b = b + lr * error
        
        print(f"X={X[i]}, y={y[i]}, y_pred={y_pred}, w={w}, b={b}")

print("\nYakuniy natija:")
print("Og'irliklar:", w)
print("Bias:", b)

# Tekshirish
print("\nTekshiruv:")
for i in range(len(X)):
    z = np.dot(X[i], w) + b
    print(f"{X[i]} -> {step_function(z)}")

12 MASHG'ULOT

import numpy as np

# Sigmoid funksiyasi
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Sigmoid hosilasi
def sigmoid_derivative(x):
    return x * (1 - x)

# Kirish ma'lumotlari
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Chiqish (AND)
y = np.array([[0], [0], [0], [1]])

# Boshlang'ich og'irliklar
np.random.seed(1)
w = np.random.rand(2, 1)
b = np.random.rand(1)

# O‘rganish tezligi
lr = 0.5

# O‘qitish
epochs = 5000
for epoch in range(epochs):
    # ===== Oldinga siljish =====
    z = np.dot(X, w) + b
    y_pred = sigmoid(z)

    # ===== Xato =====
    error = y - y_pred

    # ===== Orqaga siljish =====
    d_pred = error * sigmoid_derivative(y_pred)

    # Og'irliklarni yangilash
    w += lr * np.dot(X.T, d_pred)
    b += lr * np.sum(d_pred)

# Natija
print("Yakuniy og'irliklar:\n", w)
print("Bias:\n", b)

# Tekshiruv
print("\nNatijalar:")
for i in range(len(X)):
    print(X[i], "->", round(y_pred[i][0]))


13- AMALIY.M

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

# Ma'lumotlarni yuklash
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalizatsiya
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# CNN model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Kompilyatsiya
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# O'qitish
model.fit(X_train, y_train, epochs=3, batch_size=64)

# Baholash
loss, accuracy = model.evaluate(X_test, y_test)

print("CNN Xatolik (Loss):", loss)
print("CNN Aniqlik (Accuracy):", accuracy)


from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Ma'lumotlar
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000)

# Padding
X_train = pad_sequences(X_train, maxlen=100)
X_test = pad_sequences(X_test, maxlen=100)

# RNN model
model = Sequential([
    Embedding(10000, 32, input_length=100),
    SimpleRNN(32),
    Dense(1, activation='sigmoid')
])

# Kompilyatsiya
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# O'qitish
model.fit(X_train, y_train, epochs=3, batch_size=64)

# Baholash
loss, accuracy = model.evaluate(X_test, y_test)

print("RNN Xatolik (Loss):", loss)
print("RNN Aniqlik (Accuracy):", accuracy)




