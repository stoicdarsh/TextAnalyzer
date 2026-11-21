# A program that analyses a text file or a paragraph typed by the user.

def main():  
  content= data()
  print(content)

  c1,c2=count_characters(content)
  cw=count_words(content)
  cs=count_sentence(content)
  v,c=count_vowels_consonant(content)
  d,mfw=word_freq_dict(content)
  lw,ulw,llw,tlw=longest_word(content) 

  while True:
    print()
    print("###......OPTIONS....###")
    print("""1.Count Characters in File
2.Count Words
3.Count Sentences
4.Count Vowels and Consonant 
5.Show Word-Frequency Dictionary with most Frequent Words
6.Show longest word; Show it in Different Word-Cases
7.Check Palindrome Words/Phrases
8.Exit\n\n""")
    
    while True:
      try:
         choice=int(input("Enter your Choice[1-8]:"))
         break
      except ValueError:
         print("Enter a Valid Choice")

    match choice:
      case 1:
          print(f"Total characters( with whitespace): {c1}")
          print(f"Total characters (without whitespace): {c2}")
      case 2:
          print("Total Words:",cw)
      case 3:
          print("Total Sentences:",cs)
      case 4:
          print("Vowels:",v,"Consonants:",c)
      case 5:
          print("Dictionary:",d)
          print("Most Frequent Word:",mfw)
      case 6: 
          print("Longest word:",lw)  
          print("Upper case:",ulw)    
          print("Lower case:",llw)
          print("Title case:",tlw)
      case 7:
          print(is_palindrome())
      case 8:
          with open("new.txt","w+",encoding="utf-8") as file:
               file.write(f"Total Characters(With Whitespace): {c1}\n")
               file.write(f"Total Characters (Without Whitespace): {c2}\n")
               file.write(f"Total words: {cw}\n")
               file.write(f"Total sentences: {cs}\n")
               file.write(f"Vowels: {v}, Consonants: {c}\n")
               file.write(f"Word frequency Dictionary: {d}\n")
               file.write(f"Most frequent word: {mfw}\n")
               file.write(f"Longest Word: {lw}\n")
               file.write(f"Upper case: {ulw}\n")
               file.write(f"Lower Case: {llw}\n")
               file.write(f"Title Case: {tlw}\n")  
               file.seek(0)
               print(f"{'•'*3} Complete File Report is Here👇{'•'*3}\n")
               print(file.read())
          break
      case _:
          print("Entered invalid choice  :(  ")          
          print("Enter correct choice from below again ")


def data():
  while True:
    print(f"{'•'*3}CHOICES{'•'*3}\n1.Write & Analyze Text\n2.Analyze Text File\n""")
    
    while True:
       try:
          option=int(input("Enter your choice[1/2]: "))
          break
       except ValueError:
          print("Enter Valid Choice in described Type")

    if option==1:
        print("What's on your Mind! Write below (press Enter on an empty line to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        content = "\n".join(lines)
        if content.strip():
            break
        print("Text cannot be empty. Please enter some text.\n")

    elif option==2:
        raw_name = input("Enter File name: ").strip()
        filename = raw_name if raw_name.endswith(".txt") else raw_name + ".txt"
        try:
            with open(filename, "r", encoding="utf-8") as file:
              content = file.read()
            if content.strip():
              break
            print(f"{filename} is empty :( Choose a file with text.\n")
        except (FileNotFoundError, OSError):
            print(f"{filename} not found or invalid :( \n")
    else:
        print("Enter Valid Choice Again")     
  print("_____________________________________YOUR CONTENT____________________________________________")
  return content

def count_characters(text):
   c1=len(text)
   c2=len(text.replace(" ",""))
   return c1,c2

def count_words(text):
   l=text.split() 
   return len(l)

def count_sentence(text):
  normalized = text.replace("!", ".").replace("?", ".")
  sentences = [s for s in normalized.split(".") if s.strip()]
  return len(sentences)

def count_vowels_consonant(text):
  c=0
  v=0
  for ch in text:
    if ch.isalpha():   
      if ch.lower() in "aeiou":
        v+=1
      else:
        c+=1
  return v,c      

def word_freq_dict(text):
  d={}
  for w in text.split(" "):
    c=text.count(w.lower())
    d[w.lower()]=c
  mfw=max(d,key=d.get)
  return d,mfw

def longest_word(text):
  text.replace(".","")
  l=text.split()
  d={}
  for w in l:
    d[w]=len(w)
  lw=max(d,key=d.get)
  return lw,lw.upper(),lw.lower(),lw.title()

def is_palindrome():
   texts=input("Enter Word/phrase: ")
   return texts==texts[::-1]


if __name__=="__main__":
   main()