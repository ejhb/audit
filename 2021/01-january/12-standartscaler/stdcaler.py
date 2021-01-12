from sklearn.preprocessing import StandardScaler
import random

data = random.randint(0,100)
scaler = StandardScaler

print(scaler.fit(data))

StandardScaler
print(scaler.mean_)
print(scaler.transform(data))
print(scaler.transform([[2, 2]]))