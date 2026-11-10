import modul_sensor


# List untuk menyimpan data suhu dan kelembaban
log_kebun = []


def input_sensor():
    """
    Meminta input suhu dan kelembaban
    dengan validasi menggunakan try-except.
    """

    while True:
        try:
            suhu = float(input("Masukkan suhu udara (C): "))

            if suhu < 0 or suhu > 100:
                print("Suhu harus berada di antara 0-100 C.")
                continue

            kelembaban = float(input("Masukkan kelembaban tanah (%): "))

            if kelembaban < 0 or kelembaban > 100:
                print("Kelembaban harus berada di antara 0-100 %.")
                continue

            return (suhu, kelembaban)

        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


while True:
    print("\n===== SISTEM MONITORING KEBUN =====")
    print("[1] Rekam Data")
    print("[2] Analisis Tren (3 Terakhir)")
    print("[3] Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = input_sensor()

        log_kebun.append(data)

        print("Data berhasil direkam.")
        print("Data:", data)

    elif pilihan == "2":

        if len(log_kebun) == 0:
            print("Belum ada data yang direkam.")

        else:
            # Mengambil maksimal 3 data terakhir menggunakan slicing
            data_terakhir = log_kebun[-3:]

            print("\n=== 3 DATA TERAKHIR ===")

            # Menampilkan data menggunakan for
            for i, data in enumerate(data_terakhir, start=1):
                print(
                    f"Data {i}: "
                    f"Suhu = {data[0]} C, "
                    f"Kelembaban = {data[1]} %"
                )

            # Memanggil fungsi dari modul_sensor.py
            rata_suhu, rata_lembab = modul_sensor.hitung_tren(data_terakhir)

            status = modul_sensor.evaluasi_irigasi(
                rata_suhu,
                rata_lembab,
                modul_sensor.AMBANG_KRITIS
            )

            print("\n=== HASIL ANALISIS ===")
            print(f"Rata-rata suhu       : {rata_suhu:.2f} C")
            print(f"Rata-rata kelembaban : {rata_lembab:.2f} %")
            print(f"Status irigasi      : {status}")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia. Silakan pilih 1, 2, atau 3.")