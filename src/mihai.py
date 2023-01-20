import speech_recognition as sr
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
            try:
                m = i[k+2:].split()[0]
                if m.lower() in pieces:
                    return ((i[:k+2],m))
                else:
                    return ((i[:k+2],""))
            except:
                return ((i[:k+2],""))
    return li


def form(li):
    vlad_op_list = []
    for i in li:
        for j in i.split():
            x = lev(j)
            if x[0] >= 80:
                l = i.index(j)
                i=i[:l]+x[2]+i[l+len(j):]
                tup=limit(i[l:])
                vlad_op_list.append((tup[0],tup[1]))

    if ('','') in vlad_op_list:
        vlad_op_list.remove(('',''))
    return(vlad_op_list)
def voice():
      with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.1)

        audio2 = r.listen(source2)

        MyText = r.recognize_google(audio2)

      li = [i.get("transcript") for i in MyText] 

      print(li, "li")
      return li
def get():   
  try:
    cas = 0
    li = voice()
    for i in li:
            print(i)
            if "castle" in i.lower():
                    cas += 1
    print(form(li))
    v = ""
    if cas == 0:
            right = form(li)[0]
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
    else:
            for i in li:
                    if "long" in i:
                            v = "O-O-O"
                            break
                    elif "short" in i:
                            v = "O-O"
                            break
  except:
    return("")
  return(v)

