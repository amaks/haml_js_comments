import sublime
import sublime_plugin

# cmd + shift + /(forward_slash)

class HamlJsCommentsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = self.view.sel()[0]

    if not region.empty():
      new_region = self.toggle_area_comments(region)
      self.view.replace(edit, region, new_region)
    else:
      line       = self.view.line(region)
      new_region = self.toogle_line_comments(region, line)
      self.view.replace(edit, line, new_region)

  def toggle_area_comments(self, region):
    selected_area = self.view.substr(region)
    if '// ' in selected_area:
      new_region = self.remove_comments(selected_area)
    else:
      new_region = self.comment_area(selected_area)

    return new_region

  def toogle_line_comments(self, region, line):
    selected_area = self.view.substr(line)
    if '// ' in selected_area:
      new_region = self.remove_comments(selected_area)
    else:
      new_region = self.comment_line(line, selected_area)

    return new_region

  def remove_comments(self, selected_area):
    return selected_area.replace('// ', '')

  def comment_area(self, selected_area):
    new_region      = ''
    selected_region = selected_area.split('\n')

    for line in selected_region:
      if len(line) > 0:
        spaces_number   = len(line) - len(line.lstrip(' '))
        spaces          = [' ' for x in range(spaces_number)]
        new_region += ''.join(spaces) + '// ' + line.lstrip() + '\n'

    return new_region

  def comment_line(self, line, selected_area):
    startrow, startcol = self.view.rowcol(line.begin())
    spaces_number      = len(selected_area) - len(selected_area.lstrip(' '))
    spaces             = [' ' for x in range(spaces_number)]
    return ''.join(spaces) + '// ' + selected_area.replace(' ', '')