from tkinter import *
import random
#declares window
root = Tk()
#sets window geomotry
root.geometry("720x250")
#sets window titles
root.title("Password generator")

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
spec1 = chr (random.randint(33,152))
spec2 = chr(random.randint(33,152))
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + spec1 + spec2
password = shuffle(password)
my_list = [password]
print(my_list)
#creates text box widget
txt_output = Text(root, height=5, width=30)
txt_output.pack(pady=30)
for item in my_list:
    txt_output.insert('end', my_list)

#is loop
root.mainloop()