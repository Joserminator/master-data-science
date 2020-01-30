# Used Functions to depurate and normalize FSC LOGs


def cleanstr1(line):
    for x in line:
        wFile.write(
            f[:23] + "|" +
            l.rstrip() + "--\n")


def file_log(type_err='undefined_err', msg_err):
    if type_err = "w_filepath":
        with open("process_log.txt", "+a") as flog:
            flog.writelines(systime.isoformat() +' - ' + "Ruta o archivo incorrectos \n")
    
    elif type_err = 'undefined_err':
        with open("process_log.txt", "+a") as flog:
            flog.writelines(systime.isoformat() +' - ' + "Ruta o archivo incorrectos \n")
    else:
    with open("process_log.txt", "+a") as flog:
        flog.writeline("Compruebe error " + str(err))