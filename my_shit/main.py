import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def lev(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(lev(a[1:], b[1:])+(a[0] != b[0]), lev(a[1:], b)+1, lev(a, b[1:])+1)

try:
 #s = "w"
 # use the microphone as source for input.
 with sr.Microphone() as source2:
  # wait for a second to let the recognizer
  # adjust the energy threshold based on
  # the surrounding noise level
  #r.adjust_for_ambient_noise(source2, duration=0.2)
  
  #listens for the user's input
  #Yaudio2 = r.listen(source2)
  
  # Using google to recognize audio
  MyText = [{'transcript': ' ASLDKAWUBDUAWBYDGWV WVVVVV   Knight to E4 dahudwagdua'},{'transcript': '  WVVVVV   Knight to E4'},{'transcript': '  gicu boevicu   rook to E4'}]
  #MyText = MyText.lower()print(MyText)
  #print(MyText)
        #s = "1"
        
  #SpeakText(MyText)
  
except sr.RequestError as e:
 print("Could not request results; {0}".format(e))
 
except sr.UnknownValueError:
 print("unknown error occurred")



li = [i.get("transcript").replace("before","B4").replace("see","C").replace("9","knight") for i in MyText]
vlad_op_list=[]
pieces = ["rook", "queen", "king", "bishop", "knight", "pawn"]
print(li)
for i in li:
  for j in pieces:
    try:
      x=i.lower().index(j)
      vlad_op_list.append(i[x:])
    except:
      pass
print(vlad_op_list)
my_cool_list = []

for i in li:
 #i2 = i.replace("before","B4").replace("8","A").replace("see","C").replace("9","knight")
 for j in range(len(i)):
  try:
   if i[j] == i[j].upper() and i[j+1].isnumeric() and i[j].isalpha():
    my_cool_list.append(i)
  except:
   pass



my_second_cool_list = []
for i in my_cool_list:
    for j in pieces:
     my_second_cool_list.append((lev(i.split(" ")[0].lower(),j), i, j))

#print(sorted(my_second_cool_list)[0][2])

match sorted(my_second_cool_list)[0][2]:
 case "knight":
  print("n" + my_second_cool_list[0][1][-2:])
 case "queen":
  print("q" + my_second_cool_list[0][1][-2:])
 case "rook":
  print("r" + my_second_cool_list[0][1][-2:])
 case "king":
  print("k" + my_second_cool_list[0][1][-2:])
 case "bishop":
  print("b" + my_second_cool_list[0][1][-2:])
 case "pawn":
  print("p" + my_second_cool_list[0][1][-2:])
 
#print(sorted(my_second_cool_list)[0])