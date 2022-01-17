import numpy as np
import pandas as pd
from math import *
import scipy.signal
from gym.spaces import Box, Discrete


# I may need a table to memory each Gaossian score,mean,variance?
#from mofan education

#UCB need time to be choosed and total
#first all bandit should be chosen to avoid dividing zero

class UCBTable:
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions  # a list
        self.T = 1
        self.actions_table = {}
        for action in actions:
            self.actions_table.update({action:[0,0]})#  [chosen times,total score]

        #used to anlysis result
        self.UCBtable =[0,0,0,0]
        self.max_index =0 
    
    def choose_action(self, observation):
        self.check_state_exist(observation)
        # action selection
        # if np.random.uniform() < self.epsilon:
        #     # choose best action
        #     state_action = self.q_table.loc[observation, :]
        #     # some actions may have the same value, randomly choose on in these actions
        #     action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        # else:
        #     # choose random action
        #     action = np.random.choice(self.actions)
        
        #choose best UCB
        max_UCB = 0
        index = 0 
        for action in self.actions:
            temp_score = self.UCB(action)
            if(temp_score>max_UCB):
                max_UCB = temp_score
                self.max_index = index
            index+=1
        self.T +=1
        self.UCBtable[self.max_index] = max_UCB
        # print(max_UCB)
        return self.actions[self.max_index]

    def learn(self, state, action, reward, state_next,init = False):
        self.check_state_exist(state_next)
        times_past,totalreward_past = self.actions_table[action][0],self.actions_table[action][1]
        self.actions_table.update({action:[times_past+1,totalreward_past+reward]})
        

    def check_state_exist(self, state):
        #TODO
        # if state not in self.q_table.index:
        #     # append new state to q table
        #     self.q_table = self.q_table.append(
        #         pd.Series(
        #             [0]*len(self.actions),
        #             index=self.q_table.columns,
        #             name=state,
        #         )
        #     )
        pass
    
    def UCB(self,a):
        #?? the FORMULA of UCB should be more clearly
        UCB_score = self.actions_table[a][1]/self.actions_table[a][0]+sqrt(2*log2(self.T)/self.actions_table[a][0])
        return UCB_score
        
            