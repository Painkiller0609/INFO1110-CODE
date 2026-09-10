#write your functions here
#I used ChatGPT-5,6 Luna.
#at the beginning,I have no idea,and let ai give me the direction.
#When i finish the assignment it gets something error and it gives me the solution
#I forget how to make the return values string,it gives me the solution,actually I am not familiar with the def()
def create_profile():
    name = input("Enter your full name: ")#ask users'name area and year.
    area = input("Enter your study area: ")
    study_year = int(input("Enter your year of study: "))
    component_name = name.replace(" ", "").isalpha()#delete the sapce between last name and first name.line 13
    component_area = area.isalpha()#detect whether the all characters are alphabet.line 16
    len_name = len(name)
    if len_name > 25 or len_name < 1 or component_name == False:
        print("Incorrect name: Please enter a name between 1 and 25 characters.")
        return False
    elif component_area == False:
        print("Incorrect study area: Please enter a study area using letters and spaces only.")
        return False
    elif study_year > 6 or study_year< 1:
        print("Incorrect year: Please enter a year between 1 and 6.")
        return False
    if len_name <= 25 or len_name > 1 and component_name == True and component_area == True and study_year <=6 or study_year>= 1:
        print("==================================================")
        print("|                Profile created!                |")
        print("==================================================")
        print("| Field         | Your Details                   |")
        print("==================================================")
        print(f"| Name          | {name:<30} |")
        print(f"| Study Area    | {area:<30} |")
        print(f"| Year of Study | {study_year:<30} |")
        print("==================================================")
        return [name,area,str(study_year)]

def request_style():
    social_score = 0#define the initial value of skill and social. line 50 52 54 56
    skill_score = 0
    interest = input("What is your main interest area? ")
    interest = interest.lower()#convert the input to lowercase so that it can be identified following.
    if interest not in ["academic","creative","culture","sport","volunteering","social"]:
        print("Please enter a valid interest area.")
        return False
    
    hobbies = input("What are your hobbies? ")
    social = input("Do you want to meet new people? ")
    skill = input("Do you want to build new skills? ")
    
    social = social.lower()
    skill = skill.lower()
    if social == "yes":
        social_score = social_score + 60
    if interest in ["culture","sport","social"]:
        social_score = social_score + 20
    if skill == "yes":
        skill_score = skill_score + 60
    if interest in ["academic","creative","volunteering"]:
        skill_score = skill_score + 20
    #print(f"Your club style is: {interest}")
    #print(f"Social score: {social_score}")
    #print(f"Skill score: {skill_score}")
    return [interest, hobbies, social_score,skill_score]




























        
