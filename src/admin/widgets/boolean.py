import wtforms

from godmode.widgets.base import BaseWidget


class BooleanWidget(BaseWidget):
    field = wtforms.BooleanField()

    def render_list(self, item):
        value = getattr(item, self.name, None)
        if value:
            return "<i class='icon-ok' style='color: #0c0;'></i>"

        return "<i class='icon-remove' style='color: #c00;'></i>"


class BooleanReverseWidget(BooleanWidget):
    field = wtforms.BooleanField()

    def render_list(self, item):
        value = getattr(item, self.name, None)
        if value:
            return "<i class='icon-ok' style='color: #c00;'></i>"

        return "<i class='icon-remove' style='color: #0c0;'></i>"
