import logging
import asyncio
from playwright.async_api import async_playwright
from app.models import FronteraRecord


logging.basicConfig(
    filename="app/logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def procesar_frontera(record: FronteraRecord, max_retries: int = 3, delay: int = 5):
    """
    Aca estoy automatizando la creacion de fronteras en mx con fallbacks (intentos de reintento).
    """
    attempt = 0
    while attempt < max_retries:
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context()
                page = await context.new_page()

                #Inhreso a "mx" y hago login
                logging.info("Iniciando login en la plataforma XM")
                await page.goto("http://127.0.0.1:5501/")
                await page.fill('input[name="username"]', "xm_usuario") 
                await page.fill('input[name="password"]', "xm_contr") 
                await page.click('button[type="submit"]')
                
                #Esperara alerta para saber si se hizo correctamente el login
                # await page.wait_for_selector('text=Dashboard', timeout=5000)
                
                # 2. Navegar al formulario de creación de frontera
                logging.info("Navegando al formulario de mx")
                await page.goto("http://127.0.0.1:5501/dashboard.html")

                #click en crear para que se vea el formulario
                await page.wait_for_selector('#btnCrear', state='visible')
                await page.click('#btnCrear')
                logging.info("Botón 'Crear Frontera' presionado.")
                
                # Esperar a que el formulario se muestre
                await page.wait_for_selector('#formSection', state='visible')
                logging.info("Formulario visible. Comenzando a llenar los campos.")
            
                # Requerimiento
                await page.fill('input[name="tipoFroontera"]', record.requerimiento.tipoFroontera)
                await page.fill('input[name="requerimiento"]', record.requerimiento.requerimiento)
                await page.fill('input[name="contacto"]', record.requerimiento.contacto)
                await page.fill('input[name="fechaSolicitudRegistro"]', record.requerimiento.fechaSolicitudRegistro)
                await page.fill('input[name="fechaPosibleRegistro"]', record.requerimiento.fechaPosibleRegistro)
                await page.fill('input[name="representanteFrontera"]', record.requerimiento.representanteFrontera)
                await page.select_option('select[name="tipoRequerimiento"]', record.requerimiento.tipoRequerimiento)

                # Frontera
                await page.fill('input[name="nombreFronteraComercial"]', record.frontera.nombreFronteraComercial)
                await page.fill('input[name="pais"]', record.frontera.pais)
                await page.fill('input[name="departamento"]', record.frontera.departamento)
                await page.fill('input[name="ciudad"]', record.frontera.ciudad)
                await page.fill('input[name="centroPoblado"]', record.frontera.centroPoblado)
                await page.fill('input[name="longitud"]', record.frontera.longitud)
                await page.fill('input[name="latitud"]', record.frontera.latitud)
                await page.fill('input[name="altitud"]', record.frontera.altitud)
                await page.fill('input[name="tipoModelo"]', record.frontera.tipoModelo)
                await page.fill('input[name="codigoSic"]', record.frontera.codigoSic)
                await page.fill('input[name="operadorRed"]', record.frontera.operadorRed)
                await page.fill('input[name="mercadoDecComercializacion"]', record.frontera.mercadoDecComercializacion)
                await page.fill('input[name="tensionPuntoMedida"]', record.frontera.tensionPuntoMedida)
                await page.fill('input[name="nivelTension"]', record.frontera.nivelTension)
                await page.select_option('select[name="usuarioConectadoStn"]', record.frontera.usuarioConectadoStn)

                # Usuario
                await page.fill('input[name="nit"]', record.usuario.nit)
                await page.fill('input[name="razonSocial"]', record.usuario.razonSocial)
                await page.fill('input[name="ciiuTipo"]', record.usuario.ciiuTipo)
                await page.fill('input[name="codioCiiu"]', record.usuario.codioCiiu)
                await page.fill('input[name="niu"]', record.usuario.niu)

                # Equipos de Medida
                await page.fill('input[name="numeroSerie"]', record.ewquiposDeMedida.numeroSerie)
                await page.select_option('select[name="sBidireccional"]', record.ewquiposDeMedida.esBidireccional)
                await page.fill('input[name="tipoContador"]', record.ewquiposDeMedida.tipoContador)
                await page.fill('input[name="modelo"]', record.ewquiposDeMedida.modelo)
                await page.fill('input[name="marca"]', record.ewquiposDeMedida.marca)
                await page.fill('input[name="empresaRealizoCalibracion"]', record.ewquiposDeMedida.empresaRealizoCalibracion)
                await page.fill('input[name="numElementoUsados"]', record.ewquiposDeMedida.numElementoUsados)
                await page.fill('input[name="tipoPuntoMedicion"]', record.ewquiposDeMedida.tipoPuntoMedicion)
                await page.fill('input[name="fechcaCalibnracion"]', record.ewquiposDeMedida.fechcaCalibnracion)
                await page.fill('input[name="claseContador"]', record.ewquiposDeMedida.claseContador)
                await page.fill('input[name="claseTransofrmadorPotencial"]', record.ewquiposDeMedida.claseTransofrmadorPotencial)
                await page.fill('input[name="claseTransformadorCorriente"]', record.ewquiposDeMedida.claseTransformadorCorriente)

                # Curva Típica
                await page.fill('input[name="dia"]', record.curvaTipica.dia)
                await page.fill('input[name="periodo"]', record.curvaTipica.periodo)
                await page.fill('input[name="valor"]', record.curvaTipica.valor)

                # Certificaciones
                await page.select_option('select[name="SIC200"]', record.certificaciones.SIC200)
                await page.select_option('select[name="SIC156"]', record.certificaciones.SIC156)
                await page.select_option('select[name="SIC157"]', record.certificaciones.SIC157)
                await page.select_option('select[name="esNueva"]', record.certificaciones.esNueva)
                await page.select_option('select[name="esPorCambioDeUbicacion"]', record.certificaciones.SesPorCambioDeUbicacion)
                await page.select_option('select[name="SIC058"]', record.certificaciones.SIC058)
                await page.select_option('select[name="SIC108"]', record.certificaciones.SIC108)

                # Adjuntos (simulación: se usan rutas o nombres de archivos)
                await page.fill('input[name="certificadoCalibracion"]', record.adjuntos.certificadoCalibracion)
                await page.fill('input[name="plantillaEquiposMedida"]', record.adjuntos.plantillaEquiposMedida)
                await page.fill('input[name="pazYSalvo"]', record.adjuntos.pazYSalvo)

                # Enviar el formulario
                await page.click('button[type="submit"]')
                logging.info("Formulario enviado.")

                # Esperar el mensaje de éxito
                await page.wait_for_selector('text=Frontera creada exitosamente', timeout=5000)

                await browser.close()

                logging.info(f"Frontera {record.requerimiento.requerimiento} registrada exitosamente.")
                return f"Frontera {record.requerimiento.requerimiento} registrada exitosamente."
        except Exception as e:
            logging.error(f"Intento {attempt + 1} fallido: {str(e)}")
            attempt += 1
            await asyncio.sleep(delay)
    raise Exception(f"No se pudo registrar la frontera {record.requerimiento.requerimiento} después de {max_retries} intentos.")
