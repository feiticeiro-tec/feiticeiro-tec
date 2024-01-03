from feiticeiro_tec.request.cep import Cep, CepConsultaV1, CepConsultaV2


def test_cep_v1():
    cep = Cep(version=1)
    consulta: CepConsultaV1 = cep.get("59380000")
    assert isinstance(consulta, CepConsultaV1)
    assert consulta.cep == "59380000"
    assert consulta.state == "RN"
    assert consulta.city == "Currais Novos"


def test_cep_v2():
    cep = Cep(version=2)
    consulta: CepConsultaV2 = cep.get("59010000")
    assert isinstance(consulta, CepConsultaV2)
    assert consulta.cep == "59010000"
    assert consulta.state == "RN"
    assert consulta.city == "Natal"
    assert consulta.neighborhood == "Praia do Meio"
    assert consulta.street == "Avenida Presidente Café Filho"
    assert consulta.location.type == "Point"
    assert consulta.location.coordinates.latitude == -5.7698204
    assert consulta.location.coordinates.longitude == -35.1960325


def test_cep_v1_not_found():
    cep = Cep(version=1)
    try:
        cep.get("00000000")
        assert False
    except cep.CepNotFound:
        assert True


def test_cep_v2_not_found():
    cep = Cep(version=2)
    try:
        cep.get("00000000")
        assert False
    except cep.CepNotFound:
        assert True


def test_cep_v1_error():
    cep = Cep(version=1)
    try:
        cep.get("0000000")
        assert False
    except cep.CepError:
        assert True


def test_cep_v2_error():
    cep = Cep(version=2)
    try:
        cep.get("0000000")
        assert False
    except cep.CepError:
        assert True
