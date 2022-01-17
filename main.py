from my_model import Maze
from UCB import UCBTable
from spinup.utils.logx import EpochLogger

#before main loop of UCB, each bandit should be chosen for once, and do not increase T in this time
logger = EpochLogger()
# logger.save_config(locals())

def learn_init(RL):
    for action in RL.actions:
        print(RL.actions)
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
            
            #['u', 'd', 'l', 'r'] = [0,1,2,3]
            logger.store(UCBmax=RL.UCBtable[RL.max_index])
            logger.store(ut_d=RL.actions_table[1][1]/RL.actions_table[1][0])
            logger.store(ut_u=RL.actions_table[0][1]/RL.actions_table[0][0])
            logger.store(ut_l=RL.actions_table[2][1]/RL.actions_table[2][0])
            logger.store(ut_r=RL.actions_table[3][1]/RL.actions_table[3][0])
            # break while loop when end of this episode
            if done:
                break

    # end of game
    logger.log_tabular('UCBmax', with_min_and_max=True)
    logger.log_tabular('ut_d', with_min_and_max=True)
    logger.log_tabular('ut_u', with_min_and_max=True)
    logger.log_tabular('ut_l', with_min_and_max=True)
    logger.log_tabular('ut_r', with_min_and_max=True)
    logger.dump_tabular()
    print('game over')
    env.destroy()

#ucb learn
#UCB WILL FOREVER CHANGED TO THESE UNEXplored ,because of the increase of t
if __name__ == "__main__":
    env = Maze()
    RL = UCBTable(actions=list(range(env.n_actions)))
    learn_init(RL)

    env.after(50, update)
    env.mainloop()
