# h10_sim

h10's gazebo harmonic sim

prepare 3 terminals to run the sim

- colcon build
- source install/setup.bash
- source install/simple_auv/simple_auv/custom_setup.sh

new terminal
- ros2 run ros_gz_bridge parameter_bridge --ros-args -p config_file:=ros_gz_bridge.yaml

new terminal
- ros2 run control IMU
