
import regex
 
class Cpf:
    CPF_LENGHT = 11
    value = ''
    def __init__(self, value:str):
        error_msg = self._validate(value) 
        if error_msg != 'OK':
            raise Exception(error_msg)
        
        self.value = value

    @classmethod
    def _all_char_same(cls, param: str) -> bool:
        first_dig = param[0]
        return  param.count(first_dig) == cls.CPF_LENGHT
    
    @classmethod
    def _remove_special_chars(cls, param)->str:
        return  regex.sub(r'\D', '', param)

    @classmethod
    def _make_first_dig(cls, param)->str:
        return '0'
    
    @classmethod
    def _make_second_dig(cls, param)->str:
        return '0'

    def _validate(self, param)->str:
        param = param or ''
        if (param == ''):
            return f'CPF Vazio ou Nulo' 

        param = self._remove_special_chars(param)
        if len(param) != self.CPF_LENGHT:
            return f'CPF com tamanho diferente de {self.CPF_LENGHT}' 
        
        if self._all_char_same(param) == True:
            return f'Cpf invalido pois todos digitos sao iguais' 
        
        first_verify_dig = self._make_first_dig(param[0:9])
        if first_verify_dig != param[9]:
            return f'Primeiro digito verificador invalido' 
        
        second_verify_dig = self._make_second_dig(param[0:10])
        if second_verify_dig != param[10]:
            return f'Segundo digito verificador invalido' 

        return 'OK'
        
cpf_a_validar = '11111111100'
cpf = Cpf(cpf_a_validar) 