def hello_fun():
    print('Hello me!')

class Tuna:
    
    b = 2 # it is constant/static/instance variable
    
    life = 10
    
    #If you want to define vars for class, you need to have init():
    def __init__(self, name_id, age): #when calling a class in script, __init__ part will be run
        
        print('init part is ran clling a class')
        
        self.age = age #if you comment this, age is not callabe in script
        
        self.name = name_id #if you comment this, name is not callabe in script
        
        self.name_age = self.name + age #or instead of self.name, use name_id
        
    
    def fish(self): #this function has no input. DONT FORGET TO USE SELF DEFINING FUNCTION.
        print("I am a big tuna fish")
        
    def swim(self): #this function has no input
        print('I am swiming')
        
    def attack(self, bb): #this function has bb as input
        
        self.life-=1 #accesing constant var
        
        self.bb = bb #you can jump this line since bb is input of function so no need to self
                     #BUT if you comment above line, bb is not callabe in script as attribute of attack()
        
        self.aa = 2 * bb #if you define var for a function, you need self
        
        print('Ouch! life is: '+str(self.life)) 
        
        print('age:' + str(self.age)) #accessing dynamic var  
        
        return bb + self.aa #aa is not input and it is defined inside the function, so you need self.aa to call it