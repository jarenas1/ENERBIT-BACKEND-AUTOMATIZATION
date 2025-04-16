from pydantic import BaseModel

class Requerimiento(BaseModel):
    tipoFroontera: str
    requerimiento: str
    contacto: str
    fechaSolicitudRegistro: str   # Se puede usar datetime.date si se prefiere
    fechaPosibleRegistro: str
    representanteFrontera: str
    tipoRequerimiento: str

class Frontera(BaseModel):
    nombreFronteraComercial: str
    pais: str
    departamento: str
    ciudad: str
    centroPoblado: str
    longitud: str
    latitud: str
    altitud: str
    tipoModelo: str
    codigoSic: str
    operadorRed: str
    mercadoDecComercializacion: str
    tensionPuntoMedida: str
    nivelTension: str
    usuarioConectadoStn: str

class Usuario(BaseModel):
    nit: str
    razonSocial: str
    ciiuTipo: str
    codioCiiu: str
    niu: str

class EquiposDeMedida(BaseModel):
    numeroSerie: str
    esBidireccional: str
    tipoContador: str
    modelo: str
    marca: str
    empresaRealizoCalibracion: str
    numElementoUsados: str
    tipoPuntoMedicion: str
    fechcaCalibnracion: str
    claseContador: str
    claseTransofrmadorPotencial: str
    claseTransformadorCorriente: str

class CurvaTipica(BaseModel):
    dia: str
    periodo: str
    valor: str

class Certificaciones(BaseModel):
    SIC200: str
    SIC156: str
    SIC157: str
    esNueva: str
    esPorCambioDeUbicacion: str
    SIC058: str
    SIC108: str

class Adjuntos(BaseModel):
    certificadoCalibracion: str
    plantillaEquiposMedida: str
    pazYSalvo: str

class FronteraRecord(BaseModel):
    requerimiento: Requerimiento
    frontera: Frontera
    usuario: Usuario
    ewquiposDeMedida: EquiposDeMedida
    curvaTipica: CurvaTipica
    certificaciones: Certificaciones
    adjuntos: Adjuntos
