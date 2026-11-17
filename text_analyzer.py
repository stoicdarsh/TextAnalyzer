# A program that analyses a text file or a paragraph typed by the user.

def main():  
  content=content()
  print(content)
  while True:
    print("###......OPTIONS....###")
    print("""1.Count Characters in File
    2.Count Words
    3.Count Sentences
    4.Count Vowels and Consonant 
    5.Show Word-Frequency Dictionary with most Frequent Words
    6.Show longest word; Show it in Different Word-Cases
    7.Check Palindrome Words/Phrases
    8.Exit\n\n""")
    choice=int(input("Enter your Choice[1-8]:"))
    match choice:
      case 1:
          count_characters(content)
      case 2:
          count_words(content)
      case 3:
          count_sentence(content)
      case 4:
          count_vowels_consonant(content)
      case 5:
          word_freq_dict(content)
      case 6:
          longest_word(content)  
      case 7:
          print(is_palindrome())
      case 8:
          break
      case _:
          print("Entered invalid choice  :(  ")          
          print("Enter correct choice from below again ")
  with open("new.txt","r") as file:
     print("The New file Content is Here👇")
     print(file.read())

          
def content():
  while True:
    print(f"""{"•"*3}CHOICES{"•"*3}
      1.Write & Analyze Text
      2.Analyze Text File\n""")
    option=int(input("Enter your choice[1/2]: "))
    if option==1:
        content=input("""What's on your Mind !
        Write Here: """)
        break
    elif option==2:
        filename=input("Enter File name without Extension: ")+".txt"
        try:
          with open(filename, "r") as file:
            content=file.read()
            break
        except FileNotFoundError:
            print(f"{filename} not found :( ") 
    else:
       print("Enter Valid Choice Again")        
  print("_____________________________________YOUR CONTENT____________________________________________")
  return content

def count_characters(text):
   c1=len(text)
   c2=len(text.replace(" ",""))
   with open("new.txt","a+") as file:
      file.write(f"Total Characters(With Whitespace): {c1}\n")
      file.write(f"Total Characters (Without Whitespace): {c2}\n")
   print(f"Total characters( with whitespace): {c1}")
   print(f"Total characters (without whitespace): {c2}")

def count_words(text):
   l=text.split() 
   with open("new.txt","a") as file:
      file.write(f"Total words: {len(l)}\n")
   print(f"Total words :{len(l)}")

def count_sentence(text):
   l1=text.split(".")
   with open("new.txt","a") as file:
        file.write(f"Total sentences: {len(l1)}\n")
   print(f"Total sentence: {len(l1)}")

def count_vowels_consonant(text):
  c=0
  v=0
  for ch in text:
    if ch.isalpha():   
      if ch.lower() in "aeiou":
        v+=1
      else:
        c+=1
  with open("new.txt","a") as file:
    file.write(f"Vowels: {v}, Consonants: {c}\n")
  print("Vowels:",v,"Consonants:",c)      

def word_freq_dict(text):
  d={}
  for w in text.split(" "):
    c=text.count(w.lower())
    d[w.lower()]=c
  mfw=max(d,key=d.get)
  with open("new.txt","a") as file:
     file.write(f"Word Count Dictionary: {d}")
     file.write(f"Most frequent word: {mfw}\n")
  print(d)
  print(f"Most frequent word: {mfw}")

def longest_word(text):
  text.replace(".","")
  l=text.split()
  d={}
  for w in l:
    d[w]=len(w)
  lw=max(d,key=d.get)
  with open("new.txt","a") as file:
     file.write(f"Longest Word: {lw}\n")
     file.write(f"Upper case: {lw.uppper()}\n")
     file.write(f"Lower Case: {lw.lower()}\n")
     file.write(f"Title Case: {lw.title()}\n")
  print("Longest word:",lw)  
  print("Upper case:",lw.upper())    
  print("Lower case:",lw.lower())
  print("Title case:",lw.title())  

def is_palindrome():
   texts=input("Enter Word/phrase: ")
   return texts==texts[::-1]


if __name__=="__main__":
   main()
