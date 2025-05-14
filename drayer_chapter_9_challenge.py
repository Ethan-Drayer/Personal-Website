pointer = {}

class Frames:
    def __init__(self, first_roll, second_roll = 0, third_roll = 0):
        self.first_roll = first_roll
        self.second_roll = second_roll
        self.third_roll = third_roll

    def implementing_points1_9(self):
        """This creates the inside of the dictionary pointer for rounds 1 - 9"""
        if self.first_roll + self.second_roll > 10:
            return "try again"
        if self.first_roll == 10:
            points = [self.first_roll, "strike"]
            return points

        elif self.first_roll + self.second_roll == 10:
            points = [self.first_roll, self.second_roll, "spare"]
            return points

        else:
            points =[self.first_roll, self.second_roll, "open frame"]
            return points

    def implementing_points10(self):
        """This creates the inside of the dictionary pointer for round 10"""
        if self.first_roll == 10:
            points = [self.first_roll, self.second_roll, self.third_roll, "last frame three rolls"]
            return points

framing = ["Frame 1", "Frame 2", "Frame 3", "Frame 4", "Frame 5", "Frame 6",
           "Frame 7", "Frame 8", "Frame 9", "Frame 10"]
framing_copy = framing[:]
def framework(values):
    """Creates the dictionary pointer so to put into the scoring function"""
    step = {framing[0] : values}
    pointer.update(step)
    del framing[0]
    return pointer

def scoring(dictionary):
    """takes the pointer dictionary and scores the total points after each round"""
    self_destruct_number = []
    self_destruct_type = []
    score = 0
    for key, value in dictionary.items():
        for pieces in value:
            if pieces != str(pieces):
                self_destruct_number.append(pieces)
            else:
                self_destruct_type.append(pieces)

    self_destruct_number.append(0)
    self_destruct_number.append(0)

    while self_destruct_type:
        if self_destruct_type[0] == "strike":
            del self_destruct_type[0]
            score += self_destruct_number[0]
            score += self_destruct_number[1]
            score += self_destruct_number[2]
            del self_destruct_number[0]

        elif self_destruct_type[0] == "spare":
            del self_destruct_type[0]
            for index in range(2):
                score += self_destruct_number[0]
                del self_destruct_number[0]
            score += self_destruct_number[0]

        elif self_destruct_type[0] == "open frame":
            del self_destruct_type[0]
            for index in range(2):
                score += self_destruct_number[0]
                del self_destruct_number[0]

        elif self_destruct_type[0] == "last frame three rolls":
            del self_destruct_type[0]
            score += sum(self_destruct_number)

    return score

rounds = 0
while rounds <= 9:
    roll2 = 0
    print(f"You are now rolling for {framing_copy[rounds]}")
    print("How many pins did you knock over on your first roll(0-10):")
    try:
        roll1 = int(input())
    except:
        print("Enter a number 1-10")
        continue
    if roll1 != 10 or rounds == 9:
        print("How many pins did you knock over on your second roll(0-10):")
        try:
            roll2 = int(input())
        except:
            print("Enter a number 1-10")
            continue

    if 0 <= int(roll1) <= 10 and 0 <= int(roll2) <= 10:
        if roll1 + roll2 >= 10:
            if rounds == 9:
                print("How many pins did you knock over on your third roll?")
                try:
                    roll3 = int(input())
                except:
                    print("Enter a number 1-10")
                    continue
                complex = Frames(roll1, roll2, roll3)
                inner = complex.implementing_points10()
                arranged_points = framework(inner)
                for time, pins in arranged_points.items():
                    print(f"{time}: {pins}")
                scored_points = scoring(arranged_points)
                print(f"You have {scored_points} total points")
                rounds += 1
                continue

            else:
                complex = Frames(roll1, roll2)
                inner = complex.implementing_points1_9()
                if inner == "try again":
                    continue
                arranged_points = framework(inner)
                for time, pins in arranged_points.items():
                    print(f"{time}: {pins}")
                scored_points = scoring(arranged_points)
                print(f"You have {scored_points} total points")
                rounds += 1
                continue

        else:
            complex = Frames(roll1, roll2)
            inner = complex.implementing_points1_9()
            if inner == "try again":
                continue
            arranged_points = framework(inner)
            for time, pins in arranged_points.items():
                print(f"{time}: {pins}")
            scored_points = scoring(arranged_points)
            print(f"You have {scored_points} total points")
            rounds += 1
            continue
    else:
        print("The most amount of pins that can be knocked over is 10")