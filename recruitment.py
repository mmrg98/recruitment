def main():
        print("")



        
        skills=["p","d","q","w","E","r"]
        name=input("What is your name? ")
        age=eval(input("How old are you? "))
        exp=eval(input("How many years of experience do you have? "))
        cv={"name":"m"}
        cv["name"]=name
        cv["age"]=age
        cv["experience"]=exp
        cv["skills"]=[]
        
        for i in range(0,len(skills)):
                print(i+1,". ",skills[i])

        s1=eval(input("Choose a skill from above by entering its number: "))
        s2=eval(input("Choose another skill from above by entering its number: "))
        cv["skills"].append(skills[s1-1])
        cv["skills"].append(skills[s2-1])
        if(cv["age"] >= 25 and cv["age"]<=40 and cv["experience"]>5 and (skills[5] in cv["skills"])):
           print("accepted")
        else:
           print("rejected")
                
                
        
        
if __name__ == '__main__':
	main()



