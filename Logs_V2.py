# import re
import os

date_regex = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}:\d{3}"
print("Seleccionar fecha de fichero")
dia = input()
print(f"Seleccionando LOG del día {dia}")

# Seleccionar fichero, editar saltos línea y añadir | después del timestamp

with open(f"FSC_{dia}.log", mode="r") as file, \
	open(f"FSC_{dia}_saltopag.txt", mode="w") as wFile:
	for f in file:
		if "---" in f:
			sp = f[23:].split("---")
			for s in sp:
				wFile.write(f[:23] + "| reci -" + s.rstrip() + "---\n")

		else:
			sp = f[23:].split("---")
			for s in sp:
				wFile.write(f[:23] + "|" + s.rstrip() + "--\n")

	print("Salto de página y separador timestamp añadido")

# Ver tipo de telegrama. añadir reci- si necesita

with open(f"FSC_{dia}_saltopag.txt", mode="r") as file, open(f"FSC_{dia}_tel.txt", mode="w") as wFile:
	for lines in file:
		tel = lines[24:lines.find("|", 24)]
		if ("rec" in tel) or ("ods" in lines):
			wFile.write(lines[:24] + lines[lines.find("|", 24) - 2:])

with open(f"FSC_{dia}_tel.txt", mode="r") as file, open(f"FSC_{dia}_clean.txt", mode="w") as wFile:
	for lines in file:
		if "ve|" not in lines:
			wFile.write(lines)
print("Fichero limpio generado")

# Limpiar los ficheros auxiliares

if os.path.exists(f"FSC_{dia}_saltopag.txt"):
	os.remove(f"FSC_{dia}_saltopag.txt")
else:
	print("The file does not exist")

if os.path.exists(f"FSC_{dia}_tel.txt"):
	os.remove(f"FSC_{dia}_tel.txt")
	#os.remove(f"FSC_{dia}.log")
else:
	print("The file does not exist")
	print("Ficheros auxiliares eliminados")

# Categorizar telegramas en ficheros distintos
with open(f"FSC_{dia}_clean.txt", "r") as file, open(f"FSC_Sat.csv", "w") as wFile:
	cabecera = "TMS|TIPO|EVENTO|SALIDA\n"
	wFile.write(cabecera)
	for lines in file:
		if ("|30|3001" in lines) or ("|30|3002" in lines):
			lines.replace("|", ",")
			wFile.write(lines)
print("Fichero de saturaciones generado")

with open(f"FSC_{dia}_clean.txt", "r") as file, open(f"FSC_Paros.csv", "w") as wFile:
	cabecera = "TMS|TIPO|EVENTO|TRAMO\n"
	wFile.write(cabecera)
	for lines in file:
		if ("|30|3021" in lines) or ("|30|3024" in lines):
			lines.replace("|", ",")
			wFile.write(lines)
print("Fichero de paros generado")

with open(f"FSC_{dia}_clean.txt", "r") as file, open(f"FSC_PLC.csv", "w") as wFile:
	cabecera = "tms|tipo|pic|largo|scanned|entrance_point|entrance_state|5|6|7|8|9|10|11|12|13|14|15"
	wFile.write(cabecera)
	for lines in file:
		if "|14|" in lines:
			wFile.write(lines)
print("Fichero PLC generado")


with open(f"FSC_{dia}_clean.txt", "r") as file, open(f"FSC_10.csv", "w") as wFile:
	cabecera = ("TS_FSC,TIPO_FSC,PIC_ID,LARGO,PARCEL_SCANNER_DATA,C1,"
				"C2,C3,UPDATE_STATE,C4,PARCEL_ENTRANCE_POINT,"
				"PARCEL_ENTRANCE_STATE,PARCEL_EXIT_POINT,PARCEL_EXIT_STATE\n")
	wFile.write(cabecera)
	for lines in file:
		if "|10|" in lines:
			lines.replace("|", ",")
			wFile.write(lines.replace("|", ","))

print("Fichero de inserciones y lecturas generado")

with open(f"FSC_{dia}_clean.txt", "r") as file, open(f"FSC__20.csv", "w") as wFile:
	cabecera = "TS_FSC,TIPO_FSC,PIC_ID,LARGO,ODES,VDES,ADES,PARCEL_SCANNER_DATA,C1,C2,C3,UPDATE_STATE,C4," \
			   "PARCEL_ENTRANCE_POINT,PARCEL_ENTRANCE_STATE,PARCEL_EXIT_POINT,PARCEL_EXIT_STATE\n"
	wFile.write(cabecera)
	for lines in file:
		if "|20|" in lines:
			lines.replace("|", ",")
			wFile.write(lines.replace("|", ","))

print("Fichero de clasificación generado")

with open(f"FSC_{dia}_clean.txt", "r") as file, open(f"FSC_27.csv", "w") as wFile:
	cabecera = "TS_FSC,TIPO_FSC,PIC_ID,LARGO,PARCEL_SCANNER_DATA,C1,C2,C3,UPDATE_STATE,C4,PARCEL_ENTRANCE_POINT," \
			   "PARCEL_ENTRANCE_STATE,PARCEL_EXIT_POINT,PARCEL_EXIT_STATE\n "
	wFile.write(cabecera)
	for lines in file:
		if "|27|" in lines:
			lines.replace("|", ",")
			wFile.write(lines.replace("|", ","))
print("done")

print("Fichero lectura en colectora generado")

with open(f"FSC_{dia}_clean.txt", "r") as file, open(f"FSC_13.csv", "w") as wFile:
	cabecera = "TS_FSC,TIPO_FSC,PIC_ID,LARGO,PARCEL_SCANNER_DATA,C1,C2,C3,UPDATE_STATE,C4,PARCEL_ENTRANCE_POINT," \
			   "PARCEL_ENTRANCE_STATE,PARCEL_EXIT_POINT,PARCEL_EXIT_STATE\n"
	wFile.write(cabecera)
	for lines in file:
		if "|13|" in lines:
			lines.replace("|", ",")
			wFile.write(lines.replace("|", ","))

print("Fichero lectura en arco de recuperación generado")

print("Fin de ejecución")
# print("ejecutar saturaciones? (S/N)")
