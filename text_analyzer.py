while True:
    print("""##**OPTIONS**##
      1.WRITE AND ANALYZE
      2.ANALYZE MY TEXT FILE""")
    print()
    option=int(input("Enter your choice: "))
    if option==1:
        content=input("""WHAT'S ON YOUR MIND!!
                        write it down...""")
        break
    elif option==2:
        filename=input("Enter your file name:")+".txt"
        try:
          with open(filename, "r") as file:
            content=file.read()
            break
        except FileNotFoundError:
            print(f"{filename} not found :( ") 
    else:
       print("Enter valid choice again")        
print("__YOUR CONTENT__")
print(content)                       