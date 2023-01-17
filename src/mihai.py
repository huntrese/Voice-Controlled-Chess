import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
pieces = ["rook", "queen", "king", "bishop", "knight", "pawn","castle"]
def lev(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(lev(a[1:], b[1:])+(a[0] != b[0]), lev(a[1:], b)+1, lev(a, b[1:])+1)

def form(li):
    vlad_op_list=[]
    phrase=""
    print(li)
    for i in li:
      for j in pieces:
        try:
          x=i.lower().index(j)
          if j=="castle":
            print("$")
            if i[x-6:x-1]=="short":
              vlad_op_list.append("O-O")
            elif i[x-5:x-1]=="long":
              vlad_op_list.append("O-O-O")
          for k in range(len(i)):
            if i[k].isalpha() and i[k+1].isnumeric():
              phrase=i[x:k+2]
              for l in pieces:
                if l in i[k+2:].lower():
                  phrase+=" "+l
              if phrase not in vlad_op_list:
                vlad_op_list.append(phrase) 
              
        except:
         pass
    for i in vlad_op_list:
      if i.replace(" ","") in pieces:
        vlad_op_list.remove(i)
    return vlad_op_list
def voice():
  try:
    try:
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
      #MyText = MyText.lower()print(MyText)
      #print(MyText)
            #s = "1"
            
      #SpeakText(MyText)
      
    except sr.RequestError as e:
      print("Could not request results; {0}".format(e))
    
    except sr.UnknownValueError:
      print("unknown error occurred")


    #MyText=[{'transcript': 'sadawd night to E4', 'confidence': 0.86834723}, {'transcript': ' sawwwastrrs nice to E4'}, {'transcript': 'Knight to E4'}, {'transcript': 
    #'night to e-4'}, {'transcript': 'night to eat for'}, {'transcript': ' how r u? rook to B8'}, {'transcript': 'hahaha CHECKMATE queen to C4'}]
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
    li = [i.get("transcript") for i in MyText] 
    b = []
    for i in li:
        for x in dic:
            i = i.replace(x,dic[x])
        b.append(i)

    li = b

    li=form(li)


    print(li)
    my_cool_list = []; placements = ["a","b","c","d","e","f","g","h","A","B","C","D","E","F","G","H",]
    for i in li:
    #i2 = i.replace("before","B4").replace("8","A").replace("see","C").replace("9","knight")
      for j in range(len(i)):
        try:
          if i[j] in placements and i[j+1].isnumeric() and i[j].isalpha():
            my_cool_list.append(i)
        except:
          pass


    my_second_cool_list = []
    for i in my_cool_list:
        for j in pieces:
          my_second_cool_list.append((lev(i.split(" ")[0].lower(),j), i, j))

    #print(sorted(my_second_cool_list)[0][2])

    right = sorted(my_second_cool_list)[0]
    v = ""
    match (right[2]):
      case "knight":
        v = ("n" + right[1][-2:]) if "to" in right[1] else ("nx" + right[1][-2:])
      case "queen":
        v = ("q" + right[1][-2:]) if "to" in right[1] else ("qx" + right[1][-2:])
      case "rook":
        v = ("r" + right[1][-2:]) if "to" in right[1] else ("rx" + right[1][-2:])
      case "king":
        v = ("k" + right[1][-2:]) if "to" in right[1] else ("kx" + right[1][-2:])
      case "bishop":
        v = ("b" + right[1][-2:]) if "to" in right[1] else ("bx" + right[1][-2:])
      case "pawn":
        v = ("p" + right[1][-2:]) if "to" in right[1] else ("px" + right[1][-2:])
    
    return(v)
    #print(sorted(my_second_cool_list)[0])
  except:
    return("")
  