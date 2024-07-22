import csv
import os


print('Registre aqui seus pacientes! ')
print('\n')

#condição para verificar a existência do arquivo csv
arquivo = input('Digite o nome do arquivo: ')
caminho = arquivo + '.csv'
if os.path.exists(caminho):
    
    #ediatndo o arquivo csv
    with open(caminho, 'a', encoding = 'utf8') as clientes:
        confirmacao = input('Deseja incluir pacientes na agenda? ')
        confirmacao = confirmacao.lower()
    
        while confirmacao == 'sim':
    
            nome = input('Digite o nome do paciente: ')
            nome = nome.upper()
            tratamento = input('Digite qual procedimento irá fazer: ')
            tratamento = tratamento.upper()
            data = input('Digite a data do procedimento (dia/mês/ano): ')
            hora = input('Digite o horário do procedimento: ')
            
            #criando a variavel para ediação
            writer = csv.writer(clientes)
            
            #colocando os valores nos arquivo csv
            writer.writerow ((nome, tratamento, data, hora))
            
            #confirmação para a estrutura de repetição
            confirmacao = input('Deseja incluir mais pacientes na agenda? ')
            confirmacao = confirmacao.lower()
            
else:
    
    #criando o arquivo csv
    with open (caminho, 'w', encoding = 'utf8') as clientes:

        #criando a variável para edição
        writer = csv.writer(clientes)
        #colocando valores fixos na primeira linha
        writer.writerow (('Paciente', 'Tratamento', 'Data', 'Hora'))

        #confirmação para a estrutura de repetição
        confirmacao = input('Deseja incluir pacientes na agenda? ')
        confirmacao = confirmacao.lower()

        while confirmacao == 'sim':
            
            #incluindo as informações
            nome = input('Digite o nome do paciente: ')
            nome = nome.upper()
            tratamento = input('Digite qual procedimento irá fazer: ')
            tratamento = tratamento.upper()
            data = input('Digite a data do procedimento (dia/mês/ano): ')
            hora = input('Digite o horário do procedimento: ')
            
            #colocando os valores nos arquivo csv
            writer.writerow ((nome, tratamento, data, hora))
            
            #confirmação para a estrutura de repetição
            confirmacao = input('Deseja incluir mais pacientes na agenda? ')
            confirmacao = confirmacao.lower()

    