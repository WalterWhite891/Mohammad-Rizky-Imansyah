def konversi_ke_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    celsius_input = float(input("Masukkan suhu dalam Celsius: "))
    hasil_fahrenheit = konversi_ke_fahrenheit(celsius_input)
    print(f"{celsius_input}°C sama dengan {hasil_fahrenheit}°F")

if __name__ == "__main__":
    main()