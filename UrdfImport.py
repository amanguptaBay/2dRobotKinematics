import numpy as np
from roboticstoolbox.robot.ERobot import ERobot
from math import pi

class UrdfImport(ERobot):

    def __init__(self, filePath: str):

        links, name, urdf_string, urdf_filepath = self.URDF_read(
            filePath
        )

        super().__init__(
            links,
            name=name,
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.manufacturer = "File Import"

        # zero angles, upper arm pointing up, lower arm straight ahead
        self.addconfiguration("qz", np.array([0, 0, 0, 0]))

        # reference pose robot pointing upwards
        self.addconfiguration("up", np.array([0.0000, 0.0000, 1.5707, 0.0000]))