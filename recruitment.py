def main():
        



        
        skills=["py","db","qury","cc","js","ruby"]
        cv={}
        name=input("What is your name? ")
        cv["name"]=name
        age=int(input("How old are you? "))
        cv["age"]=age
        exp=int(input("How many years of experience do you have? "))
        cv["experience"]=exp
        cv["skills"]=[]
        
        for i in range(0,len(skills)):
                print("%d."%(i+1),skills[i])

        s1=int(input("Choose a skill from above by entering its number: "))
        cv["skills"].append(skills[s1-1])
        s2=int(input("Choose another skill from above by entering its number: "))
        cv["skills"].append(skills[s2-1])
        if(cv["age"] >= 25 and cv["age"]<=40 and cv["experience"]>5 and (skills[5] in cv["skills"])):
           print("You have been accepted, %s."%(cv["name"].title()))
        else:
           print("sorry, you are rejected")
                
                
        
        
if __name__ == '__main__':
	main()



