# RoverSim
repo where robot simulation will be held


Until Q-Mars simulation is finished we will be using a simulation 
of the Manchester robotics "puzzlebot" robot, we plan to map the 
pose of the base_link given by gazebo into the imu and gps topics
and test the autonomous navigation code we have developed on it.

To use the puzzlebot simulation run:
` roslaunch puzzlebot_gazebo puzzlebot_gazebo.launch `

before running this roslaunch please ensure:
- all the packages within this repo are located at the src/<package_name> 
level of your workspace
- you have built all the ros packeges contained in this repo
- you have installed the following:
    - sudo apt-get install ros-melodic-joint-state-publisher
    - sudo apt-get install ros-melodic-controller-manager
    - sudo apt-get install ros-melodic-gazebo-ros-control
    - sudo apt-get install ros-melodic-joint-state-controller
    - sudo apt-get install ros-melodic-effort-controllers
    - sudo apt-get install ros-melodic-position-controllers
