import math
import itertools

class Game:
    def __init__(self, max_flow = 10, total_max_flow = 10):
        self.max_flow  = max_flow
        self.total_max_flow = total_max_flow

    def reset(self, targetA, targetB):
        self.done = False
        self.scoreA,  self.scoreB  = 0, 0
        self.volA,    self.volB    = 0, 0
        self.targetA, self.targetB = targetA, targetB
        self.history_actionA = []
        self.history_actionB = []
        self.history_flowA = []
        self.history_flowB = []

    def play_wo_print(self, targetA, targetB):
        self.reset(targetA, targetB)
        while self.done == False:
            decisionA, decisionB, flowA, flowB = self.step()
        return self.scoreA + self.scoreB

    def play_with_print(self, targetA, targetB):
        self.reset(targetA, targetB)
        while self.done == False:
            decisionA, decisionB, flowA, flowB = self.step()
            print(f"Dec A: {decisionA} | Flow A: {flowA} | Vol/Tar A: {self.volA}/{self.targetA} |||| Vol/Tar B: {self.volB}/{self.targetB} | Dec B: {decisionB} | Flow B: {flowB} | ")
        score = self.scoreA + self.scoreB
        print(f"Total score: {score}")
        return score

    def step(self):
        if not self.done:
            # Replace with your strategy
            actionA = self.strategy_sharing_half(self.volA, self.targetA)
            actionB = self.strategy_sharing_half(self.volB, self.targetB)

            # 0 <= flow <= each_max_flow
            flowA   = min(actionA, self.max_flow)
            flowA   = max(0, flowA)
            flowB   = min(actionB, self.max_flow)
            flowB   = max(0, flowB)

            # flow constraint
            if (flowA + flowB > self.total_max_flow):
                flowA, flowB = 0, 0

            self.history_actionA.append(actionA)
            self.history_actionB.append(actionB)
            self.history_flowA.append(flowA)
            self.history_flowB.append(flowB)
        
            self.volA   += flowA
            self.volB   += flowB
            self.scoreA += flowA
            self.scoreB += flowB
            score = self.scoreA + self.scoreB

            if (self.volA == self.targetA) and (self.volB == self.targetB): 
                self.done = True
            elif (self.volA > self.targetA) or (self.volB > self.targetB):
                self.scoreA, self.scoreB = 0, 0
                self.done = True
            else:
                self.scoreA -= 1 # Punishment for finishing late
                self.scoreB -= 1 # Punishment for finishing late
                self.done = False
            
            return actionA, actionB, flowA, flowB
            
    def strategy_sharing_half(self, vol, target):
        missing_part = target - vol
        action = min(missing_part, self.max_flow, math.floor(self.total_max_flow/2))
        return action
    
    def strategy_new(self, vol, target, history_action, history_flow):
        pass

import os
if __name__ == "__main__":
    os.system('cls')
    game = Game()

    # # Play a single game
    # game.play_with_print(7,7)

    # Test strategy
    S = list(range(101))  # S = [0, 1, ..., 30]
    target_list = itertools.product(S, S)
    total_score = 0

    for target in target_list:
        score = game.play_wo_print(target[0], target[1])
        total_score += score
        print(f"target: {target} | score: {score}")
    
    print(f"Strategy score: {total_score}")