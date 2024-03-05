import tkinter as tk

class SuhuConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")

        # Variabel untuk menyimpan input dan hasil konversi
        self.celcius_var = tk.DoubleVar()
        self.fahrenheit_var = tk.DoubleVar()
        self.kelvin_var = tk.DoubleVar()
        self.reamur_var = tk.DoubleVar()

        # Label dan Entry untuk input Celcius
        tk.Label(root, text="Suhu (Celcius):", bg="lightgreen").grid(row=0, column=0, padx=10, pady=5)
        entry_celcius = tk.Entry(root, textvariable=self.celcius_var)
        entry_celcius.grid(row=0, column=1, padx=10, pady=5)

        # Label dan Entry untuk menampilkan hasil konversi
        tk.Label(root, text="Fahrenheit:", bg="lightgreen").grid(row=2, column=0, padx=10, pady=5)
        entry_fahrenheit = tk.Entry(root, textvariable=self.fahrenheit_var, state='readonly')
        entry_fahrenheit.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Kelvin:", bg="lightgreen").grid(row=3, column=0, padx=10, pady=5)
        entry_kelvin = tk.Entry(root, textvariable=self.kelvin_var, state='readonly')
        entry_kelvin.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Reamur:", bg="lightgreen").grid(row=4, column=0, padx=10, pady=5)
        entry_reamur = tk.Entry(root, textvariable=self.reamur_var, state='readonly')
        entry_reamur.grid(row=4, column=1, padx=10, pady=5)

        # Button untuk melakukan konversi
        btn_convert = tk.Button(root, text="Konversi", command=self.convert_suhu)
        btn_convert.grid(row=5, column=0, columnspan=2, pady=10)

    def convert_suhu(self):
        # Mengambil nilai Celcius dari entry
        suhu_celcius = self.celcius_var.get()

        # konversi
        suhu_fahrenheit = (suhu_celcius * 9/5) + 32
        suhu_kelvin = suhu_celcius + 273.15
        suhu_reamur = suhu_celcius * 4/5

        # Simpan  hasil konversi ke variabel
        self.fahrenheit_var.set(round(suhu_fahrenheit, 2))
        self.kelvin_var.set(round(suhu_kelvin, 2))
        self.reamur_var.set(round(suhu_reamur, 2))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x250")
    root.configure(bg="lightgreen")  # Menambahkan latar belakang hijau muda ke root
    root.resizable(False,False)
    app = SuhuConverterApp(root)
    root.mainloop()
