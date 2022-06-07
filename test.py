
Matrix1 = [[6,5,4,3,2,1,2,3],
            [5,4,3,2,1,0,1,2],
            [6,5,4,3,2,1,2,3],
            [7,6,5,4,3,2,3,4],
            [8,7,6,5,4,3,4,5],
            [9,8,7,6,5,4,5,6],
            [10,9,8,7,6,5,6,7],
            [11,10,9,8,7,6,7,8],
            [12,11,10,9,8,7,8,9],
            [13,12,11,10,9,8,9,10],
            [14,13,12,11,10,9,10,11]]


'''
6 5 4 3 2 1 2 3
5 4 3 2 1 0 1 2
6 5 4 3 2 1 2 3
7 6 5 4 3 2 3 4
8 7 6 5 4 3 4 5
9 8 7 6 5 4 5 6
10 9 8 7 6 5 6 7
11 10 9 8 7 6 7 8
12 11 10 9 8 7 8 9
13 12 11 10 9 8 9 10
14 13 12 11 10 9 10 11
'''


engine_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
engine_right = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        



class Bahnplanung:
    def __init__(self, matrix, start_x, start_y):
        self.direction = 'FW'
        self.matrix = matrix
        self.start_x = start_x
        self.start_y = start_y
      
        self.engine_speed = 200
        self.neg_engine_speed = 0 - self.engine_speed
        self.field_length = 200
        self.drive_time_to_next_field = self.field_length / 0.0735

    
    def find_path(self):
        print("pathfindng start")
        x = self.start_x
        y = self.start_y
        value = self.matrix[x][y]
        value_front = 1000
        value_right = 1000
        value_left = 1000
        value_back = 1000
        #value_list = [value_front, value_right, value_back, value_left]
        while value != 0:
            print("field [",x,"][",y,"]")
            try:
                value_front = matrix[x][y-1]
            except:
                value_front = 1000
            try:
                value_right = matrix[x+1][y]
            except:
                value_right = 1000
            try:
                value_left = matrix[x-1][y]
            except:
                value_left = 1000
            try:
                value_back = matrix[x][y+1]
            except:
                value_back = 1000

            lowest = 1000
            lowest_direction = None
            if value_front < lowest:
                lowest = value_front
                lowest_direction = 'FW'
            if value_right < lowest:
                lowest = value_right
                lowest_direction = 'R'
            if value_back < lowest:
                lowest = value_back
                lowest_direction = 'BW'
            if value_left < lowest:
                lowest = value_left
                lowest_direction = 'L'
            match lowest_direction:
                case 'FW':
                    self.go_FW()
                    y = y-1
                case 'R':
                    self.go_right()
                    x = x+1
                case 'L':
                    self.go_left()
                    x = x-1
                case 'BW':
                    self.go_back()
                    x = y+1
            


    def go_FW(self):
        print("go_FW")

    def go_right(self):
        print("go_right")
    
    def go_left(self):
        print("go_left")
    
    def go_back(self):
        print("go_back")
