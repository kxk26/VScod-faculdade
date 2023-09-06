import time


def entrar():
    login = input ("Digite o seu login:")
    senha = input ("Digite sua senha:")
    if login == "userpy01" and senha == "teste01":
        print ("Ola  userpy01")
    elif login == "userpy02" and senha == "teste02":
        print (" Ola  userpy02")
    elif login == "userpy03" and senha == "teste03":
        print (" Ola  userpy03")
    elif login == "userpy04" and senha == "teste04":
        print (" Ola  userpy04")
    elif login == "userpy05" and senha == "teste05":
        print (" Ola  userpy05")
    else:
        print("Login Falhou, verifique sua senha e tente novamente")
        time.sleep(3)
        entrar()
entrar()
    