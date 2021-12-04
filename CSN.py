#Este programa serve como demonstrativo da utilização do app que estamos propondo
#Todos os valores nele são demonstrativos, ou seja, não representam a realidade completamente
#No app propriamente dito, teremos integração avançada, UX de qualidade, e confiabilidade nas operações

from datetime import datetime
from random import uniform
hoje = datetime.datetime.today()

print("Bom dia! Sou a Cisnei, sua assistente virtual para reciclagem de aço :) ")

tipo = input("Primeiro, escolha uma opão: \n 1) Sou Cooperativa \n 2) Sou Cliente que deseja reciclar \n 3) Checar meus dados \n 4) Saiba mais do Projeto Cisnei")

if tipo == 1:
	cadastro = input("Informe seu CPF ou CNPJ:")
	total_rec = random.uniform(0.5, 134.18) #No programa real, teremos uma associação correta com uma database de cadastros e o total já fornecido
	print ("Você já nos forneceu",total_rec,"kg! Parabéns!")
	kg_p = input("Informe para a gente  o peso total que irá fornecer:")
	if hoje.day() > 15:
		print ("Você poderá entregar seus", kg_p ,"entre os dias 19 e 30 do mês", hoje.month() + 1, " .")
	else:
 	  print ("Você poderá entregar seus", kg_p ,"entre os dias 19 e 30 deste mês")
	print ("Agora você terá contribuído com", kg_p + total_rec," kg. Uau!" )

elif tipo == 2: #Doméstica
	cadastro = input("Informe seu CPF ou CNPJ:")
	total_rec = uniform(0.4, 16.87)
	print ("Você já reciclou",total_rec,"kg! Economizando assim R$ ", total_rec*0.05," .Parabéns!")
	cidade = input("Você está em: \n 1) Volta Redonda - RJ \n 2) Araucária - PR \n 3) Porto Real - RJ")
	tipo_cliente = input("Você gostaria de: \n 1) Agendar coleta \n 2) Encontrar um posto de troca?")
	if tipo_cliente == 1 : #Agendamento
		latas_conserva = input("Quantas latas de conserva; como milho, ervilhas ou salsichas você vai reciclar?")
		latas_tinta = input ("E de de tintas de parede?")
		latas_aerosol = input ("E de sprays aerosol inserticidas?")
		dia_do_mes = hoje.day()
    	if hoje.weekday() == 1:
      		if dia_do_mes + 8 > 30:
				print ("Coleta agendada para", hoje.day + 8 - 30,"/",hoje.month() + 1," .")
		  	else:
				print ("Coleta agendada para", hoje.day + 8,"/",hoje.month()," .")
		if hoje.weekday() == 7 :#Sábado
			if dia_do_mes + 9 > 30:
				print ("Coleta agendada para", hoje.day + 9 - 30,"/",hoje.month() + 1," .")
			else:
				print ("Coleta agendada para", hoje.day + 9,"/",hoje.month()," .")
		else:
			print ("Coleta agendada para", hoje.day + 7,"/",hoje.month()," .")
        print("Agora você está reclicando um total de ", total_rec + 0.05*latas_aerosol + 3*latas_tinta + 0,4*latas_tinta" kg! Parabéns!")
	if tipo_cliente == 2 :#Coleta, nos postos eles colocarão as informações para troca de pontos
		print("Os pontos de coleta são: ")
		if cidade = 1:
			print("Galeria Extra - Rua Vinte e Três - B \n Siderurgia CSN - Rodovia Augusto Manani N° 68")
		elif cidade = 2:
			print("Pão de Açucar - Rua Cel. Fonseca N° 444 \n Pão de Açúcar Express - Rua Tácito Monteiro N° 42")
		elif cidade = 3:
			print("Rodovia Presidente Dutra N° 203 \n Rua Estevan Domingues Pedrassi N° 722")

elif tipo == 3: #Dados
	cadastro = input("Informe seu CPF ou CNPJ:")
	total_rec = random.uniform(0.4, 134.18)
	print ("Você já reciclou",total_rec,"kg! Economizando assim R$ ", total_rec*0,05" .Parabéns!")

elif tipo == 4: #Saiba mais
	print("O Projeto CiSNei é um ambicioso projeto de conscientização de reclicagem de aço, através de ações afirmativas para pontuar quem se dispoem a tal ato")
	print("Através dele, esperamos chegar à marca de mais de 2 milhões toneladas de aço reaproveitado por ano")
print("Muito obrigada por reciclar aço!")
