import datetime
class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.score = []
        self.team = team

    def add_score(self,date,score):
        self.date = date
        self.score.append(score)
    def total_score(self):
        total = 0
        for i in range(len(score)):
            total += score[i]
        return total
    def average_score(self):
        total = 0
        for i in range(len(self.score)):
            total += self.score[i]
            average = total/len(self.score)
        return average
torres = Player ('Fernando','Torres','Liverpool FC')
torres.add_score((datetime.date(2012,06,01)),0)
torres.add_score((datetime.date(2012,06,02)),0)
torres.add_score((datetime.date(2012,06,03)),1)
torres.add_score((datetime.date(2012,06,04)),0)
torres.add_score((datetime.date(2012,06,05)),1)
print torres.score
print torres.average_score()

print '#######################################################################'

class Team:
    def __init__(self,name,league,manager_name,points):
        self.full_name = name
        self.one_league = league
        self.manage = manager_name
        self.team_points = points
        self.players = []
    def add_player(self,player)
        self.player = player
        self.players.append(player)

    spain = Team ('Barca','Premiership','Kaka',2)
    portugal = Team ('manU','Premiership','Gatoso',1)

    def __str__(self):
        
    
        
        
