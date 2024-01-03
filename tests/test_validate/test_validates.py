from feiticeiro_tec.validate import Cnpj, Cpf, CpfCnpj, Email, InscricaoMunicipal


def test_validate_cnpj_error():
    try:
        assert Cnpj().validate("00.000.000/0000-00")
        assert False
    except ValueError:
        assert True


def test_validate_cnpj():
    assert Cnpj().validate("98.866.338/0001-25")
    assert Cnpj().validate("98.866.338/000125")
    assert Cnpj().validate("98.866.338000125")
    assert Cnpj().validate("98.866338000125")
    assert Cnpj().validate("98866338000125")


def test_validate_cpf_error():
    try:
        assert Cpf().validate("123.456.789-00")
        assert False
    except ValueError:
        assert True


def test_validate_cpf():
    assert Cpf().validate("406.365.060-02")
    assert Cpf().validate("406.365.06002")
    assert Cpf().validate("406.36506002")
    assert Cpf().validate("40636506002")


def test_validate_cpf_or_cnpj_error():
    try:
        assert CpfCnpj().validate("123.456.789-00")
        assert False
    except ValueError:
        assert True
    try:
        assert CpfCnpj().validate("00.000.000/0000-00")
        assert False
    except ValueError:
        assert True


def test_validate_cpf_or_cnpj():
    assert CpfCnpj().validate("406.365.060-02")
    assert CpfCnpj().validate("406.365.06002")
    assert CpfCnpj().validate("406.36506002")
    assert CpfCnpj().validate("40636506002")
    assert CpfCnpj().validate("98.866.338/0001-25")
    assert CpfCnpj().validate("98.866.338/000125")
    assert CpfCnpj().validate("98.866.338000125")
    assert CpfCnpj().validate("98.866338000125")
    assert CpfCnpj().validate("98866338000125")


def test_validate_email_error():
    try:
        assert Email().validate("teste@ok")
        assert False
    except ValueError:
        assert True


def test_validate_email():
    assert Email().validate("test@host.in")
    assert Email().validate("t@o.i")
    assert Email().validate("test+2@host.com")
    assert Email().validate("test28937@host.in")


def test_validate_inscricao_municipal_error():
    try:
        assert InscricaoMunicipal().validate("sadd")
        assert False
    except ValueError:
        assert True


def test_validate_inscricao_municipal():
    assert InscricaoMunicipal().validate("000.000-0")
    assert InscricaoMunicipal().validate("000.0000")
    assert InscricaoMunicipal().validate("0000000")
