import csv
'''
Getting info

1 Chinese Yuan Renminbi (CNY) = 15.0789 HTG

1 USD = 97.5098 HTG

 Euro: Achat 113.3456 / Vente 113.4478
 Peso dom.: Achat 1.6976 / Vente 1.6992
 Dollar can.: Achat 75.9481 / Vente 76.0166


::need:
     usd to canada
     usd to peso
     peso to canada
     euro to usd
     euro to canada
     euro to peso

 '''
 
us_rate = 105
can_rate = 76
peso_rate = 1.7
euro_rate = 114
yen_rate = 16
us_can_rate = 1.27


def xBank_graphik():
    print("\t\t\t $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("\t\t\t $$\t\t \t\t $$")
    print("\t\t\t $$\t\t xBank \t\t $$")
    print("\t\t\t $$\t\t  \t\t $$")
    print("\t\t\t $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()

# xBank_graphik()





# #############################################################################################################
# #############################################################################################################

#  HT to USD function
# 1.1
def ht_to_us(us_rate):
    print("*****************************************************")
    print("You want to change Your Gourdes money into US")
    print()
    print("Note: The USD rate is", us_rate,"Gdes for 1 US")
    print()
    get_ht = int(input("Enter your gourdes amount: "))
    print()
    us_value = get_ht / us_rate
    print("*****************************************************")
    print(get_ht, "Gourde(s) are", round(us_value, 3), "US")
    print("*****************************************************")



# ht_to_usd()

# #############################################################################################################
# #############################################################################################################


#  USD to HT function
# 1.2
def us_to_ht(us_rate):
    print("*****************************************************")
    print("You want to change Your US money into Gourdes")
    print()
    print("Note: The USD rate is", us_rate,"Gdes for 1 US")
    print("*****************************************************")
    get_us = int(input("Enter your usd amount: "))
    ht_value = get_us * us_rate
    print()
    print("*****************************************************")
    print(get_us, "Dollar US are", round(ht_value, 3), "Gourdes")
    print("*****************************************************")

    

# #############################################################################################################
# #############################################################################################################


#  HT to Dollar Can function
# 2.3
def ht_to_can():
    print("*****************************************************")
    print("You want to change Your Gourdes money into Dollar Canadian")
    print()
    print("Note: The canada rate is", can_rate,"Gdes for 1 dollar canadian")
    print()
    print("*****************************************************")
    get_ht = int(input("Enter your gourdes amount: "))
    print()
    can_value = get_ht / can_rate
    print("*****************************************************")
    print(get_ht, "Gourdes are", round(can_value, 3), " Dollar Canadian")
    print("*****************************************************")

    

# ht_to_can()


# #############################################################################################################
# #############################################################################################################


#  Dollar Can to HT function
# 2.4
def can_to_ht():
    print("*****************************************************")
    print("You want to change Your Canadian money into Gourdes")
    print()
    print("Note: The canada rate is", can_rate,"Gdes for 1 dollar canadian")
    print("*****************************************************")
    get_can = int(input("Enter you canadian value: "))
    print()
    ht_value = get_can * can_rate
    print("*****************************************************")
    print(get_can, "Dollar Canadian are", round(ht_value, 3), " Gourdes")
    print("*****************************************************")


# can_to_ht()

# #############################################################################################################
# #############################################################################################################

# Dollar can to usd
# 3.5
def can_to_us():
    print("*****************************************************")
    print("You want to change Your Canadian money into US")
    print()
    print("The US - Canada rate is", us_can_rate)
    print()
    print("*****************************************************")
    get_can = int(input("Enter you Canadian value: "))
    print()
    us_value = get_can / us_can_rate
    print("*****************************************************")
    print(get_can, "Dollar Canadian are", round(us_value, 3), " Dollar US")
    print("*****************************************************")
# can_to_us()

# #############################################################################################################
# #############################################################################################################


# Dollar usd to can
# 3.6
def us_to_can():
    print("*****************************************************")
    print("You want to change Your US money into Dollar Canadian")
    print()
    print("The US - Canada rate is", us_can_rate)
    print()
    print("*****************************************************")
    get_us = int(input("Enter your US value: "))
    print()
    can_value = get_us * us_can_rate
    print("*****************************************************")
    print(get_us, "Dollar US are", round(can_value, 3), " Dollar Canadian")
    print("*****************************************************")

    
#us_to_can()


# #############################################################################################################
# #############################################################################################################

#  HT to peso function
# 4.7
def ht_to_peso():
    print("*****************************************************")
    print("You want to change Your Gourdes money into Peso")
    print()
    print("The peso rate are", peso_rate)
    print()
    print("*****************************************************")
    get_ht = int(input("Enter your gourdes amount: "))
    print()
    peso_value = get_ht / peso_rate
    print("*****************************************************")
    print(get_ht, "Gourdes are", round(peso_value, 3), "Pesos")
    print("*****************************************************")

# ht_to_peso()

# #############################################################################################################
# #############################################################################################################


#  Peso to HT function
# 4.8
def peso_to_ht():
    print("*****************************************************")
    print("You want to change Your Peso money into Gourdes")
    print()
    print("The peso rate are", peso_rate)
    print()
    print("*****************************************************")
    get_peso = int(input("Enter your peso amount: "))
    print()
    ht_value = get_peso * peso_rate
    print("*****************************************************")
    print(get_peso, "Pesos are", round(ht_value, 3), "Gourdes")
    print("*****************************************************")

# peso_to_ht()

# #############################################################################################################
# #############################################################################################################


#  HT to Euro function
# 5.9
def ht_to_euro():
    print("*****************************************************")
    print("You want to change Your Peso money into Gourdes")
    print()
    print("The peso rate are", euro_rate)
    print()
    print("*****************************************************")
    get_ht = int(input("Enter your gourdes amount: "))
    print()
    euro_value = get_ht / euro_rate
    print("*****************************************************")
    print(get_ht, "Gourdes are", round(euro_value, 3), "Euro")
    print("*****************************************************")

    
# #############################################################################################################
# #############################################################################################################


#  Euro to HT function
# 5.10
def euro_to_ht():
    print("*****************************************************")
    print("You want to change Your Peso money into Gourdes")
    print()
    print("The peso rate are", euro_rate)
    print()
    print("*****************************************************")
    get_euro = int(input("Enter your euro amount: "))
    print()
    ht_value = get_euro * euro_rate
    print("*****************************************************")
    print(get_euro, "Euro are", ht_value, "Gourdes")
    print("*****************************************************")
    

# #############################################################################################################
# #############################################################################################################




def welcome():
    print("1) Haitian to US")
    print("2) US to Haitian")
    print()

    print("3) Haitian to Canadian")
    print("4) Canadian to Haitian")
    print()

    print("5) Canadian to US")
    print("6) US to Canadian")
    print()

    print("7) Haitian to Peso")
    print("8) Peso to Haitian")
    print()

    print("9) Haitian to Euro")
    print("10) Euro to Haitian ")
    print()
    print("0) Quit the Program")

def function_mixed():
    xBank_graphik()
    welcome()
    print()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    



def login():
    print()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("you must be logged to continue!")
    file = open("Logged.csv", "w")
    username = input("Enter your username: \n ")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    usermail = input("Enter your username:\n ")
    info = username + ", " + usermail
    file.write(str(info))


def Quit_App():
    print("Thank you for visiting!!")
    



# conditions
def conditions():
    function_mixed()
    user_volunteer = int(input("What is your choice: "))

    if  user_volunteer == 1:
        ht_to_us(us_rate)

    elif user_volunteer == 2:
        us_to_ht(us_rate)

    elif user_volunteer ==3:
        ht_to_can()

    elif user_volunteer ==4:
        can_to_ht()

    elif user_volunteer ==5:
        login()
        can_to_us()

    elif user_volunteer ==6:
        login()
        us_to_can()

    elif user_volunteer ==7:
        login()
        ht_to_peso()

    elif user_volunteer ==8:
        login()
        peso_to_ht()

    elif user_volunteer ==9:
        login()
        ht_to_euro()

    elif user_volunteer ==10:
        login()
        euro_to_ht()

    elif user_volunteer== 0:
        Quit_App()

    else:
        print("Error")

def main():
    conditions()


main()