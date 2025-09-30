# 8. Crie uma lista com as datas de todos os dias de janeiro em um ano bissexto (considerando que um ano bissexto é divisível por 4).

datas_janeiro = [f"2020-01-{dai:02d}" for dai in range(1, 32)]
print(datas_janeiro)