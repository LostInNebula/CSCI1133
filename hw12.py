import random
class Character:
    '''
    Purpose: An object in this class represents an Item, a product of a store.
    Instance variables: self.store = the store in which the item is from
                        self.name = the name of the item
                        self.price = the price of the item
                        self.category = where on the body the item is worn
    Methods: __init__ = a constructor to initialize instance variables
             __str__ = a method that returns a string that contains the name, category, and price of an item
             __lt__ = a method that determines if one item is or is not less expensive than another item
    '''
    def __init__(self, name, color, num_tasks):
        tasks = []
        possible_tasks = ['Stabilize drill', 'Calibrate distributor',
'Map course', 'Clear out O2 filter', 'Download files',
'Redirect power', 'Empty garbage', 'Repair wiring',
'Fill engines tanks', 'Inspect laboratory', 'Record temperature',
'Sign in with ID', 'Enable manifolds', 'Upload files']

        self.name = name
        self.color = color
        self.alive = True
        self.role = "Good"
        for i in range(num_tasks):
            task = random.choice(possible_tasks)
            possible_tasks.remove(task)
            tasks.append(task)
        self.task_list = tasks
    
    def __repr__(self):
        if self.alive == True:
            return(self.name + ": " + self.color + " - Health Status: Alive")
        else:
            return(self.name + ": " + self.color + " - Health Status: Ghost")
    
    def get_identity(self):
        return "Character"
    
class Crewperson(Character):
    '''
    Purpose: An object in this class represents an Item, a product of a store.
    Instance variables: self.store = the store in which the item is from
                        self.name = the name of the item
                        self.price = the price of the item
                        self.category = where on the body the item is worn
    Methods: __init__ = a constructor to initialize instance variables
             __str__ = a method that returns a string that contains the name, category, and price of an item
             __lt__ = a method that determines if one item is or is not less expensive than another item
    '''
    def get_identity(self):
        return "Crewperson"
        
    def complete_task(self):
        if len(self.task_list) > 1:
            print(self.name + " has completed task: " + self.task_list[0])
            self.task_list.remove(self.task_list[0])
        elif len(self.task_list) == 1:
            print(self.name + " has completed task: " + self.task_list[0])
            self.task_list.remove(self.task_list[0])
        elif len(self.task_list) == 0:
            print(self.name + " has completed all their tasks")
        
        return self.task_list
        
        
class Pretender(Character):
    '''
    Purpose: An object in this class represents an Item, a product of a store.
    Instance variables: self.store = the store in which the item is from
                        self.name = the name of the item
                        self.price = the price of the item
                        self.category = where on the body the item is worn
    Methods: __init__ = a constructor to initialize instance variables
             __str__ = a method that returns a string that contains the name, category, and price of an item
             __lt__ = a method that determines if one item is or is not less expensive than another item
    '''
    def __init__(self, name, color, num_tasks):
        Character.__init__(self,name,color,num_tasks)
        self.role = "Evil"
        
    def get_identity(self):
        return "Pretender"
        
    def eliminate(self, target):
        target.alive = False
        print(self.name + " eliminated " + target.name)

class Sheriff(Crewperson):
    '''
    Purpose: An object in this class represents an Item, a product of a store.
    Instance variables: self.store = the store in which the item is from
                        self.name = the name of the item
                        self.price = the price of the item
                        self.category = where on the body the item is worn
    Methods: __init__ = a constructor to initialize instance variables
             __str__ = a method that returns a string that contains the name, category, and price of an item
             __lt__ = a method that determines if one item is or is not less expensive than another item
    '''
    def get_identity(self):
        return "Sheriff"
    
    def encounter(self, target):
        if target.role == "Evil":
            target.alive = False
            print(self.name + " eliminated " + target.name)
        
