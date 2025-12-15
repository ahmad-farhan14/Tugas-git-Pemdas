data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# no 1
print('no 1')
for lokasi, data in data_panen.items():
    print("Nama Lokasi :", data['nama_lokasi'])
    print("Hasil Panen :", data['hasil_panen'])

# no 2
print('no 2')
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print("Jumlah Hasil Panen Jagung Lokasi 2:", jagung_lokasi2)

# no 3
print("Nama Lokasi 3:", data_panen['lokasi3']['nama_lokasi'])

# no 4
padi = {}
kedelai = {}
print('no 4')
for lokasi, data in data_panen.items():
    padi[data['nama_lokasi']] = data['hasil_panen']['padi']
    kedelai[data['nama_lokasi']] = data['hasil_panen']['kedelai']

print("Data Padi    :", padi)
print("Data Kedelai :", kedelai)

# no 5
print('no.5')
for data in data_panen.values():
    padi_val = data['hasil_panen']['padi']
    jagung_val = data['hasil_panen']['jagung']

    if padi_val > 1300 or jagung_val > 800:
        print(data['nama_lokasi'], ": Memerlukan perhatian khusus")
    else:
        print(data['nama_lokasi'], ": Kondisi baik")