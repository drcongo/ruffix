import sublime_plugin
import subprocess


def is_python(view):
    return view.match_selector(0, "source.python")


class RuffixCommand(sublime_plugin.TextCommand):

    def is_enabled(self):
        return is_python(self.view)

    is_visible = is_enabled

    def run(self, edit):
        cmd = ['ruff', '--fix', self.view.file_name()]
        subprocess.Popen(cmd)
