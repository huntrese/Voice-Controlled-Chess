import difflib
pieces = ["rook", "queen", "king", "bishop", "knight", "pawn", "castle"]


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


MyText = [{'transcript': 'sadawd rook to E4 Queen'}, {
    'transcript': ' sawwwastrrs night to E4 sadw'},]
li = [i.get("transcript") for i in MyText]
li = form(li)
print(li)
