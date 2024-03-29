class Environment:
    def __init__(self):
        self.locationCondition = {'A': '0', 'B': '0'}

        if random.randint(0, 1) == 0:
            self.locationCondition['A'] = '1'
        if random.randint(0, 1) == 0:
            self.locationCondition['B'] = '1'

class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print(Environment.locationCondition)
        Score = 0
        vacuumLocation = random.randint(0, 1)
        if vacuumLocation == 0:
            print("Vacuum randomly placed at Location A.")
            if Environment.locationCondition['A'] == '1':
                print("Location A is Dirty.")
                Environment.locationCondition['A'] = '0';
                Score += 1
                print("Location A has been Cleaned.")
                print("Moving to Location B...")
                Score -= 1
                if Environment.locationCondition['B'] == '1':
                    print("Location B is Dirty.")
                    Environment.locationCondition['B'] = '0';
                    Score += 1
                    print("Location B has been Cleaned.")
            else:
                print("Moving to Location B...")
                Score -= 1
                if Environment.locationCondition['B'] == '1':
                    print("Location B is Dirty.")
                    Environment.locationCondition['B'] = '0';
                    Score += 1
                    print("Location B has been Cleaned.")

        elif vacuumLocation == 1:
            print("Vacuum randomly placed at Location B.")
            if Environment.locationCondition['B'] == '1':
                print("Location B is Dirty.")
                Environment.locationCondition['B'] = '0';
                Score += 1
                print("Location B has been Cleaned.")
                print("Moving to Location A...")
                Score -= 1
                if Environment.locationCondition['A'] == '1':
                    print("Location A is Dirty.")
                    Environment.locationCondition['A'] = '0';
                    Score += 1
                    print("Location A has been Cleaned.")
            else:
                print("Moving to Location A...")
                Score -= 1
                if Environment.locationCondition['A'] == '1':
                    print("Location A is Dirty.")
                    Environment.locationCondition['A'] = '0';
                    Score += 1
                    print("Location A has been Cleaned.")
        print("Performance Measurement: " + str(Score))

import random
env = Environment()
vac = SimpleReflexVacuumAgent(env)
