from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, {"bg": "white", "width": self.width, "height": self.height})
        self.canvas.pack(fill=BOTH, expand=True)
        self.__isRunning = True


    # Redraw the window after each iteration
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # Manage the state of the window (running or not)
    def wait_for_close(self):
        while self.__isRunning:
            self.redraw()

    
    # Set the window's state to False
    def close(self):
        self.__isRunning = False
        self.__root.quit()





    