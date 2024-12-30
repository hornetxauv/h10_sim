# h10_sim

h10's gazebo sim

Because of abundance of documentation, the sim uses gazebo garden.
To download gazebo garden:
- https://gazebosim.org/docs/garden/install/
- Even if it's EOL, since we use an older version of ROS2, the compatibility is better

For integration between ROS2 and Gazebo:
- sudo apt-get install ros-humble-ros-gzgarden

prepare 3 terminals to run the sim
- cd h10_sim
- cd h10_sim
- colcon build
- source install/setup_custom.bash

new terminal
- ros2 run ros_gz_bridge parameter_bridge --ros-args -p config_file:=ros_gz_bridge.yaml

new terminal
- colcon build
- source install/setup_custom.bash
- ros2 run control IMU
