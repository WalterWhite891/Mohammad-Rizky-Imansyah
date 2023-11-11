# program aplikasi menghitung luas dan volume balok

# Pertemuan 2
# Programmer: Mohammad rizky imansyah
# Tanggal:  11 November 2023

import tkinter as tk

def calculate():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())
        volume = panjang * lebar * tinggi
        luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
        label_volume.config(text="Volume Balok: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Balok: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

root = tk.Tk()
root.title("Kalkulator Balok")
root.geometry("250x250")

label_panjang = tk.Label(root, text="Panjang Balok:")
label_panjang.pack()
entry_panjang = tk.Entry(root)
entry_panjang.pack()

label_lebar = tk.Label(root, text="Lebar Balok:")
label_lebar.pack()
entry_lebar = tk.Entry(root)
entry_lebar.pack()

label_tinggi = tk.Label(root, text="Tinggi Balok:")
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