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
for d in data_panen:
    print(d)

# no 2
total_jagung = 0
for d in data_panen:
    total_jagung += d["jagung"]
print("Total Jagung:", total_jagung)

# no 3
print("Nama Lokasi ke-3:", data_panen[2]["lokasi"])

# no 4
padi = {}
kedelai = {}

for d in data_panen:
    padi[d["lokasi"]] = d["padi"]
    kedelai[d["lokasi"]] = d["kedelai"]

# no 5
for d in data_panen:
    if d["padi"] > 1300 or d["jagung"] > 800:
        print(d["lokasi"], ": Memerlukan perhatian khusus")
    else:
        print(d["lokasi"], ": Kondisi baik")
