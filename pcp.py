import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
from math import sqrt, atan2, pi
from std_srvs.srv import Trigger

class pcp(Node):
    def __init__(self):
        super().__init__("pcp")
        self.cx = 0.0
        self.cy = 0.0
        self.current_theta = 0.0
        self.subscription1 = self.create_subscription(Pose, "/turtle1/pose", self.turtle_callback, 10)
        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.client = self.create_client(Trigger, 'move_circle')
        self.timer = self.create_timer(0.1, self.my_publisher)
        self.state = 0  

    def turtle_callback(self, msg: Pose):
        self.cx = msg.x
        self.cy = msg.y
        self.current_theta = msg.theta

    def normalize_angle(self, angle):
        while angle > pi:
            angle -= 2 * pi
        while angle < -pi:
            angle += 2 * pi
        return angle

    def move_88(self):
        self.get_logger().info("working inside the function")
        ox, oy = 8.0, 8.0
        distance = sqrt((self.cx - ox)**2 + (self.cy - oy)**2)
        target_angle = atan2(oy - self.cy, ox - self.cx)
        angle_error = self.normalize_angle(target_angle - self.current_theta)

        twist2 = Twist()
        twist2.angular.z = 4 * angle_error
        twist2.linear.x = 1.5 * distance
        self.publisher.publish(twist2)


    def my_publisher(self):
        if self.state == 0:
            ox, oy = 5.5, 8.0
            distance = sqrt((self.cx - ox)**2 + (self.cy - oy)**2)
            target_angle = atan2(oy - self.cy, ox - self.cx)
            angle_error = self.normalize_angle(target_angle - self.current_theta)

            twist = Twist()
            twist.angular.z = 4 * angle_error
            twist.linear.x = 1.5 * distance
            self.publisher.publish(twist)

            if distance < 0.1:
                self.get_logger().info("at (5.5,8)")
                trig = Trigger.Request()
                future = self.client.call_async(trig)
                rclpy.spin_until_future_complete(self, future)
                self.get_logger().info("state changed")
                self.state = 1

        elif self.state == 1:
            time.sleep(2.0)
            self.move_88()

        
def main(args=None):
    rclpy.init(args=args)
    node = pcp()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
