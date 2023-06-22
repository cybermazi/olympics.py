#!/usr/bin/env python
# coding: utf-8

# In[ ]:




##main class for all variables
class AthletesInfo:
    
    def __init__(self, firstname: str, lastname: str, nickname: str, dob: str, event: str, position: str, height: str, weight: str, email: str, num: str, address: str, gender: str, allergy: str, mental_illness: str, health_insur: str, parent_firstname: str, parent_lastname: str, relationship: str, parent_num: str, parent_email: str ):
        self.firstname = firstname.capitalize()
        self.lastname = lastname.capitalize()
        self.nickname = nickname
        self.dob = dob
        ##type is either Individual or team
        self.type = type
        self.event = event
        self.height = height
        self.weight = weight
        self.email = email
        self.num = num
        self.address = address.capitalize()
        self.gender = gender.upper()
        self.allergy = allergy
        self.mental_illness = mental_illness
        self.health_insur = health_insur

        
   ##str to define name     
    def __str__(self):
        return f"{self.firstname}{self.nickname}{self.lastname}"
    
  ##inheriting from main class   
class Sports(AthletesInfo):
    
    ##function for football to accept position played ,height , and weight of player   
    def football(self, height: str, weight: str):
        height = input("enter your hebight(inches): ")
        weight = input("enter your weight(kg): ")

    ##function for basketball to accept position played,height, and weight of player
    def basketball(self, height: str, weight: str):
        height = input("enter your height(inches): ")
        weight = input("enter your weight(kg): ")

    ##function to accept position in cricket, height and weight of player
    def cricket(self, height: str, weight: str):
        height = input("enter your height:(inches): ")
        weight = input("enter your weight(kg): ")

    def volleyball(self, height: str, weight: str):
        height = input("enter your height(inches): ")
        weight = input("enter your weight(kg): ")

    def tennis(self, height: str, weight: str):
        height = input("enter your height(inches): ")
        weight = input("enter your weight(kg): ")

    def boxing(self, height: str, weight: str):
        height = input("enter your height(inches): ")
        weight = input("enter your weight(kg): ")

    def cycling(self, height: str, weight: str):
        height = input("enter your height(inches): ")
        weight = input("enter your weight(kg): ")

    def gymnastics(self, height: str, weight: str):
        height = input("enter your height(inches): ")
        weight = input("enter your weight(kg): ")






class Coach:
    
    ##key is nickname
    athletes = {}
    
    def __init__(self):
        pass


    ##function to VENUE IS HERE
    ##venue is among Moshood Abiola National Stadium Abuja, Akpabio National Stadium Uyo,
    # Adamasingba Stadium ibadan,Teslim Balogun Stadium Lagos, Liberation Stadium porthacourt

     ##function to check in nickname is in dictionary  
    def confirm_reg(self, nickname: str):
        return nickname in Coach.athletes
    
    @classmethod

    ##function to append items into athlete dictionary expect info relating to sport ,height ,weight 
    def general_info(self, firstname: str, lastname: str, nickname: str, dob: str, email: str, num: str, address: str, gender: str, allergy: str, mental_illness: str, health_insur: str):
        if not self.confirm_reg:
            athlete = AthletesInfo(firstname, lastname, nickname, dob, email, num, address, gender, allergy, mental_illness, health_insur)
            Coach.athletes[nickname] = athlete
            return True
        else:
            return f"{nickname}, Complete your registration"
   
    @classmethod

    ##if general_info function returns True, run this function to collect the remaining info not collected initally
    def complete_reg(self,type: str, event: str, height: str, weight: str ):
        if self.general_info(firstname, lastname, nickname, dob, email, num, address, gender, allergy, mental_illness,health_insur) == True:
            athlete['event', 'type', 'height', 'weight'] = (athlete.event, athlete.type, athlete.height, athlete.weight)
            return f"{nickname}, your registration is complete"
        else:
            return 'Technical Error' 
        
        
    def get_athlete(self, nickname: str):
        if self.confirm_reg(nickname):
            return Coach.athletes[nickname]
        
        
