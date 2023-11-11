# program aplikasi menghitung luas dan volume kubus

# Pertemuan 2
# Programmer: Mohammad rizky imansyah
# Tanggal:  11 November 2023

import tkinter as tk

def calculate():
    try:
        sisi = float(entry_sisi.get())
        volume = sisi ** 3
        luas_permukaan = 6 * (sisi ** 2)
        label_volume.config(text="Volume Kubus: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Kubus: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

root = tk.Tk()
root.title("Kalkulator Kubus")
root.geometry("250x250")

label_sisi = tk.Label(root, text="Panjang Sisi Kubus:")
label_sisi.pack()
entry_sisi = tk.Entry(root)
entry_sisi.pack()

calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack()

label_volume = tk.Label(root, text="")
label_volume.pack()
label_luas_permukaan = tk.Label(root, text="")
label_luas_permukaan.pack()

root.mainloop()