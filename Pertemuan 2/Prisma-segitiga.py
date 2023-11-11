# program aplikasi menghitung luas dan volume prisma segitiga

# Pertemuan 2
# Programmer: Mohammad rizky imansyah
# Tanggal:  11 November 2023

import tkinter as tk
import math

def calculate():
    try:
        alas = float(entry_alas.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_prisma = float(entry_tinggi_prisma.get())
        panjang_sisi = float(entry_panjang_sisi.get())
        
        volume = (alas * tinggi_segitiga * tinggi_prisma) / 2
        luas_permukaan = (alas * tinggi_segitiga) + (3 * panjang_sisi * tinggi_prisma)
        
        label_volume.config(text="Volume Prisma Segitiga: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Prisma Segitiga: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

root = tk.Tk()
root.title("Kalkulator Prisma Segitiga")
root.geometry("250x250")

label_alas = tk.Label(root, text="Panjang Alas Segitiga:")
label_alas.pack()
entry_alas = tk.Entry(root)
entry_alas.pack()

label_tinggi_segitiga = tk.Label(root, text="Tinggi Segitiga:")
label_tinggi_segitiga.pack()
entry_tinggi_segitiga = tk.Entry(root)
entry_tinggi_segitiga.pack()

label_tinggi_prisma = tk.Label(root, text="Tinggi Prisma:")
label_tinggi_prisma.pack()
entry_tinggi_prisma = tk.Entry(root)
entry_tinggi_prisma.pack()

label_panjang_sisi = tk.Label(root, text="Panjang Sisi Prisma:")
label_panjang_sisi.pack()
entry_panjang_sisi = tk.Entry(root)
entry_panjang_sisi.pack()

calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack()

label_volume = tk.Label(root, text="")
label_volume.pack()
label_luas_permukaan = tk.Label(root, text="")
label_luas_permukaan.pack()

root.mainloop()