from validate_docbr import CPF, CNPJ
from .abs import AbstractValidate
from .types import CPFCNPJ, INCRICAOMUNICIPAL, EMAIL


class Cpf(AbstractValidate):
    MSG_RAISE = "CPF inválido!"
    VALIDATOR = CPF


class Cnpj(AbstractValidate):
    MSG_RAISE = "CNPJ inválido!"
    VALIDATOR = CNPJ


class CpfCnpj(AbstractValidate):
    MSG_RAISE = "CPF ou CNPJ inválido!"
    VALIDATOR = CPFCNPJ


class InscricaoMunicipal(AbstractValidate):
    MSG_RAISE = "Inscrição Municipal inválida!"
    VALIDATOR = INCRICAOMUNICIPAL


class Email(AbstractValidate):
    MSG_RAISE = "Email inválido!"
    VALIDATOR = EMAIL
