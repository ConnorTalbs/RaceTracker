import pandas as pd
class race:
    def __init__(self,name,players,rating) -> None:
        self.name = name
        self.players = players
        self.rating = rating
class player:
    def __init__(self,name,times,car) -> None:
        self.name = name
        self.times = times
        self.car = car
        pass
name = []
car = []
time1 = []
while(True):
    name.append(input('Name: '))
    car.append(input('Car: '))
    time1.append(input('Time 1: '))
    if input('Done?(y/n): ') == 'y':
        break

test = {'Name':name,'Car':car,'Time1':time1}

output = {'Name':['Ty Sandman','Connor Talbot'],'Car':['Mazda Miata','Ford Focus'],'Time1':['10.2','9.8']}

#play = player(name, times, car)
#col1 = 'X'
#col2 = 'Y'

#data = pd.DataFrame.from_dict({'Name':['Ty Sandman','Connor Talbot'],'Car':['Mazda Miata','Ford Focus'],'Time1':['10.2','9.8']})
data = pd.DataFrame.from_dict(test)
data.to_excel('sample_data.xlsx', sheet_name='Sheet1', index=False)