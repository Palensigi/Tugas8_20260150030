# Konstanta lokasi dalam bentuk Tuple
LOKASI = ("Kampung Anggur Plumbungan", -7.828, 110.378)

# Konstanta ambang kritis dalam bentuk Tuple
# (Suhu Maksimal, Kelembaban Minimal)
AMBANG_KRITIS = (35.0, 40.0)


def hitung_tren(data_slice):
    """
    Menghitung rata-rata suhu dan kelembaban
    dari data yang sudah di-slice.
    """

    total_suhu = 0
    total_lembab = 0

    for data in data_slice:
        total_suhu += data[0]
        total_lembab += data[1]

    jumlah_data = len(data_slice)

    rata_suhu = total_suhu / jumlah_data
    rata_lembab = total_lembab / jumlah_data

    return rata_suhu, rata_lembab


def evaluasi_irigasi(rata_suhu, rata_lembab, tuple_kritis):
    """
    Mengevaluasi apakah pompa irigasi dinyalakan
    berdasarkan suhu dan kelembaban rata-rata.
    """

    suhu_max = tuple_kritis[0]
    lembab_min = tuple_kritis[1]

    if rata_suhu > suhu_max or rata_lembab < lembab_min:
        return "KRITIS: Nyalakan Pompa Irigasi!"
    else:
        return "NORMAL: Pompa Mati."