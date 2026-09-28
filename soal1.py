def convertstemperature(values, unit):
	if unit == "C":
		return (values * 9 / 5) + 32
	elif unit == "F":
		return (values - 32) * 5 / 9

values = float(input("Masukkan Value: "))
unit = (input("Masukkan Unit (C/F): "))
konversi = convertstemperature(values, unit)

print("Hasil konversi: ", konversi)