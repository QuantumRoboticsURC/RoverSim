# LIGHT RoverSim
repo where robot LIGHT simulation will be held


This repo contains a simulation 
of the Manchester robotics "puzzlebot" robot, which we plan to use 
as computationaly cheap simulation of the Q-Mars. For this we plan to map the pose of the base_link given by gazebo into the imu and gps topics and to test the autonomous navigation codes.

To use the puzzlebot simulation:
- clone this repository in the src folder of your ros workspace
- rename the folder called 'RoverSim' to 'puzzlebot_sim'
- do catkin_make
- run:
` roslaunch puzzlebot_sim our_puzlebot_sim.launch `
- if your are using this simulation to test algorithms within the [autonomous nav package](https://github.com/QuantumRoboticsURC/qr_navigation) the node that will generate the gps and imu equivalents is the [OdomPublisherPuzzlebotSim.py](https://github.com/QuantumRoboticsURC/qr_navigation/blob/main/scripts/OdomPublisherPuzzlebotSim2.py) node  

before running this roslaunch please ensure:
- all the packages within this repo are located at the src/<package_name> 
level of your workspace
- you have built all the ros packeges contained in this repo
- you have installed the following:
    - sudo apt-get install ros-melodic-joint-state-publisher
    - sudo apt-get install ros-melodic-controller-manager
    - sudo apt-get install ros-melodic-gazebo-ros-control
    - sudo apt-get install ros-melodic-joint-state-contoller
    - sudo apt-get install ros-melodic-effort-controllers
    - sudo apt-get install ros-melodic-position-controllers
