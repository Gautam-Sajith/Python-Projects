from IPython.display import clear_output
def it():
    name1=input("PLAYER 1 ENTER YOUR NAME ")
    name2=input("PLAYER 2 ENTER YOUR NAME ")
    word=input(name1+ " ENTER WORD ")
    clear_output()
    return(name1,name2,word)
    

    from IPython.display import clear_output
def q():
    (name1,name2,word)=it()
    cntr=0
    rep=''
    for j in range(0,len(word)):
        rep=rep+(str(j))
        
    
    while(cntr<=5):
        letter=input(name2+ " ENTER LETTER ")
        k=0
        for x in range(0,len(word)):
            if word[x]==letter:
                
                rep=rep.replace(rep[x],letter)
                k=1
                print(rep)
             
             
        if(k==0):
            cntr+=1
        if cntr==1:
            print(".")
        if cntr==2:
            print(".")
            print(" |")
            print(" |")
            
        if cntr==3:
            print(".")
            print(" |")
            print(" |")
            print(" .O.")
        if cntr==4:
            print(".")
            print(" |")
            print(" |")
            print(" .O.")
            print(" /|\ ")
        if cntr==5:
            print(".") 
            print(" |")
            print(" |")
            print(" .O.")
            print(" /|\ " )
            print(" / \ ")      
            print(name2+" YOU DIED")      
       
            print(word)
            break
          


        if(word==rep):
                print(name2+" YOU WIN")
                break
          