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
