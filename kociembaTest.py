import kociemba

colordict={'W':'U','Y':'D','R':'L','O':'R','B':'F','G':'B'}


allcolor=['YWOOBBOGW', 'GRRWRRRGB', 'BRORRBBWB', 'RORYGYRRY', 'GRRORRRBR', 'RRROORRRR']

temp=''

for facec in allcolor:
    for num in facec:
        temp=temp+colordict[num]


for a in temp:
    print(a)
    



sendstr=kociemba.solve('RLDBFFFDDLDRULUUFLLBFFULLDRDRBBBLUUUBUUDRRFRBFBDFDLBRR')

#'YWOOBBOGWGOYWYYYGBBRORRBBWBRORYGYRRYGYWOWBWBWGGRROGOWG'

#用字符 H   I   J   X   Y   Z
#  代替 U2  R2  F2  D2  L2  B2
actlist=["U2","U'","R2","R'","F2","F'","D2","D'","L2","L'","B2","B'"]
actdict={"U2":'H',"U'":'u',"R2":'I',"R'":'r',"F2":'J',"F'":'f',"D2":'X',"D'":'d',"L2":'Y',"L'":'l',"B2":'Z',"B'":'b'}

for act in actlist:
    temp=sendstr.replace(act,actdict[act])
    sendstr=temp

sendstr=sendstr.replace(" ","")

print(sendstr)



'''
其中魔方状态的字符串 按照
 `U1`, `U2`, `U3`, `U4`, `U5`, `U6`, `U7`, `U8`, `U9`,   
  `R1`, `R2`, `R3`, `R4`, `R5`, `R6`, `R7`, `R8`, `R9`,  
  `F1`, `F2`, `F3`, `F4`, `F5`, `F6`, `F7`, `F8`, `F9`, 
  `D1`, `D2`, `D3`, `D4`, `D5`, `D6`, `D7`, `D8`, `D9`, 
  `L1`, `L2`, `L3`, `L4`, `L5`, `L6`, `L7`, `L8`, `L9`, 
   `B1`, `B2`, `B3`, `B4`, `B5`, `B6`, `B7`, `B8`, `B9`       的顺序排列

             |************|

             |*U1**U2**U3*|

             |************|

             |*U4**U5**U6*|

             |************|

             |*U7**U8**U9*|

             |************|

 ************|************|************|************

 *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*

 ************|************|************|************

 *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*

 ************|************|************|************

 *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*

 ************|************|************|************

             |************|

             |*D1**D2**D3*|

             |************|

             |*D4**D5**D6*|

             |************|

             |*D7**D8**D9*|

             |************|
'''