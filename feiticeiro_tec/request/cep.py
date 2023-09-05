import re
from typing import Optional
from requests import get
from pydantic import BaseModel


class CepError(Exception):
    ...


class CepNotFound(CepError):
    ...


def clear_cep(cep: str):
    return re.sub(r"\D", "", str(cep))


def serializer_cep(cep: str):
    clear_cep(cep)
    if len(cep) >= 5:
        return f"{cep[:5]}{cep[5:]:0<3}"
    return cep


def mask_cep(cep: str):
    cep = clear_cep(cep)
    if len(cep) >= 5:
        return f"{cep[:5]}-{cep[5:]:0<3}"
    return cep


def get_cep(cep: str):
    cep = serializer_cep(cep)
    url = f"https://brasilapi.com.br/api/cep/v2/{cep}"
    response = get(url)
    if response.status_code == 200:
        return CepConsulta(**response.json())
    else:
        raise CepNotFound(f"CEP {mask_cep(cep)} não encontrado")


class CepCordenadas(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class CepLocation(BaseModel):
    type: Optional[str] = None
    coordinates: Optional[CepCordenadas] = None


class CepConsulta(BaseModel):
    cep: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    neighborhood: Optional[str] = None
    street: Optional[str] = None
    service: Optional[str] = None
    location: Optional[CepLocation] = None
