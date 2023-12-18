import sys

class Stack:
    def __init__(self):
        self.data_list = []
    
    def add(self,value):
        self.data_list.append(value)

    def pop(self):
        try: print(self.data_list.pop())
        except: print(-1)

    def check_data(self):
        if len(self) == 0: print(1)
        else: print(0)

    def last_data(self):
        try: print(self.data_list[-1])
        except: print(-1)
            
    def __len__(self):
        return len(self.data_list)
        
stack = Stack()
for i in range(int(input())):
    # x = list(map(int,sys.stdin.readline().split()))
    x = list(map(int, input().split()))
    
    if len(x) == 2:
        stack.add(x[1])
    else:
        if x[0] == 2: stack.pop()
        elif x[0] == 3: print(len(stack))
        elif x[0] == 4: stack.check_data()
        else: stack.last_data()