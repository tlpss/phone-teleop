import numpy as np
from teleop import Teleop


def main():
    def callback(pose, message):
        print(f"Pose: {pose}")
        print(f"Message: {message}")

    teleop = Teleop(host="0.0.0.0",port=5000)
    teleop.set_pose(np.eye(4))
    teleop.subscribe(callback)
    teleop.run()


if __name__ == "__main__":
    main()
