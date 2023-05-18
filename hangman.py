#------------------------------ HANGMAN GAME---------------------------------------------------------




import random

import turtle
t=turtle.Turtle()
s=turtle.Screen()

t.pensize(5)
t.color("black")
s.title("Hangman_Game")
s.bgcolor("light yellow")

t.up()
t.bk(200)
t.setheading(270)
t.fd(150)
t.down()
t.setheading(90)
t.fd(400)
t.setheading(0)
t.fd(150)

 


m=0


class A:
     

    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
         



    def one(self):
        print("this is ",self.n1)
        print("this is ",self.n2)

        k=random.randint(1,2)
        a=int(input("\n\n user1 :chooose any number between  1 and 2 \n"))
        print("\nthe random value initilize is for starting the game: ",k)
        print("\n\n")
        if a==k:
            print("user1  will give the word and user2 has to gess the word letter by letter")
        else:
            print("user2  will give the word and user1 has to gess the word letter by letter")




    @staticmethod
    def two():
        w=input("\nenter the word\n")
        l=list(w)
        li=[]
         
        for i in range(0,len(l)):
            li.insert(i," ")

         
        def dess():
            for i in range(0,len(l)):
                print("_",end=" ")

        def guess(w,li):
            
                
                for i in range(0,len(w)):
                    if x==w[i] :
                        print("correct gess\n")
                         
                        li[i]=x
                        print("this is your position\n")
                        for k in range(0,len(li)):
                                       print(li[k],end=" ")
                        print()
                        dess()

                        break
                            
                        
        
                    if i==len(w)-1:
                        if x!=w[i]:
                            print("incoerrect gess\n")
                            global m
                            m=m+1
                            if m==1:
                                t.setheading(270)
                                t.fd(100)

                            elif m==2:
                                t.setheading(0)
                                t.circle(-40)
                                t.up()
                                t.setheading(270)
                                t.fd(80)
                                t.down()

                            elif m==3 or m==5:
                                t.setheading(270)
                                t.fd(100)

                            elif m==4 or m==6:
                                t.setheading(90)
                                t.left(45)
                                t.fd(50)
                                t.bk(50)
                                t.setheading(90)
                                t.right(45)
                                t.fd(50)
                                t.bk(50)

                                return m

                            
        
                     
        for s in range(0,50):
             
            c=0
            for i in range(0,len(li)):
                if li[i]==" ":
                    c=c+1
                    
            if c>0:
                x=input("\n\ngess the letter\n")
                m=guess(w,li)

                if m==6:
                    print("-------------------the hangame has created----------------")
                    print("-------------------you lose the game---------------\n")
                    
                    print("\n************************Finished Game**************************")
                    break

            elif c==0:
                print("\n")
                print("-----------------------you have guessed all the letters--------------\n")
                print("-----------------------you win the game------------------------")
                print("\n************************Finished Game**************************")
                break
         
            
           
        
                     
    


print("------------------------------START GAME----------------------------")
print("\n*********************************************************************\n\n")



obj1=A("user1","user2")

obj1.one()

obj1.two()

t.hideturtle()





