from queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDist(self):
        pass

    def CreateChildren(self):
        pass

class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def CreateChildren(self):
        if not self.children:
            i = self.value.index('0')
            vals = [[i - 1, 'Left'], [i + 1, 'Right'], [i - 3, 'Up'], [i + 3, 'Down']]
            for val in vals:
                if val[0] >= 0 and val[0] < len(self.value):
                    if val[1] == 'Up' or val[1] == 'Down':
                        if val[0] % 3 != i % 3:
                            temp = self.value
                            temp = temp[:i] + temp[val[0]] + temp[i+1:]
                            temp = temp[:val[0]] + '0' + temp[val[0]+1:]
                            child = State_String(temp, self)
                            self.children.append(child)
                    elif val[1] == 'Left' or val[1] == 'Right':
                        if val[0] // 3 == i // 3:
                            temp = self.value
                            temp = temp[:i] + temp[val[0]] + temp[i+1:]
                            temp = temp[:val[0]] + '0' + temp[val[0]+1:]
                            child = State_String(temp, self)
                            self.children.append(child)

class AStar_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_String(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("Goal of " + self.goal + " is not possible!")
        return self.path

if __name__ == "__main__":
    start1 = "123456780"
    goal1 = "123456780"
    print("Starting...")
    a = AStar_Solver(start1, goal1)
    a.Solve()
    for i in range(len(a.path)):
        print("%d) " %i + a.path[i])
