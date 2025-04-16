from fastapi import APIRouter, HTTPException
from app.utils import extraer_datos_crm
from app.automation import procesar_frontera
from app.models import FronteraRecord
import asyncio

router = APIRouter()

@router.post("/registrar_frontera/")
async def registrar_frontera(url_odoo: str):
    try:
        #Extraer data de oddo
        frontera_record: FronteraRecord = extraer_datos_crm(url_odoo)

        #registrar en xm
        resultado = await procesar_frontera(frontera_record)

        return {"message": resultado}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
