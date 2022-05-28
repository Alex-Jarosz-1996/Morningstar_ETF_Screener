from tkinter import *
from etf import WebScraper
from pandastable import Table

class App(Frame):
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            geometry = '1080x720'
            title = "Morningstar ETF Screener"
            self.main.geometry(geometry)
            self.main.title(title)
            frame = Frame(self.main)
            frame.pack(fill=BOTH, expand=1)
            df = WebScraper.createDF()
            self.table = pt = Table(frame, dataframe=df,
                                    showtoolbar=False, showstatusbar=False,
                                    maxcellwidth=2000)
            pt.show()
            return

app = App()
#launch the app
app.mainloop()