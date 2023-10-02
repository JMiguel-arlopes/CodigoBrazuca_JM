
import regex

CPF_LENGHT = 11
value = ''

    
 
def all_char_same(param: str) -> bool:
    first_dig = param[0]
    return  param.count(first_dig) == CPF_LENGHT
    
def remove_special_chars(param)->str:
    return  regex.sub(r'\D', '', param)

def make_first_dig(param)->str:
    return '0'
    
def make_second_dig(param)->str:
    return '0'

def cpf_validate(param)->str:
    param = param or ''
    if (param == ''):
        return f'CPF Vazio ou Nulo' 

    param = remove_special_chars(param)
    if len(param) != CPF_LENGHT:
        return f'CPF com tamanho diferente de {CPF_LENGHT}' 
    
    if all_char_same(param) == True:
        return f'Cpf invalido pois todos digitos sao iguais' 
    
    first_verify_dig = make_first_dig(param[0:9])
    if first_verify_dig != param[9]:
        return f'Primeiro digito verificador invalido' 
    
    second_verify_dig = make_second_dig(param[0:10])
    if second_verify_dig != param[10]:
        return f'Segundo digito verificador invalido' 

    return 'OK'
        
cpf_a_validar = '1111111110'
error_msg = cpf_validate(cpf_a_validar) 
if error_msg != 'OK':
    raise Exception(error_msg)

