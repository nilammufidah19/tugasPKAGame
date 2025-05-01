import random

list_angka = [1, 2, 3, 4]
dict_warna = {
    "kp": "putih",
    "br": "biru",
    "mr": "merah"
}

rand_angka_ = random.choice(list_angka)
rand_warna_ = random.choice(list(dict_warna.keys()))
print(rand_angka_, rand_warna_)
file_name_button = f"button_{rand_warna_}{rand_angka_}.png"
print(file_name_button)
button_data = {"id":f"{rand_warna_}1{rand_angka_}", "warna": dict_warna[rand_warna_], "angka": rand_angka_}

################
button_image_31 = PhotoImage(
    file=relative_to_assets(file_name_button))
kp11 = Button(
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda: handle_button_click(kp11)
)
# button_data = {"id": "kp11", "warna": "putih", "angka": 1}
# Store all data as attributes
kp11.id = button_data["id"]
kp11.warna = button_data["warna"]
kp11.angka = button_data["angka"]