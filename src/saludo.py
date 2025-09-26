from datetime import datetime
hora_actual = datetime.now().hour
nombre= input("Escriba su nombre")
if hora_actual<12:
    print("buenos días,", nombre)
elif 12<hora_actual<20:
    print("buenas tardes,", nombre)
elif 20< hora_actual:
    print("buenas noches,", nombre)

