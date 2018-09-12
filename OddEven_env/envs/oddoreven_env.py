import gym
from gym import error, spaces, utils
from gym.utils import seeding
import random
import os

class OddorevenEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self,max_reward=100):
    self.max_reward = max_reward
    self.state=0
    self.counter=0
    self.action_space = spaces.Discrete(5)
    self.observation_space = spaces.Discrete(5)
    self.seed()
    with open('player-profile-1.txt') as f:
      self.lines = f.read().splitlines()
    #print(self.lines)

  def seed(self, seed=None):
    self.np_random, seed = seeding.np_random(seed)
    return [seed]    
   
  
  def step(self, action):
    done = False
    assert self.action_space.contains(action)
    self.counter += 1
    self.state = int(self.lines[self.counter])
    if action == self.state:
      done = True
      reward = self.max_reward - (self.counter/(self.counter+5))*self.max_reward  # formula for 
    else:
      reward = 0
    return self.state, reward, done, {} 

  def reset(self):
    self.state = random.randrange(1,6)
    self.counter = 0
    return self.state     
    
  def render(self, mode='human', close=False):
    return 0     
    
