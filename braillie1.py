#This is a python program to convert
#english





grade_1={"a":'⠁',"b":'⠃','c':'⠉','d':'⠙','e':'⠑','f':'⠋','g':'⠛','h':'⠓','i':'⠊','j':'⠚',
         'k':'⠅','l':'⠇','m':'⠍','n':'⠝','o':'⠕','p':'⠏','q':'⠟','r':'⠗','s':'⠎','t':'⠞',
         'u':'⠥','v':'⠧','x':'⠭','y':'⠽','z':'⠵',
         'w':'⠺','π':'⠨⠏',
         '#':{'1':'⠁','2':'⠃','3':'⠉','4':'⠙','5':'⠑','6':'⠋','7':'⠛','8':'⠓','9':'⠊'},
         "A":'⠁',"B":'⠃','C':'⠉','D':'⠙','E':'⠑','F':'⠋','G':'⠛','H':'⠓','I':'⠊','J':'⠚',
         'K':'⠅','L':'⠇','M':'⠍','N':'⠝','O':'⠕','P':'⠏','Q':'⠟','R':'⠗','S':'⠎','T':'⠞',
         'U':'⠥','V':'⠧','X':'⠭','Y':'⠽','Z':'⠵',
         'W':'⠺',
         'syntax':{',':'⠂',';':'⠆',':':'⠒','.':'⠲','!':'⠖',' ':' ','(':'⠐⠣',')':'⠐⠜','{':'⠸⠣','}':'⠸⠜',"'":"⠄",'<':'⠈⠣','>':'⠈⠜','[':'⠨⠣',']':'⠨⠜','@':'⠈⠁',
                   '$':'⠈⠎','*':'⠐⠔','$':'⠈⠎','=':'⠐⠶','%':'⠨⠴','+':'⠐⠖','-':'⠂⠤','÷':'⠐⠌','×':'⠐⠦','<':'⠈⠣','>':'⠈⠜'}
         #⠼ numbers
         #⠰ small
         #⠠ caps
         }

count=0
previous_character=[]
braillie_grade1_list=[]
input_text=input("Enter the text:")
input_text_list=list(input_text)

for character in input_text_list:
    count+=1
    if character=='0':
        try:
            if eval(previous_character[-1]):
                braillie_grade1_list.append("⠚")
        except (NameError,SyntaxError,IndexError):
            braillie_grade1_list.append("⠼"+"⠚")


    if character.isupper():
        if len(previous_character)==0:
            braillie_grade1_list.append("⠠"+grade_1[character])
        else:
            if previous_character[-1].islower():
                braillie_grade1_list.append("⠠"+grade_1[character])
            elif previous_character[-1].isupper():
                braillie_grade1_list.append("⠠"+grade_1[character])

            try:
                if eval(previous_character[-1]):
                    braillie_grade1_list.append("⠠"+grade_1[character])
            except NameError:
                pass
            except SyntaxError:
                braillie_grade1_list.append("⠠"+grade_1[character])


    if character.islower():
        if len(previous_character)==0:
            braillie_grade1_list.append(grade_1[character])
        else:
            if previous_character[-1].isupper():
                braillie_grade1_list.append(grade_1[character])
            elif previous_character[-1].islower():
                braillie_grade1_list.append(grade_1[character])
            try:
                if eval(previous_character[-1]):
                    braillie_grade1_list.append("⠰"+grade_1[character])
            except NameError:
                pass
            except SyntaxError:
                braillie_grade1_list.append(grade_1[character])


    try:
        if eval(character):
            if len(previous_character)==0:
                braillie_grade1_list.append("⠼"+grade_1['#'][character])
            else:
                try:
                    if eval(previous_character[-1]):
                        braillie_grade1_list.append(grade_1['#'][character])
                except NameError:
                    braillie_grade1_list.append("⠼"+grade_1['#'][character])
                except SyntaxError:
                    if previous_character[-1]=='.':
                        braillie_grade1_list.append(grade_1['#'][character])
                    else:
                        braillie_grade1_list.append("⠼"+grade_1['#'][character])
    except NameError:
        pass
    except SyntaxError:
        braillie_grade1_list.append(grade_1['syntax'][character])

    previous_character.append(input_text_list[count-1])

#print(previous_character)
print("\nBraillie output in grade 1:")
for braillie_character in braillie_grade1_list:
    print(braillie_character,end='')
