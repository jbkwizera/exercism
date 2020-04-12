class BowlingGame:
    def __init__(self):
        self.ball1 = -1
        self.rolls = []
        self.count = 0
        self.award = 1

    def roll(self, pins):
        if not 0 <= pins <= 10:
            raise ValueError("Roll value must be between 0 and 10.")
        if self.count == 10:
            raise Exception("Game is already 10 frames.")

        if self.ball1 == -1:                    # new frame
            if pins == 10:                      # strike
                if self.award == 1:
                    if self.count == 9:         # apply extra two balls award on tenth strike by
                        self.award = -1         # not counting this frame and deprecate award
                    else:
                        self.count += 1
                else:                           # strike after award doesnt count
                    self.count = self.count+1 if self.award == 1 else self.count+0.5
            else:
                self.ball1 = pins               # 1st ball of an open/spare frame
                self.count += 0.5               # 1st ball of frame played
        else:
            if self.ball1 + pins <= 10:         # open/spare frame
                if self.ball1 + pins == 10:
                    if self.award == 1:
                        if self.count == 9.5:   # apply one ball award on tenth spare by
                            self.award = -1     # not counting this ball and deprecate award
                        else:
                            self.count += 0.5
                    else:
                        self.count += 0.5       # 2nd ball of a spare frame
                else:
                    self.count += 0.5           # 2nd ball of an open frame
                self.ball1 = -1                 # ready to start a new frame
            else:
                raise ValueError("A frame cannot score more than 10.")
        self.rolls.append(pins)

    def score(self):
        if self.count != 10:
            raise Exception("Incomplete game cannot be scored.")

        accum = [roll for roll in self.rolls]
        i = 0
        while i < len(accum)-3:
            if accum[i] == 10:
                accum[i] += accum[i+1] + accum[i+2]
                i += 1
            else:
                if accum[i] + accum[i+1] == 10:
                    accum[i+1] += accum[i+2]
                i += 2
        return sum(accum)
