#Este programa serve como demonstrativo da utilização do app que estamos propondo
#Todos os valores nele são demonstrativos, ou seja, não representam a realidade completamente
#No app propriamente dito, teremos integração avançada, UX de qualidade, e confiabilidade nas operações
#Teste, veja as operações, e veja o nosso fluxo de ideias :)

from random import uniform

print("Bom dia! Sou a Cisnei, sua assistente virtual para reciclagem de aço :) ")

cadastro = input("Primeiro, entre com seu CPF: \n")
tipo = '0'
while tipo != '5':
	tipo = input("Escolha uma opão: \n 1) Sou Cooperativa \n 2) Sou Cliente que deseja reciclar \n 3) Checar meus dados \n 4) Saiba mais do Projeto \n 5) Sair \n")

	if tipo == "1":
		total_rec = uniform(0.5, 134.18) #No programa real, teremos uma associação correta com uma database de cadastros e o total já fornecido
		total_rec = float(total_rec)
		total_rec = float("{:.3f}".format(total_rec))
		print ("Você já nos forneceu",total_rec,"kg! Parabéns!")
		kg_p = input("Informe para a gente  o peso total que irá fornecer:\n")
		print ("Você poderá entregar seus", kg_p ,"no próximo dia", int(uniform(1,30)),".\n")
		kg_p = float(kg_p)
		tot =  kg_p + total_rec
		print ("Agora você terá contribuído com", float("{:.3f}".format(tot))," kg. Uau!" )

	elif tipo == "2": #Doméstica
		total_rec = uniform(0.4, 16.87)
		total_rec = float(total_rec)
		total_rec = float("{:.3f}".format(total_rec))
		din_rec = total_rec*0.05
		din_rec = float("{:.2f}".format(din_rec))
		print ("Você já reciclou",total_rec,"kg! Economizando assim R$ ", din_rec,". Parabéns!\n")
		cidade = input("Você está em: \n 1) Volta Redonda - RJ \n 2) Araucária - PR \n 3) Porto Real - RJ\n")
		tipo_cliente = input("Você gostaria de: \n 1) Agendar coleta \n 2) Encontrar um posto de troca\n")
		if tipo_cliente == "1" : #Agendamento
			latas_conserva = input("Quantas latas de conserva; como milho, ervilhas ou salsichas você vai reciclar?\n")
			latas_tinta = input ("E de de tintas de parede?\n")
			latas_aerosol = input ("E de sprays aerosol inserticidas?\n")
			latas_tinta = int(latas_tinta)
			latas_aerosol = int(latas_aerosol)
			latas_conserva = int(latas_conserva)
			total_rec = total_rec + 0.05*latas_aerosol + 3 * latas_tinta + 0.4*latas_tinta
			total_rec = float("{:.3f}".format(total_rec))
			print("Agora você está reclicando um total de ", total_rec," kg! Parabéns!")
			coletando = int(uniform(1,30))
			print ("Coleta agendada para o próximo dia",coletando)
		if tipo_cliente == "2" :#Coleta, nos postos eles colocarão as informações para troca de pontos
			print("Os pontos de coleta são: \n")
			if cidade == "1":
				print(" Galeria Extra - Rua Vinte e Três - B \n Posto CSN - Rodovia Augusto Manani N° 68\n")
			elif cidade == "2":
				print(" Pão de Açucar - Rua Cel. Fonseca N° 444 \n Pão de Açúcar Express - Rua Tácito Monteiro N° 42\n")
			elif cidade == "3":
				print(" Rodovia Presidente Dutra N° 203 \n Rua Estevan Domingues Pedrassi N° 722\n")

	elif tipo == "3": #Dados
		total_rec = uniform(0.4, 134.18)
		total_rec = float("{:.3f}".format(total_rec))
		din_rec = total_rec * 0.05
		din_rec = float("{:.2f}".format(din_rec))
		print ("Você já reciclou",total_rec,"kg, ou seja R$",din_rec,"! Parabéns!\n")

	elif tipo == "4": #Saiba mais
		print("Este é um ambicioso projeto de conscientização de reclicagem de aço, através de ações afirmativas para pontuar quem se dispoem a tal ato\n")
		print("Através dele, esperamos chegar à marca de mais de 2 milhões toneladas de aço reaproveitado por ano\n")

print("Muito obrigada por reciclar aço!\n")

espera = input("Pressione Enter para sair")
