# 3. Use o módulo string para verificar se uma string contém apenas dígitos.

import string
texto = "12345"
if all(char in string.digits for char in texto):
    print(f"A string '{texto}' contém apenas dígitos.")
else:
    print(f"A string '{texto}' não contém apenas dígitos.")