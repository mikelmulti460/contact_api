from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get(path="/saludo/{id_usuario}")
def saludar(
    id_usuario: int,
    ubi: Union[str, None]=None,
    country: Union[str, None]=None
):
    if ubi == None:
        return "ingresa tu ubicación!"
    users_list = {10:"mikel", 11:"evelin"}
    get_user_name = users_list[id_usuario]
    return {"saludo":f"Hola usuario: {get_user_name} ----> {country}"}



#TODO: Crear un path registro -> recibe nombre, apellidos, edad, servicio, numero -> guardarlo en un archivo de texto en la ruta ./logs/users.txt
# @app.post(path="procesar_datos")
# def data():
    