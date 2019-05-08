#!/usr/bin/env python
import os
from shutil import copyfile
import sublime
import sublime_plugin


class DuplicateFileCommand(sublime_plugin.WindowCommand):
    @property
    def path(self):
        return sublime.active_window().active_view().file_name()

    def duplicate(self):
        src = sublime.active_window().active_view().file_name()
        if not src:
            return
        filename = "%s copy" % os.path.splitext(os.path.basename(src))[0]
        if os.path.splitext(src)[1]:
            filename = filename + os.path.splitext(src)[1]
        os.path.splitext(os.path.basename(src))
        dst = os.path.join(os.path.dirname(src), filename)
        if not os.path.exists(dst):
            copyfile(src, dst)

    def run(self):
        try:
            self.duplicate()
        except Exception as e:
            msg = "%s\n%s" % (type(e), str(e))
            sublime.error_message(msg)
