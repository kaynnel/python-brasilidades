#código n funciona por causa da versão

from cpf_cnpj import Documento
from validate_docbr import CNPJ
#cpf_um = Cpf("45509415886")
#print(cpf_um)

exemplo_cnpj = "12345678000190"
exemplo_cpf = "45509415886"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(exemplo_cpf)
print(documento)
