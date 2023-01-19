import speech_recognition as sr
import pyttsx3
import difflib
r = sr.Recognizer()
pieces = ["rook", "queen", "king", "bishop", "knight", "pawn","castle"]
def lev(a):
    li = []
    for i in pieces:
        seq = difflib.SequenceMatcher(None, i, a)
        li.append(tuple((seq.ratio()*100, a, i)))
    return (sorted(li, reverse=True)[0])
def limit(i):
    li=["",""]
    for k in range(len(i)-1):
        if i[k].isalpha() and i[k+1].isnumeric():
            phrase = i[:k+2]
            print(phrase)
            try:
                m = i[k+2:].split()[0]
                
                print(m)
                if m.lower() in pieces:
                    return ((i[:k+2],m))
                else:
                    return ((i[:k+2],""))
            except:
                return ((i[:k+2],""))
    return li

def checkCastle(i,x,j):
  if j=="castle":
            print("$")
            if i[x-6:x-1]=="short":
              return("O-O")
            elif i[x-5:x-1]=="long":
              return("O-O-O")
  else:
    return("")

def ns():
  dic={
    "be":"B",
    "see":"C",
    "age":"H",
    "night":"Knight",
    "tonight":"Knight",
    "own":"pawn",
    "book":"rook",
    "look":"rook",
    "nice":"Knight",
    "porn":"pawn",
    "phone":"pawn",
    "born":"pawn",
    " one":"1",
    " two":"2",
    " three":"3",
    " four":"4",
    " five":"5",
    " six":"6",
    " seven":"7",
    " eight":"8",
    " nine":"9",
    " for":"4",
    " free":"3"
  }
  b = []
  for i in li:
    for x in dic:
      i = i.replace(x,dic[x])
      b.append(i)
  li = b
  return li

def form(li):
    vlad_op_list = []
    final = []
    phrase = ""
    # print(li)
    for i in li:
        for j in i.split():
            x = lev(j)
            # castle=checkCastle(x[1],j)
            # if castle!="":
            #   return(castle)

            if x[0] >= 80:
                # print(x)
                l = i.index(j)
                i=i[:l]+x[2]+i[l+len(j):]
                tup=limit(i[l:])
                print(tup)
                vlad_op_list.append((tup[0],tup[1]))

    if ('','') in vlad_op_list:
        vlad_op_list.remove(('',''))
    return(vlad_op_list)
def voice():
    #s = "w"
    # use the microphone as source for input.
      with sr.Microphone() as source2:
      # wait for a second to let the recognizer
      # adjust the energy threshold based on
      # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=0.1)
      
      #listens for the user's input
        audio2 = r.listen(source2)
      
      # Using google to recognize audio
        MyText = r.recognize_google(audio2); #print(MyText)
        # MyText=[{'transcript': 'sadawd rook to E4 Queen'}, {'transcript': ' night to E4'},] 
      #MyText = MyText.lower()print(MyText)
      #print(MyText)
            #s = "1"
            
      #SpeakText(MyText)


    #MyText=[{'transcript': 'sadawd night to E4', 'confidence': 0.86834723}, {'transcript': ' sawwwastrrs nice to E4'}, {'transcript': 'Knight to E4'}, {'transcript': 
    #'night to e-4'}, {'transcript': 'night to eat for'}, {'transcript': ' how r u? rook to B8'}, {'transcript': 'hahaha CHECKMATE queen to C4'}]

      li = [i.get("transcript") for i in MyText] 
      li=ns(li)
      li=form(li)

      print(li)
  
      #print(sorted(my_second_cool_list, reverse=True)[:8])


      #print(sorted(my_second_cool_list)[0][2])

      right = li[0]
      print(right)
      v = ""
      match (right[0].split()[0]):
        case "knight":
          v = ("n" + right[0][-2:]) if "to" in right[0] else ("nx" + right[0][-2:])
        case "queen":
          v = ("q" + right[0][-2:]) if "to" in right[0] else ("qx" + right[0][-2:])
        case "rook":
          v = ("r" + right[0][-2:]) if "to" in right[0] else ("rx" + right[0][-2:])
        case "king":
          v = ("k" + right[0][-2:]) if "to" in right[0] else ("kx" + right[0][-2:])
        case "bishop":
          v = ("b" + right[0][-2:]) if "to" in right[0] else ("bx" + right[0][-2:])
        case "pawn":
          v = ("p" + right[0][-2:]) if "to" in right[0] else ("px" + right[0][-2:])
      if right[1].lower() in pieces:
        v+=right[1][:1]
      return(v)
    