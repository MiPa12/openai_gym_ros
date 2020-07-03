#!/usr/bin/env python
from gym.envs.registration import register
from gym import envs


def RegisterOpenAI_Ros_Env(task_env, max_episode_steps=10000):
    """
    Registers all the ENVS supported in OpenAI ROS. This way we can load them
    with variable limits.
    Here is where you have to PLACE YOUR NEW TASK ENV, to be registered and accesible.
    return: False if the Task_Env wasnt registered, True if it was.
    """

    ###########################################################################
    # MovingCube Task-Robot Envs

    result = True

    # Cubli Moving Cube
    if task_env == 'TurtleBot2Maze-v0':

        register(
            id=task_env,
            entry_point='openai_ros.task_envs.turtlebot2.turtlebot2_maze:TurtleBot2MazeEnv',
            max_episode_steps=max_episode_steps,
        )
        # import our training environment
        from openai_ros.task_envs.turtlebot2 import turtlebot2_maze

    elif task_env == 'MyTurtleBot2Wall-v0':

        register(
            id=task_env,
            entry_point='openai_ros.task_envs.turtlebot2.turtlebot2_wall:TurtleBot2WallEnv',
            max_episode_steps=max_episode_steps,
        )
        # import our training environment
        from openai_ros.task_envs.turtlebot2 import turtlebot2_wall

    elif task_env == 'MyTurtleBot2WillowGarage-v0':

        register(
            id=task_env,
            entry_point='openai_ros.task_envs.turtlebot2.turtlebot2_willow_garage:TurtleBot2WillowGarageEnv',
            max_episode_steps=max_episode_steps,
        )
        # import our training environment
        from openai_ros.task_envs.turtlebot2 import turtlebot2_willow_garage

    elif task_env == 'TurtleBot3World-v0':

        register(
            id=task_env,
            entry_point='openai_ros.task_envs.turtlebot3.turtlebot3_world:TurtleBot3WorldEnv',
            max_episode_steps=max_episode_steps,
        )

        # import our training environment
        from openai_ros.task_envs.turtlebot3 import turtlebot3_world


    # Add here your Task Envs to be registered
    else:
        result = False

    ###########################################################################

    if result:
        # We check that it was really registered
        supported_gym_envs = GetAllRegisteredGymEnvs()
        #print("REGISTERED GYM ENVS===>"+str(supported_gym_envs))
        assert (task_env in supported_gym_envs), "The Task_Robot_ENV given is not Registered ==>" + \
            str(task_env)

    return result


def GetAllRegisteredGymEnvs():
    """
    Returns a List of all the registered Envs in the system
    return EX: ['Copy-v0', 'RepeatCopy-v0', 'ReversedAddition-v0', ... ]
    """

    all_envs = envs.registry.all()
    env_ids = [env_spec.id for env_spec in all_envs]

    return env_ids
