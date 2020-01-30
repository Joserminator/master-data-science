import numpy as np
import pandas as pd
import datetime as dt

fe_act = str(dt.date.today().day)
systime = dt.datetime.now()

print("Seleccionando fichero del día " + fe_act)


# path = "\\172.17.50.240\Logs\FSC_"

# Se detecta, que para un mismo timestamp, a veces hay
# varias líneas separadas por "---"
# corregimos separadores faltantes y separamos líneas


try:
    with open(f"FSC_{fe_act}.log", mode="r") as file, \
            open("aux.txt", mode="w") as wFile:
        # recorre líneas, si "---", separa respetando timestamp
        for f in file:
            if "---" in f:
                line = f[23:].split("---")
                for l in line:
                    wFile.write(
                        f[:23] + "| reci -"
                        + l.rstrip() + "---\n")
                else:
                    line = f[23:].split("---")
                    for l in line:
                        wFile.write(
                            f[:23] + "|" +
                            l.rstrip() + "--\n")
        # grabamos ejecución en log
        with open("pro_log.txt", "+a") as flog:
            flog.writeline("Salto de página generado")
except (FileNotFoundError, IOError):
    with open("process_log.txt", "+a") as flog:
        flog.writelines(systime.isoformat() +' - ' + "Ruta o archivo incorrectos \n")
except Exception as err:
    with open("process_log.txt", "+a") as flog:
        flog.writeline("Compruebe error " + str(err))

