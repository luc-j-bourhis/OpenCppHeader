import sublime, sublime_plugin
import re

class OpenCppHeaderCommand(sublime_plugin.TextCommand):

  include_pat = re.compile(
    r'^ \# \s* include \s* (?: (") | <) ([^">]+) (?(1) " | >)', re.X)

  def run(self, edit):
    view = self.view
    window = view.window()
    li = view.substr(view.line(view.sel()[0].b))
    m = self.include_pat.search(li)
    if m is not None:
      window.run_command("show_overlay",
                         {"overlay": "goto", "text": "%s" % m.group(2)})
    else:
      sublime.status_message('* Error: Not an #include *')

  def description(self):
    return ("If the cursor is inside a line featuring an #include, "
            "display a list of matching header to let the other open one "
            "of them")
