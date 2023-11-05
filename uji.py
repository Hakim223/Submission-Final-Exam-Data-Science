import requests
import json
import pandas as pd
from scipy.stats import f_oneway

# Mengunduh data dari URL
url = "https://raw.githubusercontent.com/rebekz/datascience_course/main/data/driver_income.json"
response = requests.get(url)

# Memeriksa apakah permintaan berhasil
if response.status_code == 200:
    # Membaca data JSON dari respons
    data = json.loads(response.text)

    # Membuat DataFrame dari data
    df = pd.DataFrame(data)
    print(df)

    # Melakukan uji ANOVA
    grouped_data = [df[df['ownership'] == 'own']['income'],
                    df[df['ownership'] == 'rent']['income'],
                    df[df['ownership'] == 'other']['income']]

    print(grouped_data)
    # Melakukan uji ANOVA
    f_statistic, p_value = f_oneway(*grouped_data)

    # Menampilkan hasil uji statistik
    print("Hasil Uji ANOVA:")
    print("Nilai F-statistic:", f_statistic)
    print("Nilai p-value:", p_value)

    # Menginterpretasikan hasil uji ANOVA
    alpha = 0.05
    if p_value < alpha:
        print("Ada perbedaan signifikan dalam pendapatan antara kelompok ownership.")
    else:
        print("Tidak ada perbedaan signifikan dalam pendapatan antara kelompok ownership.")

else:
    print("Gagal mengunduh data. Kode status:", response.status_code)
