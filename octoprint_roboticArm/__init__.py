#python3
import octoprint.plugin

class RoboticArm(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin):
	def on_after_startup(self):
		self._logger.info("Hello World!")
    

__plugin_implementation__ = RoboticArm()


