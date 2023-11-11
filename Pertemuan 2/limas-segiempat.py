# program aplikasi menghitung luas dan volume limas segiempat

# Pertemuan 2
# Programmer: Mohammad rizky imansyah
# Tanggal:  11 November 2023


import tkinter as tk
import math

def calculate():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi_limas = float(entry_tinggi_limas.get())
        tinggi_alas = float(entry_tinggi_alas.get())
        
        volume = (panjang * lebar * tinggi_limas) / 3
        luas_permukaan = (panjang * lebar) + (panjang * math.sqrt((lebar/2)**2 + tinggi_alas**2)) + (lebar * math.sqrt((panjang/2)**2 + tinggi_alas**2))
        
        label_volume.config(text="Volume Limas Segiempat: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Limas Segiempat: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

root = tk.Tk()
root.title("Kalkulator Limas Segiempat")
root.geometry('250x250')

label_panjang = tk.Label(root, text="Panjang Limas:")
label_panjang.pack()
entry_panjang = tk.Entry(root)
entry_panjang.pack()

label_lebar = tk.Label(root, text="Lebar Limas:")
label_lebar.pack()
entry_lebar = tk.Entry(root)
entry_lebar.pack()

label_tinggi_limas = tk.Label(root, text="Tinggi Limas:")
label_tinggi_limas.pack()
entry_tinggi_limas = tk.Entry(root)
entry_tinggi_limas.pack()

label_tinggi_alas = tk.Label(root, text="Tinggi Segitiga Alas:")
label_tinggi_alas.pack()
entry_tinggi_alas = tk.Entry(root)
entry_tinggi_alas.pack()

calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack()

label_volume = tk.Label(root, text="")
label_volume.pack()
label_luas_permukaan = tk.Label(root, text="")
label_luas_permukaan.pack()

# Memulai loop tkinter
root.mainloop()