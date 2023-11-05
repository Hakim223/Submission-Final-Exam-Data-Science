import requests
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Mengunduh data dari URL
url = "https://raw.githubusercontent.com/rebekz/datascience_course/main/data/driver_income.json"
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
    # Membaca data JSON dari respons
    data = json.loads(response.text)

    # Membuat DataFrame dari data
    df = pd.DataFrame(data)

    # Memilih fitur (features) dan target variable
    features = ['tenure', 'avg_passenger', 'avg_milage_normalized', 'avg_duration', 'avg_distance_normalized']
    target = 'income'

    # Memisahkan data menjadi features (X) dan target variable (y)
    X = df[features]
    y = df[target]

    # Membagi data menjadi data latih dan data uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat model regresi linear
    model = LinearRegression()

    # Melatih model menggunakan data latih
    model.fit(X_train, y_train)

    # Memprediksi pendapatan menggunakan data uji
    y_pred = model.predict(X_test)

    # Menghitung performa model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Menampilkan performa model
    print("Mean Squared Error (MSE):", mse)
    print("R-squared (R2):", r2)
else:
    print("Gagal mengunduh data. Kode status:", response.status_code)
