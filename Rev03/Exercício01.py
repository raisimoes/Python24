import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

total_funcionarios = 0
total_abono = 0
abonos_minimo = 0
abono_maximo = 0

salarios = []
abonos = []

while True:
    salario = float(input("Digite o valor do sálario do funcionário (Digite 0 para encerrar): "))

    if salario == 0:
        print("\n-----------------------------------")
        print("Cadastramento de salarios encerrado")
        print("-----------------------------------")
        break

    if salario > 0:
       abono = max(100, 0.2 * salario)
       total_abono += abono
       total_funcionarios += 1
   
    if abono == 100:
        abonos_minimo += 1
    if abono > abono_maximo:
        abono_maximo = abono

    salarios.append(salario)
    abonos.append(abono)

print("\nProjeção de Gastos com Abono")
print("============================")
print("Salários e Abonos de cada funcionário:")
print("======================================")
for i in range(total_funcionarios):
    salario_formatado = locale.currency(salarios[i], grouping=True)
    abono_formatado = locale.currency(abonos[i], grouping=True)
    print(f"Funcionário {i + 1}: Salário: {salario_formatado} | Abono: {abono_formatado}")

print(f"\nTotal de salários: {locale.currency(sum(salarios), grouping=True)}")
print(f"\nTotal de funcionários processados: {total_funcionarios}")
total_abono_formatado = locale.currency(total_abono, grouping=True)
print(f"Valor total a ser gasto com abonos: {total_abono_formatado}")
print(f"Número de funcionários que receberão o valor mínimo de R$ 100: {abonos_minimo}")
abono_maximo_formatado = locale.currency(abono_maximo, grouping=True)
print(f"Maior valor pago como abono: {abono_maximo_formatado}")

