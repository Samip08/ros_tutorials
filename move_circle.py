import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger
import time

class move_circle(Node):
    def __init__(self):
        super().__init__("move_circle")
        self.srv = self.create_service(Trigger,'move_circle',self.make_circle)
        self.publisher = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.timer = None
        self.count = 0
        self.total_time = 25

    def make_circle(self, request, response):
        self.get_logger().info('request recieved')
        self.timer = self.create_timer(0.1, self.circlemaker)
        response.success = True
        response.message = 'done'
        return response
    
    def circlemaker(self):
        if self.count >= 20:
            self.publisher.publish(Twist())
            new=Twist()
            new.linear.x=-3.8
            new.linear.y=3.0
            self.publisher.publish(new)       #stops running after 20 iterations of clock with 0.1 its 2 sec
            self.count+=1
            if self.count>=25:
                            self.timer.cancel()               #so it does 3.14*2  a whole circle
                            self.timer= None
                            return

        twist = Twist()
        twist.linear.x = 2.5*3.14             # r times omega   
        twist.angular.z = 3.14
        self.publisher.publish(twist)
        self.count += 1
        time.sleep(0.1)

def main(args=None):
    rclpy.init(args=args)
    node = move_circle()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()