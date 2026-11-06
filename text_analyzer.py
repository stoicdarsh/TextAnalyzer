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
print("_____________________________________YOUR CONTENT____________________________________________")
print(content)

def count_characters(text):
   c1=len(text)
   c2=len(text.replace(" ",""))
   print(f"Total characters( with whitespace): {c1}")
   print(f"Total characters (without whitespace): {c2}")
def count_words(text):
   l=text.split() 
   print(f"Total words :{len(l)}")
def count_sentence(text):
   l1=text.split(".")
   print(f"Total sentence: {len(l1)}")
def count_vowels_consonant(text):
   v=0
   c=0
   for ch in text.replace(" ","").replace(".",""):
      if ch in "aeiouAEIOU":
         v+=1
      else:
         c+=1
   print("Vowels:",v,"       ","Consonants:",c)      
def word_freq_dict(text):
  d={}
  for w in text.split(" "):
    c=text.count(w.lower())
    d[w.lower()]=c
  mfw=max(d,key=d.get)
  print(d)
  print(f"Most frequent word :{mfw}")




print("###......OPTIONS....####")
print("""          1.count characters in my text.
          2.count words
          3.count sentence
          4.count vowels and consonant 
          5.count frequncy of each word and display word with max. frequency
          6.Exit""")
while True:
  print()
  print()
  print("Enter your choice....")
  o=int(input())
  print()
  if o==1:
    count_characters(content)
  elif o==2:
    count_words(content)
  elif o==3:
    count_sentence(content)
  elif o==4:
    count_vowels_consonant(content)
  elif o==5:
    word_freq_dict(content)
  elif o==6:
     break  
  else:
     print("Entered invalid choice  :(  ")          
     print("Enter correct choice from below again ")







            