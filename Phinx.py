import sublime, sublime_plugin, os
import subprocess

class PhinxMigrateCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Environment:", "development", self.on_done, None, None)

	def on_done(self, environment):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["phinx", "migrate", "-e", environment],
				"shell" : True,
				"working_dir" : folder})

		except ValueError:
			pass

class PhinxRollbackCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Environment:", "development", self.on_done, None, None)

	def on_done(self, environment):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["phinx", "rollback", "-e", environment],
				"shell" : True,
				"working_dir" : folder})

		except ValueError:
			pass

class PhinxHelpCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["phinx", "help"],
			"shell" : True,
			"working_dir" : folder})

class PhinxStatusCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Environment:", "development", self.on_done, None, None)

	def on_done(self, environment):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["phinx", "status", "-e", environment],
				"shell" : True,
				"working_dir" : folder})

		except ValueError:
			pass

class PhinxCreateCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Migration Name (UseCamelCase):", "", self.on_done, None, None)

	def on_done(self, filename):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)

			self.window.run_command("exec", {
				"cmd" : ["phinx", "create", filename],
				"shell" : True,
				"working_dir" : folder})

		except ValueError:
			pass