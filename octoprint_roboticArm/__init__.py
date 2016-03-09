#python
from __future__ import absolute_import

import StepperMotor
import octoprint.plugin

class RoboticArm(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin):
	def on_after_startup(self):
		self._logger.info("Hello World!")
    

__plugin_implementation__ = RoboticArm()


