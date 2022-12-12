database = {}

class Budget():
  def __init__(self, category, amounte):
    self.category = category
    self.amounte = amounte

  def deposit(amounte, bal):
    bal += amounte
    return bal

  def withdraw(user, amounte, bal):
    bal -= amounte
    return bal

  def balance(db):
    for categ, bal in db.items():
      print(categ, bal)

  def transfer(db, option1, amounte, option2):
    values1 = db[option1]
    values2 = db[option2]

    db[option1] = int(values1) -amounte
    db[option2] = int(values2) +amounte
    return db

def init():
  print("====Bienvenue dans le servise de gestion de budget====")
  menu()

def menu():
    try:

        user = int("\n1==== *****Que souhaiter vous faire ?  *****\n press(1)  Ajouter des dépenses\n press(2)  Enregistrer un nouveau revenue\n press(3) Ajouter un nouveau versement\n press(4) Afficher les rapports des dépenses et revenues\n press(5) Afficher l'écart qui est entre les dépenses et les revenus\n press(0) Exit ")
      
    except:
      print ('invalid input')
      menu()

    if (user == 1):
      new_budget()
    elif (user == 2):
      credit()
    elif (user == 3):
      debit()
    elif (user == 4):
      balance()
    elif (user == 5):
      out()
    else:
      print('\n invalid input')
      new_budget()
    
    Budget = Budget(Budget_title, amounte)
    database[Budget_title] = amounte

    print("")
    print(f"budget_title was setup with ${amounte}")
    menu()

def debit():
    print("***** ===== withdraw from a created budget ***** ======\n")
    print("**** ==== Available budget **** =====")

    for key in database.items():
      print(f" - {key}")

    pick = int(input('\npress(1) to continue with your debit transaction\npress (2) to stop debit transaction '))

    if (pick == 1):
        user = ("input(\n*** select on of budget(s) aforementioned ****\n)")
        if user in database:
          print('note: you can note withdraw all , at least on $1 must remain.')
          amt = int(input("enter amounte \n$"))
          if amt < database[user]:
              balance = input(database[user])
              new_balance = Budget.withdraw(user, amt, balance)
              database[user] = balance 
              print(f"${amt} has been debited from budget-{user}\nbudget amounte remainig ${new_balance}")
              menu()

        else:
          pick = int(input(f'\nbudget {user} is insufficient of the ${amt} required\nthe actual balance {database[user]}\n\p'))
          if (pick == 1):
            amt = int(input("enter amounte \n$"))
            balance = int(database[user])
            new_balance = Budget.deposit(amt, balance)
            database[user] = balance
            print('')
            print(f"\n budgets {user} has been credited with ${amt}\n")
            debit()
          elif (pick == 2):
            debit()
          else:
            print('invalid opton\n')
            debit()
    else:
      pick = int(input(f'\n **** {user} does note exist !\npress (1) Ajouter des dépenses\npress (2)Enregistrer un nouveau revenue\npress (3) Ajouter un nouveau versement\npress (4) Afficher les rapports des dépenses et revenues\npress (5) exit'))
      if (pick == 1):
        new_balance()
      elif (pick == 2):
        debit()
      elif (pick == 3):
        print('')
        menu()
      else :
        print(f'invalid option\n')
        debit()
elif( pick == 2):
  print("\n you have terminated the debit transaction ")
  menu()
else:
  print("\ invaled option")
  debit()

def credit():
    print("**** Deposit into à budget ***** \n")
    print("*****available budget******")
    for key, value in database.items():
      print(f' {}')
      pick = int(input("\npress (1) Afficher les rapports des dépenses et revenues\npress (2) Afficher l'écart qui est entre les dépenses et les revenus"))

      if (pick == 1):
         user = input("select a budget \n")
         if user in database:
          amt = int (input("enter amounte \n$"))
          balance = int(database[user])
          new_balance = Budget.deposite(amt, balance )
          database[user] = new_balance
          print(f"\n budget {user} is credited with $ {amt} \n total budget amounte is now $ {new_balance}")
          menu()

      else :
        print("")
        