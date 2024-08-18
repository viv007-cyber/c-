print("Do you want to code or decode")
print("1.Code")
print("2.Decode")
c=int(input("Enter your choice:"))


def decoder(code):
  if (len(code)<=3):
    code.reverse()
    yip=''.join(map(str,code))
    print(yip)
  else:
    code.pop(0)
    code.pop(0)
    code.pop(0)
    code.pop(-1)
    code.pop(-1)
    code.pop(-1)
    code.insert(0,code[-1])
    code.pop(-1)
    
    n=''.join(map(str,code))
    print(n)

def coder(word):
   if (len(word) >=3):
     word.append(word[0])
     word.remove(word[0])
     k=''.join(map(str,word))
     d=input("Enter 3 characters:")
     g=input("Enter 3 characters:")
     print(g+k+d)
   else:
     word.reverse()
     t=''.join(map(str,word))
     print(t)

if (c==1):
   m=(input("Enter your word:"))
   word=[i for i in m]
   print(f"code initiated{coder(word)}") 
elif(c==2):
  print("lets start decoding:")
  p= input("Enter your code:")
  code=[i for i in p]
  print(f"decode initiated{decoder(code)}")
else:
  exit()



#   aayyuussderaa => a2y2u2s2d1e1r1a2 
