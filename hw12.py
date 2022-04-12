import random
class Character:
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
    def get_identity(self):
        return "Crewperson"
        
    def complete_task(self):
        if len(self.task_list) > 1:
            print(self.name + " has completed task: " + self.task_list[0])
            self.task_list.remove(self.task_list[0])
        elif len(self.task_list) == 1:
            print(self.name + " has completed all their tasks")
        
class Pretender(Character):
    def __init__(self, name, color, num_tasks):
        Character.__init__(self,name,color,num_tasks)
        self.role = "Evil"
        
    def get_identity(self):
        return "Pretender"
        
    def eliminate(self, target):
        target.alive = False
        print(self.name + " eliminated " + target.name)

class Sheriff(Crewperson):
    def get_identity(self):
        return "Sheriff"
    
    def encounter(self, target):
        if target.role == "Evil":
            target.alive = False
            print(self.name + " eliminated " + target.name)
        
class Game:
    def __init__(self, player_list):
        self.player_list = player_list
    
    def check_winner(self):
        tasks_left = 100
        good_count = 0
        evil_count = 0
        dead_evil_count = 0
        dead_good_count = 0
        for i in range(len(self.player_list)):
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
        # name_list = []
        # for i in range(len(self.player_list)):
        #     name_list.append(self.player_list[i].name)
        #     self.player_list[i].name.vote_count = 0
        # loser = name_list[0]
        # for i in range(len(name_list)):
        #     for j in range(len(name_list)):
        #         vote = random.choice(name_list)
        #         while vote == name_list[i] or self.player_list[j].alive == False:
        #             vote = random.choice(name_list)
        #         print(name_list[i] + " voted for " + vote)
        #         self.player_list[i].name.vote_count += 1
        #         break
        # for j in range(len(name_list)):
        #     if name_list[j].vote_count > loser.vote_count:
        #         loser = self.player_list[j]
        # print(loser + " was voted out and eliminated")
        
        # for i in range(len(self.player_list)):
        #     if self.player_list[i].name == loser:
        #         self.player_list[i].alive = False
            vote = random.choice(self.player_list)
            while vote.alive == False:
                vote = random.choice(self.player_list)
            for i in range(len(self.player_list)):
                if self.player_list[i].alive == True:
                    print(self.player_list[i].name + " voted for " + vote.name)
            print(vote.name + " was voted out and eliminated.")
        
        
    def play_game(self):
        while self.check_winner() == "-":
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
                self.check_winner()
            
        
g = Game([
        Pretender('Rachel', 'Blue', 6),
        Crewperson('Fatima', 'Orange', 6),
        Pretender('Emily', 'Red', 6),
        Crewperson('Nakul', 'Indigo', 6),
        Crewperson('Demond', 'Pink', 6),
        Crewperson('Eric', 'Yellow', 6),
        Crewperson('Chris', 'Teal', 6),
        Crewperson('Aishwarya', 'Brown', 6),
        Crewperson('Athreyi', 'Purple', 6),
        Sheriff('Adrika', 'White', 6)])









        
        
