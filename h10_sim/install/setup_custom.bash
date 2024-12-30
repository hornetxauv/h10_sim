#!/bin/bash
# Source the default setup.bash generated by colcon
source /home/jelly/h10_sim/h10_sim/install/setup.bash

# Append GZ_SIM_RESOURCE_PATH
export GZ_SIM_RESOURCE_PATH=/home/jelly/h10_sim/h10_sim/install/share/simple_auv/worlds:/home/jelly/h10_sim/h10_sim/install/share/simple_auv/models:/home/jelly/h10_sim/h10_sim/install/share/simple_auv/worlds/media/materials/scripts:$GZ_SIM_RESOURCE_PATH
echo 'GZ_SIM_RESOURCE_PATH: $GZ_SIM_RESOURCE_PATH'