from gym.envs.registration import register

register(
    id='OddorEven-v1',
    entry_point='OddEven_env.envs:oddoreven_env',
)
