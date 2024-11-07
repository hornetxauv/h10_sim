# h10_sim

h10's gazebo harmonic sim

prepare 3 terminals to run the sim
- cd h10_sim
- cd h10_sim
- colcon build

this sources setup.bash aswell as sets the enironment parameters
- source install/setup_custom.bash

new terminal
- ros2 run ros_gz_bridge parameter_bridge --ros-args -p config_file:=ros_gz_bridge.yaml

new terminal
- colcon build
- source install/setup_custom.bash
- ros2 run control IMU
