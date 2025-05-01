import random

def cari_gelas_kosong(gelas):
    return [g for g in gelas if g["status"] == "kosong"]

def cari_gelas_kosong_berwarna(gelas):
    for g in gelas:
        if g["status"] == "kosong" and g["warna"] in ["merah", "biru"]:
            return g
    return None

def cari_gelas_kosong_putih(gelas):
    for g in gelas:
        if g["status"] == "kosong" and g["warna"] == "putih":
            return g
    return None

def cari_kartu_berwarna(kartu, warna):
    return [k for k in kartu if k["warna"] == warna]

def cari_kartu_putih(kartu_dapat):
    return [k for k in kartu_dapat if k["warna"] == "putih"]

def proses_komputer(gelasmain, kartu_dapat, giliran):
    print(f"\n=== GILIRAN KE-{giliran} ===")
    print("\n--- Giliran KOMPUTER ---")

    # tampilkan_kartu(kartu_dapat)
    print("\nLangkah 1: Cari gelas kosong yang berwarna")
    gelas_target = cari_gelas_kosong_berwarna(gelasmain)
    jml_score = 0 # Inisialisasi jml_score di awal fungsi
    if gelas_target is None:
        gelas_target = cari_gelas_kosong_putih(gelasmain)
        print(f"Gelas terpilih: {gelas_target['id']} ({gelas_target['warna']})")

        print("\nLangkah 2: Karena gelas putih maka langsung cari kartu terbesar")
        print("\nLangkah 3: Cek angka tertinggi dari kartu berwarna sama")
        kartu_terpilih = max(kartu_dapat, key=lambda k: k["angka"])

        # skor = kartu_terpilih["angka"]
        # gelas_target.update({"status": "terisi", "skor": skor})
        # print(f"\nLangkah 4: Kartu terpilih adalah {kartu_terpilih['id']}, skor = {skor}")
        # jml_score=jml_score+skor
        # hapus_kartu(kartu_dapat, kartu_terpilih)
        # ambil_kartu(kartu, kartu_dapat)
        # print("\nkartu saat ini\n",kartu_dapat)

    else:
        print(f"Gelas terpilih: {gelas_target['id']} ({gelas_target['warna']})")

        print("\nLangkah 2: Cek kartu yang bewarna sama")
        kartu_sama = cari_kartu_berwarna(kartu_dapat, gelas_target["warna"])
        if kartu_sama:
            print(f"Ada kartu yang warnanya sama: {[k['id'] for k in kartu_sama]}")
            print("Menampilkan semua kartu yang warnanya sama:")
            for k in kartu_sama:
                print(f"  ID: {k['id']}, Warna: {k['warna']}, Angka: {k['angka']}")

            print("\nLangkah 3: Cek angka tertinggi dari kartu berwarna sama")
            kartu_terpilih = max(kartu_sama, key=lambda k: k["angka"])
            if kartu_terpilih["warna"] in ["merah", "biru"]:
                skor = kartu_terpilih["angka"] * 2
                print(f"\nLangkah 4: Kartu terpilih adalah {kartu_terpilih['id']}, skor x2 = {skor}")
            elif kartu_terpilih["warna"] == "putih":
                skor = kartu_terpilih["angka"]
                print(f"\nLangkah 4: Kartu terpilih adalah {kartu_terpilih['id']}, skor = {skor}")
            else:
                skor = 1
                print(f"\nLangkah 4: Kartu terpilih adalah {kartu_terpilih['id']}, skor = {skor}")
            gelas_target.update({"status": "terisi", "skor": skor})
            jml_score=jml_score+skor
            hapus_kartu(kartu_dapat, kartu_terpilih)
            ambil_kartu(kartu, kartu_dapat)
            print("\nkartu saat ini\n",kartu_dapat)
        else:
            print("\nLangkah 3: Tidak ada kartu dengan warna yang sama, cek kartu putih")
            kartu_putih = cari_kartu_putih(kartu_dapat)
            if kartu_putih:
                print(f"Ada kartu putih: {[k['id'] for k in kartu_putih]}")
                print("Menampilkan semua kartu putih:")
                for k in kartu_putih:
                    print(f"  ID: {k['id']}, Warna: {k['warna']}, Angka: {k['angka']}")

                print("\nLangkah 4: Cek angka tertinggi dari kartu putih")
                kartu_terpilih = max(kartu_putih, key=lambda k: k["angka"])
                skor = kartu_terpilih["angka"]
                gelas_target.update({"status": "terisi", "skor": skor})
                print(f"Kartu terpilih adalah {kartu_terpilih['id']}, skor = {skor}")
                jml_score=jml_score+skor
                hapus_kartu(kartu_dapat, kartu_terpilih)
                ambil_kartu(kartu, kartu_dapat)
                print("\nkartu saat ini\n",kartu_dapat)
            else:
                print("\nLangkah 4: Tidak ada kartu putih, cari gelas kosong putih")
                gelas_putih = cari_gelas_kosong_putih(gelasmain)
                if gelas_putih:
                    kartu_terpilih = max(kartu_dapat, key=lambda k: k["angka"])
                    if kartu_terpilih["warna"] in ["merah", "biru"]:
                        skor = kartu_terpilih["angka"] * 1
                    else:
                        skor = kartu_terpilih["angka"]
                    gelas_putih.update({"status": "terisi", "skor": skor})
                    print(f"Gelas putih terisi oleh {kartu_terpilih['id']}, skor = {skor}")
                    jml_score=jml_score+skor
                    hapus_kartu(kartu_dapat, kartu_terpilih)
                    ambil_kartu(kartu, kartu_dapat)
                    print("\nkartu saat ini\n",kartu_dapat)
                else:
                    print("\nLangkah 5: Tidak ada gelas putih. Pilih gelas berwarna awal dan skor akan menjadi 1")
                    gelas_target.update({"status": "terisi", "skor": 1})
                    kartu_terpilih = min(kartu_dapat, key=lambda k: k["angka"])
                    skor=1
                    print(f"Gelas {gelas_target['id']} skor = 1")
                    jml_score=jml_score+skor

                    hapus_kartu(kartu_dapat, kartu_terpilih)
                    ambil_kartu(kartu, kartu_dapat)
                    print("\nkartu saat ini\n",kartu_dapat)
    return skor