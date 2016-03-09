#python3

import octoprint.plugin

    
    
__plugin_name__ = "Robotic Arm"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Robotic Arm Control for Octoprint"
__plugin_implementation__ = RoboticArm()

class RoboticArm(octoprint.plugin.StartupPlugin):
	def on_after_startup(self):
		self._logger.info("Hello World!")
