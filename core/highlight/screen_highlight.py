from tkinter import *

from core.highlight.highlight_circle import HighlightCircle
from core.highlight.highlight_rectangle import HighlightRectangle


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

        canvas = Canvas(self.root, width=s_width, height=s_height, borderwidth=0, highlightthickness=0, bg="black")
        canvas.grid()

        Canvas.draw_circle = _draw_circle
        Canvas.draw_rectangle = _draw_rectangle

        self.root.wm_attributes("-transparentcolor", "black")
        # self.root.attributes('-alpha', 0.9)

        self.canvas = canvas
