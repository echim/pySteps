from tkinter import *

from core.highlight.highlight_circle import HighlightCircle
from core.highlight.highlight_rectangle import HighlightRectangle
from core.enums.os_platform import OsPlatform
from core.helpers.os_helpers import get_os_platform


def _draw_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


def _draw_rectangle(self, x, y, w, h, **kwargs):
    rectangle = self.create_rectangle(0, 0, w, h, **kwargs)
    self.move(rectangle, x, y)


class ScreenHighlight:

    def draw_circle(self, a_circle: HighlightCircle):
        return self.canvas.draw_circle(a_circle.center.x,
                                       a_circle.center.y,
                                       a_circle.radius,
                                       outline=a_circle.color.value,
                                       width=a_circle.thickness)

    def draw_rectangle(self, a_rectangle: HighlightRectangle):
        return self.canvas.draw_rectangle(a_rectangle.start_point.x,
                                          a_rectangle.start_point.y,
                                          a_rectangle.width,
                                          a_rectangle.height,
                                          outline=a_rectangle.color.value,
                                          width=a_rectangle.thickness)

    def quit(self):
        self.root.quit()
        self.root.destroy()

    def render(self, for_ms):
        self.root.after(for_ms, self.quit)
        self.root.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(1)

        s_width = self.root.winfo_screenwidth()
        s_height = self.root.winfo_screenheight()

        canvas = Canvas(self.root, width=s_width, height=s_height, borderwidth=0, highlightthickness=0, bg="white")
        canvas.grid()

        Canvas.draw_circle = _draw_circle
        Canvas.draw_rectangle = _draw_rectangle

        platform: OsPlatform = get_os_platform()

        if platform is OsPlatform.WINDOWS:
            self.root.wm_attributes("-transparentcolor", "white")

        if platform is OsPlatform.LINUX:
            self.root.wait_visibility(self.root)
            self.root.attributes('-alpha', 0.9)

        self.canvas = canvas
