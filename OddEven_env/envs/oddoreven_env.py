import gym
from gym import error, spaces, utils
from gym.utils import seeding

class OddorevenEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self,small=2,large=10):
    self.input=0
    self.state=0
    self.action_space = spaces.Discrete(5)
    self.observation_space = spaces.Discrete(5)
    self.seed()

  def _seed(self, seed=None):
    self.np_random, seed = seeding.np_random(seed)
    return [seed]    
   
  
  def _step(self, action):
    return 0, 0, 0, {} 

  def _reset(self):
    return 0     
    
  def _render(self, mode='human', close=False):
    return 0     
    
