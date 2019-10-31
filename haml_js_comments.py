import sublime
import sublime_plugin

# cmd + shift + /(forward_slash)

class HamlJsCommentsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = self.view.sel()[0]

    if not region.empty():
      selected_area = self.view.substr(region)
      if '// ' in selected_area:
        new_region = selected_area.replace('// ', '')
      else:
        new_region      = ''
        selected_region = selected_area.split('\n')

        for line in selected_region:
          if len(line) > 0:
            spaces_number   = len(line) - len(line.lstrip(' '))
            spaces          = [' ' for x in range(spaces_number)]
            new_region += ''.join(spaces) + '// ' + line.lstrip() + '\n'

      self.view.replace(edit, region, new_region)
    else:

      line          = self.view.line(region)
      selected_area = self.view.substr(line)
      if '// ' in selected_area:
        new_region = selected_area.replace('// ', '')
      else:
        startrow, startcol = self.view.rowcol(line.begin())
        spaces_number      = len(selected_area) - len(selected_area.lstrip(' '))
        spaces             = [' ' for x in range(spaces_number)]
        new_region         = ''.join(spaces) + '// ' + selected_area.replace(' ', '')

      self.view.replace(edit, line, new_region)