class RegistrationPortal(Coach, Sports):
    
    @classmethod
    def menu(self):
        while True:
            choice = input("[1] New Registration\n[2] Check my Registration Status\n[#] Exit\nEnter option:" )
            return choice
            
    @classmethod
    def sports_menu(self):
        while True:
            status = False
            type = input("What are you registering as:\n[1] Individual\n[2] Team\nEnter option: ")
            if type == '1':
                self.type = 'Individual'
                while type == '1':
                    event = input('What event are you registering for\n[1] Tennis\n[2] Boxing\n[3] Cycling\n[4] Gymnastics\n: ')
                    if event == '1':
                        self.event = 'Tennis'
                        self.tennis(height,weight)
                        self.complete_reg(type,event, height, weight )

                    if event == '2':
                        self.event = 'Boxing'
                        self.tennis(height, weight)
                        self.complete_reg(type,event, height, weight)

                    if event == '3':
                        self.event = 'Cycling'
                        self.cycling(height,weight)
                        self.complete_reg(type, event, height, weight)

                    if event == '4':
                        self.event = 'Gymnastics'
                        self.gymnastics(height, weight)
                        self.complete_reg(type, event, height, weight)

                
            if type == '2':
                self.type = 'Team'
                while type == '2':
                    event = input('What event are you registering for\n[1] Football\n[2] Basketball\n[3] Cricket\n[4] Volleyball\nEnter option:')
                    if event == '1':
                        self.event = 'Football'
                        self.football(height, weight)
                        self.complete_reg(type, event, height, weight)

                    if event == '2':
                        self.event = 'Basketball'
                        Sports.basketball(height, weight)
                        Sports.complete_reg(type, event, height, weight)

                    if event == '3':
                        self.event = 'Cricket'
                        self.cricket(height, weight)
                        self.complete_reg(type, event, height, weight)

                    if event == '4':
                        self.event = 'Volleyball'
                        self.volleyball(height, weight)
                        self.complete_reg(type, event, height, weight)





        
    
    @classmethod         
    def reg_menu(self):
        status = False
        while status == False:
            print("GENERAL INFO")
            firstname = input("Enter your firstname:")
            lastname = input("Enter your lastname:")
            nickname = input("Enter your nickname:")
            dob = input("Enter your Date of Birth: \nIn this format(DD/MM/YY)")
            email = input("Enter your email address: ")
            num = input("Do enter your phone number: ")
            address = input("enter your residential address: ")
            gender = input("[1] Male\n[2] Female\nSelect option: ")
            if gender == '1':
                self.gender = 'male'
            elif gender == '2':
                self.gender = 'female'
            else:
                self.gender = input("kindly state your gender: ")
            allergy = input("Do you have any allergies??\n[1] Yes\n[2] No\n[3] Not sure:  ")
            if allergy == '1':
                self.allergy = 'Yes'
            elif allergy == '2':
                self.allergy = 'No'
            elif allergy == '3':
                self.allergy = 'Not sure'
            mental_illness = input("Do you have a history of mental illness in the past?\n[1] Yes\n[2] No\n[3] Not sure:  ")
            if mental_illness == '1' :
                self.mental_illness = 'Yes'
            elif mental_illness == '2':
                self.mental_illness = 'No'
            elif mental_illness == '3':
                self.mental_illness = 'Not sure'
            health_insur = input("Do you actively have health insurance coverage?\n[1] Yes\n[2] No\n[3] Not sure: ")
            if health_insur == '1':
                self.health_insur = 'Yes'
            elif health_insur == '2':
                self.health_insur = 'No'
            elif health_insur == '3':
                self.health_insur = 'Not sure'
            #if self.general_info(firstname, lastname, nickname, dob, email, num, address, gender, allergy, mental_illness, health_insur) == True:
            self.sports_menu()
            status = True
                
    @classmethod            
    def portal(cls):
        portal = RegistrationPortal()
        while True:
            choice = RegistrationPortal.menu()
            if choice == '1':
                RegistrationPortal.reg_menu()
            if choice == '2':
                pass
            else:
                break
                
                
if __name__ == "__main__":
    RegistrationPortal.portal()
    
            
            
        
        
        
            
        
    
    
    
    
    

