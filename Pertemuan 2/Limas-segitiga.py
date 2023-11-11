# program aplikasi menghitung luas dan volume limas segitiga

# Pertemuan 2
# Programmer: Mohammad rizky imansyah
# Tanggal:  11 November 2023

import tkinter as tk
import math

def calculate():
    try:
        alas = float(entry_alas.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_limas = float(entry_tinggi_limas.get())
        
        volume = (alas * tinggi_segitiga * tinggi_limas) / 3
        luas_permukaan = (alas * tinggi_segitiga) + (3 * (alas * tinggi_limas) / 2)
        
        label_volume.config(text="Volume Limas Segitiga: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Limas Segitiga: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

root = tk.Tk()
root.title("Kalkulator Limas Segitiga")
root.geometry("250x250")

label_alas = tk.Label(root, text="Panjang Alas Segitiga:")
label_alas.pack()
entry_alas = tk.Entry(root)
entry_alas.pack()

label_tinggi_segitiga = tk.Label(root, text="Tinggi Segitiga:")
label_tinggi_segitiga.pack()
entry_tinggi_segitiga = tk.Entry(root)
entry_tinggi_segitiga.pack()

label_tinggi_limas = tk.Label(root, text="Tinggi Limas:")
label_tinggi_limas.pack()
entry_tinggi_limas = tk.Entry(root)
entry_tinggi_limas.pack()

calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack()

label_volume = tk.Label(root, text="")
label_volume.pack()
label_luas_permukaan = tk.Label(root, text="")
label_luas_permukaan.pack()

root.mainloop()