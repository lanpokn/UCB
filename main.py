"""
Reinforcement learning maze example.
Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].
This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.
View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

# from my_model import Maze
# from Qlearn import QLearningTable

# def learn_init(actions):
#     for action in actions:
#         self.learn(s)
#     pass

# # qlearn update
# def update():
#     for episode in range(100):
#         # initial observation
#         observation = env.reset()

#         while True:
#             # fresh env
#             env.render()

#             # RL choose action based on observation
#             action = RL.choose_action(str(observation))

#             # RL take action and get next observation and reward
#             observation_, reward, done = env.step(action)

#             # RL learn from this transition
#             RL.learn(str(observation), action, reward, str(observation_))

#             # swap observation
#             observation = observation_

#             # break while loop when end of this episode
#             if done:
#                 break

#     # end of game
#     print('game over')
#     env.destroy()
    

# if __name__ == "__main__":
#     env = Maze()
#     RL = QLearningTable(actions=list(range(env.n_actions)))

#     env.after(100, update)
#     env.mainloop()









from my_model import Maze
from UCB import UCBTable

#before main loop of UCB, each bandit should be chosen for once, and do not increase T in this time
def learn_init(RL):
    for action in RL.actions:
        # initial observation each time
        observation = env.reset()
        env.render()
        observation_, reward, done = env.step(action)

        # RL learn from this transition
        RL.learn(str(observation), action, reward, str(observation_),init = True)

        # swap observation, in tradition MAB, they are the same
        observation = observation_
    pass
def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

#ucb learn
if __name__ == "__main__":
    env = Maze()
    RL = UCBTable(actions=list(range(env.n_actions)))
    learn_init(RL)

    env.after(100, update)
    env.mainloop()
