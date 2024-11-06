cmake_minimum_required(VERSION 3.5)

project(simple_auv)

#============================================================================
# Hooks
configure_file(
  "hooks/hook.dsv.in"
  "${CMAKE_CURRENT_BINARY_DIR}/hooks/hook.dsv" @ONLY
)

#============================================================================
# Install models, worlds, and hooks
message("Installing models, worlds, and hooks directories to share/${PROJECT_NAME}")

install(DIRECTORY
  models
  worlds
  ${CMAKE_CURRENT_BINARY_DIR}/hooks
  DESTINATION share/${PROJECT_NAME})

install(CODE "file(APPEND install/setup.bash \"\\nexport GZ_SIM_RESOURCE_PATH=/home/jelly/h10/h10_sim/h10_sim/install/simple_auv/share/simple_auv/worlds:/home/jelly/h10/h10_sim/h10_sim/install/simple_auv/share/simple_auv/worlds/media/materials/scripts:/home/jelly/h10/h10_sim/h10_sim/install/simple_auv/share/simple_auv/models:\$GZ_SIM_RESOURCE_PATH\\n\")")

# Configure and install custom_setup.sh
configure_file(
  "hooks/custom_setup.sh.in"
  "${CMAKE_CURRENT_BINARY_DIR}/hooks/custom_setup.sh" @ONLY
)

install(FILES
  "${CMAKE_CURRENT_BINARY_DIR}/hooks/custom_setup.sh"
  DESTINATION .)


