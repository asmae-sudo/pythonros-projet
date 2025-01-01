import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PasswordCLI(Node):
    def __init__(self):
        super().__init__('password_cli')
        self.subscription = self.create_subscription(
            String,
            'password_topic',
            self.listener_callback,
            10
        )
        self.publisher_ = self.create_publisher(String, 'password_request', 10)
        self.get_logger().info("Password CLI node started.")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received password: {msg.data}")

    def send_password_request(self):
        # Envoie une demande de génération de mot de passe
        msg = String()
        msg.data = "Generate password"
        self.publisher_.publish(msg)
        self.get_logger().info("Password request sent.")

def main(args=None):
    rclpy.init(args=args)
    node = PasswordCLI()

    # Envoie la demande de génération de mot de passe
    node.send_password_request()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

