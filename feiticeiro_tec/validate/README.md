# Configurações de projeto

### Como Usar ? 
```python
from feiticeiro_tec.validate import Cnpj, Cpf, CpfCnpj, Email, InscricaoMunicipal

# Validate
print(Cnpj().validate("57.882.179/0001-75"))
print(Cpf().validate("433.391.740-91"))
print(CpfCnpj().validate("433.391.740-91"))
print(CpfCnpj().validate("57.882.179/0001-75"))
print(Email().validate("silviohenriquecruzdasilva@gmail.com"))
print(InscricaoMunicipal().validate("000.000-0"))

#Mask
print(Cnpj().mask("57882179/000175"))
print(Cpf().mask("43339174091"))
print(CpfCnpj().mask("43339174091"))
print(CpfCnpj().mask("57882179/000175"))
print(Email().mask("silviohenriquecruzdasilva@gmail.com"))
print(InscricaoMunicipal().mask("0000000"))

```

> console
```bash
True
True
True
True
True
True
57.882.179/0001-75
433.391.740-91
433.391.740-91
57.882.179/0001-75
silviohenriquecruzdasilva@gmail.com
000.000-0
```