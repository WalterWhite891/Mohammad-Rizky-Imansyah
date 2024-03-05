def konversi_ke_reamur(celsius):
    reamur = celsius * 4/5
    return reamur

def main():
    celsius_input = float(input("Masukkan suhu dalam Celsius: "))
    hasil_reamur = konversi_ke_reamur(celsius_input)
    print(f"{celsius_input}°C sama dengan {hasil_reamur}°Re")

if __name__ == "__main__":
    main()