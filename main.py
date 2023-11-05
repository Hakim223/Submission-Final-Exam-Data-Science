import requests
import json
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/rebekz/datascience_course/main/data/driver_income.json"
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
    # Membaca data JSON dari respons
    data = json.loads(response.text)

    # Mendapatkan data yang diperlukan
    income = list(map(float, data['income'].values()))
    tenure = list(map(int, data['tenure'].values()))
    avg_passenger = list(map(float, data['avg_passenger'].values()))

    # Visualisasi 1: Scatter plot income vs tenure
    plt.figure(figsize=(8, 6))
    plt.scatter(tenure, income, color='b', alpha=0.5)
    plt.xlabel('Tenure')
    plt.ylabel('Pendapatan')
    plt.title('Scatter plot Pendapatan vs Tenure')
    plt.grid(True)
    plt.savefig('scatter_plot.png')  # Simpan gambar visualisasi
    plt.show()

    # Visualisasi 2: Scatter plot income vs avg_passenger
    plt.figure(figsize=(8, 6))
    plt.scatter(avg_passenger, income, color='g', alpha=0.5)
    plt.xlabel('Rata-rata Penumpang')
    plt.ylabel('Pendapatan')
    plt.title('Scatter plot Pendapatan vs Rata-rata Penumpang')
    plt.grid(True)
    plt.savefig('scatter_plot_avg_passenger.png')  # Simpan gambar visualisasi
    plt.show()

        # Visualisasi 3: Histogram pendapatan
    plt.figure(figsize=(8, 6))
    plt.hist(income, bins=30, color='orange', alpha=0.7)
    plt.xlabel('Pendapatan')
    plt.ylabel('Frekuensi')
    plt.title('Histogram Pendapatan')
    plt.grid(True)
    plt.savefig('histogram_income.png')  # Simpan gambar visualisasi
    plt.show()

else:
    print("Gagal mengunduh data. Kode status:", response.status_code)
