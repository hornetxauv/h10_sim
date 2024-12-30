# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Int32MultiArray
# from controls_movement.thruster_allocator import ThrustAllocator

# t = ThrustAllocator()


# def publisher():
#     # Initialize the ROS node
#     rclpy.init()
#     rclpy.create_node('int_list_publisher')
    
#     # Create a publisher that publishes to the 'thruster_control' topic
#     pub = Node.create_publisher('thruster_control', Int32MultiArray, queue_size=10)
    
#     # Set the loop rate (1 Hz in this case)
#     rate = Node.create_rate(1)  # 1 Hz

#     # Define the list of 7 integers
#     int_list = t.getThrustPwm([10, 0, 0])

#     # Prepare the message
#     msg = Int32MultiArray()
#     msg.data = int_list

#     # Main loop to keep publishing the message
#     while rclpy.ok():
#         Node.get_logger().info(f"Publishing: {int_list}")
#         pub.publish(msg)
#         rate.sleep()
# def main():
#     publisher()
# if __name__ == '__main__':
#     try:
#         main()
#     except rclpy.ROSInterruptException:
#         pass

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from controls_movement.thruster_allocator import ThrustAllocator

class ThrusterPublisher(Node):
    def __init__(self):
        super().__init__('int_list_publisher')
        self.t = ThrustAllocator()

        # Create publishers for each thruster
        self.thruster_publishers = [
            self.create_publisher(Float64, f'/model/auv/joint/prop_{pos}_joint/cmd_thrust', 10)
            for pos in ['fl', 'fr', 'ml', 'mr', 'rl', 'rr']
        ]

        self.timer = self.create_timer(1.0, self.publish_thrust_values)

    def publish_thrust_values(self):
        # Example target force and torque (replace with your desired values)
        target_xyz_force = [0.05, 0, 0]  # Example: forward force
        target_torque = [0, 0, 0]      # Example: no rotation

        thrust_values = self.t.getThrustPwm(target_xyz_force, target_torque)

        for i, pub in enumerate(self.thruster_publishers):
            msg = Float64()
            msg.data = float(thrust_values[i])  
            pub.publish(msg)

        self.get_logger().info(f"Published thrust values: {thrust_values}")


def main():
    rclpy.init()
    node = ThrusterPublisher()
    try:
        rclpy.spin(node)  
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()



"""
class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')   #this is the name of the node
        self.publisher_ = self.create_publisher(ChatMessage, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = ChatMessage()
        msg.name = "user1"
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    """
