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


