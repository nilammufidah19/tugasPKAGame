# Menjalankan Berdasarkan python Code
step 1 : install package yang di perlukan

```pip install -r requirements.txt```

step 2 : run code guiv3.2.py

```python guiv3.2.py```

# Menjalankan Berdasarkan GUI 

step 1 : Buka folder ```dist```

step 2 : klik 2 kali pada ```guiv3.2.exe```

# Mengubah file .py menjadi .exe

jalankan code tersebut pada command prompt

```pyinstaller --onefile --noconsole --add-data "build/assets/frame0;build/assets/frame0" --add-data "build/assets/hb.ico;build/assets" guiv3.2.py```

jika menggunakan selain windows ubah titik koma (;) menjadi titik dua (:)

pastikan posisi directory data seperti di bawah
```
guiv3.2.py
build/
└── assets/
    └── frame0/
        ├── image_1.png
        ├── image_2.png
        ├── button_1.png
        └── ...
```


credit by : ATIKA RISKA R, MAGNOLIA G R S, NILAM MUFIDAH, SOUFI R I
