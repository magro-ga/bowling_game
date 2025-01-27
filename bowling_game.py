class BowlingGame:
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        pins = self.convert_input(pins)
        if not self.frames or len(self.frames[-1]) == 2 or sum(self.frames[-1]) == 10:
            self.frames.append([pins])
        else:
            self.frames[-1].append(pins)

    def convert_input(self, pins):
        if pins == 'X':
            return 10
        elif pins == '/':
            return 10 - self.frames[-1][0]
        elif pins == '-':
            return 0
        else:
            return int(pins)

    def score(self):
        total_score = 0
        for i in range(10):  # Max 10 frames
            frame = self.frames[i]
            if self.is_strike(frame):
                total_score += 10 + self.strike_bonus(i)
            elif self.is_spare(frame):
                total_score += 10 + self.spare_bonus(i)
            else:
                total_score += sum(frame)
        return total_score

    def is_strike(self, frame):
        return len(frame) == 1 and frame[0] == 10

    def is_spare(self, frame):
        return len(frame) == 2 and sum(frame) == 10

    def strike_bonus(self, frame_index):
        next_frames = self.frames[frame_index + 1:]
        rolls = [roll for frame in next_frames for roll in frame]
        return sum(rolls[:2])

    def spare_bonus(self, frame_index):
        if frame_index + 1 < len(self.frames):
            return self.frames[frame_index + 1][0]
        return 0

def parse_rolls(frames):
    rolls = []
    frames_list = frames.split()
    
    for i, frame in enumerate(frames_list):
        if i < 9:
            if frame == 'X':  # strike
                rolls.append(10)
            elif '/' in frame:  # spare
                rolls.append(int(frame[0]) if frame[0] != '-' else 0)
                rolls.append(10 - (int(frame[0]) if frame[0] != '-' else 0))
            else:
                rolls.append(int(frame[0]) if frame[0] != '-' else 0)
                rolls.append(int(frame[1]) if frame[1] != '-' else 0)
        else:
            rolls.extend(
                10 if char == 'X' else 10 - rolls[-1] if char == '/' else 0 if char == '-' else int(char)
                for char in frame
            )   

    return rolls

def calculate_score(rolls):
    total_score = 0
    roll_index = 0
    
    for frame in range(9):
        if rolls[roll_index] == 10:
            total_score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
            roll_index += 1
        elif rolls[roll_index] + rolls[roll_index + 1] == 10:
            total_score += 10 + rolls[roll_index + 2]
            roll_index += 2
        else:
            total_score += rolls[roll_index] + rolls[roll_index + 1]
            roll_index += 2    
        
    total_score += sum(rolls[roll_index:roll_index + 3])
    return total_score

def bowling_score(frames):
    rolls = parse_rolls(frames)
    return calculate_score(rolls)