sublime-phinx
===============

Sublime Text plugin for Phinx commands

The plugin allows basic access to the phinx library via the sublime command pallete, or user defined shortcuts.

Options Available:
- help (phinx --help)
- status (phinx status -e environment)
- create (phinx create MigrationName)
- migrate (phinx migrate -e environment)
- rollback (phinx rollback -e environment)

INSTALLATION
Create a /Phinx/ folder inside your /Sublime Text 3/Packages/ folder and place all the containing files inside of it. 

Just press Cmd + Shift + P for the dropdown command list, and search for Artisan, and pick your command :D

Once copied, run Cmd/Ctrl + Shift + P search for Phinx and the commands will display for you.

NOTE: At current, the plugin assumes that "phinx" is available globally via your PATH

This is a community plugin, and not directly associated to Phinx or Rob Morgan, but we would like to thank him for the software he's provided!

Owen
owen@selesti.com
www.selesti.com