class Game:
    '''
    Purpose: An object in this class represents an Item, a product of a store.
    Instance variables: self.store = the store in which the item is from
                        self.name = the name of the item
                        self.price = the price of the item
                        self.category = where on the body the item is worn
    Methods: __init__ = a constructor to initialize instance variables
             __str__ = a method that returns a string that contains the name, category, and price of an item
             __lt__ = a method that determines if one item is or is not less expensive than another item
    '''
    def __init__(self, player_list):
        self.player_list = player_list
    
    def check_winner(self):
        tasks_left = 0
        good_count = 0
        evil_count = 0
        dead_evil_count = 0
        dead_good_count = 0

        for i in range(len(self.player_list)):
            if self.player_list[i].role == "Good":
                tasks_left += len((self.player_list[i]).task_list)

            if self.player_list[i].role == "Evil":
                evil_count += 1
                if self.player_list[i].alive == False:
                    dead_evil_count += 1
            
            if self.player_list[i].role == "Good":
                good_count += 1
                if self.player_list[i].alive == False:
                    dead_good_count += 1

        if tasks_left == 0 or dead_evil_count == evil_count:
            print("Crewpersons win!")
            return "C"
        elif (evil_count - dead_evil_count) >= (good_count - dead_good_count):
            print("Pretenders win!")
            return "P"

        else:
            return "-"

    def meeting(self):
        Tie = False
        voting_dict = {}
        alive_list = []

        for i in range(len(self.player_list)):
            voting_dict[self.player_list[i].name] = 0

        for i in range(len(self.player_list)):
            if self.player_list[i].alive == True:
                alive_list.append(self.player_list[i])
                voting_dict[self.player_list[i].name] == 0

        for i in range(len(alive_list)):
            if alive_list[i].alive == True:
                vote = random.choice(alive_list)
                while vote.name == alive_list[i].name:
                    vote = random.choice(alive_list)
                print(alive_list[i].name + " voted for " + vote.name)
                voting_dict[vote.name] += 1
        
        loser_votes = max(voting_dict.values())

        for i in range(len(alive_list)):
            if voting_dict[alive_list[i].name] == loser_votes:
                loser_name = alive_list[i].name
                loser = alive_list[i]

        for i in range(len(alive_list)):
            if alive_list[i].name != loser_name:
                if voting_dict[alive_list[i].name] == loser_votes:
                    Tie = True
                    break

        if Tie == True:
            print("Nobody was voted out.")
        else:
            print(loser_name + " was voted out and eliminated.")
            loser.alive = False

            # vote = random.choice(self.player_list)
            # while vote.alive == False:
            #     vote = random.choice(self.player_list)
            # for i in range(len(self.player_list)):
            #     if self.player_list[i].alive == True:
            #         print(self.player_list[i].name + " voted for " + vote.name)
            # print(vote.name + " was voted out and eliminated.")
            # vote.alive = False
            
        
        
    def play_game(self):
        keep_playing = True
        while keep_playing == True:
            for i in range(len(self.player_list)):
                if self.player_list[i].role == "Good":
                    for j in range(random.randrange(1,4)):
                         self.player_list[i].complete_task()
            for i in range(len(self.player_list)):
                 if self.player_list[i].role == "Evil" and self.player_list[i].alive == True:
                      p_choice = random.choice(self.player_list)
                      if p_choice.role == "Good" and p_choice.alive == True:
                          self.player_list[i].eliminate(p_choice)
            for i in range(len(self.player_list)):
                if self.player_list[i].get_identity() == "Sheriff" and self.player_list[i].alive == True:
                    s_choice = random.choice(self.player_list)
                    if s_choice.role == "Evil" and s_choice.alive == True:
                        self.player_list[i].encounter(s_choice)
            if self.check_winner() == "-":
                self.meeting()
                if self.check_winner() == "-":
                    keep_playing = True
                else:
                    keep_playing = False
            else:
                keep_playing = False
        

            
        
g = Game([
        Pretender('James Joyce', 'Blue', 4),
        Crewperson('Nate', 'Orange', 4),
        Pretender('Markov', 'Red', 4),
        Crewperson('Fanatical', 'Indigo', 4),
        Crewperson('Nebula', 'Black', 4),
        Sheriff('basicbot', 'White', 4)])


g.play_game()




        
        
