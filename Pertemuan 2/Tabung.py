# program aplikasi menghitung luas dan volume tabung

# Pertemuan 2
# Programmer: Mohammad rizky imansyah
# Tanggal:  11 November 2023


import tkinter as tk
import math

def calculate():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        volume = math.pi * (jari_jari ** 2) * tinggi
        luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        label_volume.config(text="Volume Tabung: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Tabung: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

root = tk.Tk()
root.title("Kalkulator Tabung")
root.geometry("250x250")

label_jari_jari = tk.Label(root, text="Jari-Jari Tabung:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(root)
entry_jari_jari.pack()

label_tinggi = tk.Label(root, text="Tinggi Tabung:")
label_tinggi.pack()
entry_tinggi = tk.Entry(root)
entry_tinggi.pack()

calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack()

label_volume = tk.Label(root, text="")
label_volume.pack()
label_luas_permukaan = tk.Label(root, text="")
label_luas_permukaan.pack()

root.mainloop()