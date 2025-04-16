import os
import json
import requests
from bs4 import BeautifulSoup
from app.models import FronteraRecord

def extraer_datos_crm(url: str) -> FronteraRecord:

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error al obtener la página: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extraer datos basados en selectores
    data = {
        "requerimiento": {
            "tipoFroontera": soup.find(id="tipoFroontera").text.strip(),
            "requerimiento": soup.find(id="reqNumero").text.strip(),
            "contacto": soup.find(id="contacto").text.strip(),
            "fechaSolicitudRegistro": soup.find(id="fechaSolicitudRegistro").text.strip(),
            "fechaPosibleRegistro": soup.find(id="fechaPosibleRegistro").text.strip(),
            "representanteFrontera": soup.find(id="representanteFrontera").text.strip(),
            "tipoRequerimiento": soup.find(id="tipoRequerimiento").text.strip(),
        },
        "frontera": {
            "nombreFronteraComercial": soup.find(id="nombreFronteraComercial").text.strip(),
            "pais": soup.find(id="pais").text.strip(),
            "departamento": soup.find(id="departamento").text.strip(),
            "ciudad": soup.find(id="ciudad").text.strip(),
            "centroPoblado": soup.find(id="centroPoblado").text.strip(),
            "longitud": soup.find(id="longitud").text.strip(),
            "latitud": soup.find(id="latitud").text.strip(),
            "altitud": soup.find(id="altitud").text.strip(),
            "tipoModelo": soup.find(id="tipoModelo").text.strip(),
            "codigoSic": soup.find(id="codigoSic").text.strip(),
            "operadorRed": soup.find(id="operadorRed").text.strip(),
            "mercadoDecComercializacion": soup.find(id="mercadoDecComercializacion").text.strip(),
            "tensionPuntoMedida": soup.find(id="tensionPuntoMedida").text.strip(),
            "nivelTension": soup.find(id="nivelTension").text.strip(),
            "usuarioConectadoStn": soup.find(id="usuarioConectadoStn").text.strip(),
        },
        "usuario": {
            "nit": soup.find(id="nit").text.strip(),
            "razonSocial": soup.find(id="razonSocial").text.strip(),
            "ciiuTipo": soup.find(id="ciiuTipo").text.strip(),
            "codioCiiu": soup.find(id="codioCiiu").text.strip(),
            "niu": soup.find(id="niu").text.strip(),
        },
        "ewquiposDeMedida": {
            "numeroSerie": soup.find(id="numeroSerie").text.strip(),
            "esBidireccional": soup.find(id="esBidireccional").text.strip(),
            "tipoContador": soup.find(id="tipoContador").text.strip(),
            "modelo": soup.find(id="modelo").text.strip(),
            "marca": soup.find(id="marca").text.strip(),
            "empresaRealizoCalibracion": soup.find(id="empresaRealizoCalibracion").text.strip(),
            "numElementoUsados": soup.find(id="numElementoUsados").text.strip(),
            "tipoPuntoMedicion": soup.find(id="tipoPuntoMedicion").text.strip(),
            "fechcaCalibnracion": soup.find(id="fechcaCalibnracion").text.strip(),
            "claseContador": soup.find(id="claseContador").text.strip(),
            "claseTransofrmadorPotencial": soup.find(id="claseTransofrmadorPotencial").text.strip(),
            "claseTransformadorCorriente": soup.find(id="claseTransformadorCorriente").text.strip(),
        },
        "curvaTipica": {
            "dia": soup.find(id="dia").text.strip(),
            "periodo": soup.find(id="periodo").text.strip(),
            "valor": soup.find(id="valor").text.strip(),
        },
        "certificaciones": {
            "SIC200": soup.find(id="SIC200").text.strip(),
            "SIC156": soup.find(id="SIC156").text.strip(),
            "SIC157": soup.find(id="SIC157").text.strip(),
            "esNueva": soup.find(id="esNueva").text.strip(),
            "esPorCambioDeUbicacion": soup.find(id="esPorCambioDeUbicacion").text.strip(),
            "SIC058": soup.find(id="SIC058").text.strip(),
            "SIC108": soup.find(id="SIC108").text.strip(),
        },
        "adjuntos": {
            "certificadoCalibracion": soup.find(id="certificadoCalibracion").text.strip(),
            "plantillaEquiposMedida": soup.find(id="plantillaEquiposMedida").text.strip(),
            "pazYSalvo": soup.find(id="pazYSalvo").text.strip(),
        }
    }
    return FronteraRecord(**data)
