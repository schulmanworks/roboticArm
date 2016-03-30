#python
from __future__ import absolute_import


import octoprint.plugin

class RoboticArm(octoprint.plugin.StartupPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Hello World!")
    def get_assets(self):
    	return dict(
			js=["js/roboticArm_viewmodel.js"]
		)

__plugin_implementation__ = RoboticArm()


