from tkinter import *
from mainMenu import *

class MainApplication:
	def __init__(self):
		self.root = Tk()
		self.root.title("Simple Text Editor")
		self.txtEdit = Text(self.root)
		self.txtEdit.pack(expand=True, fill='both')
		self.currentFilePath = ""
		self.mainMenuPanel = MainMenuPanel(self.root, self.txtEdit)

		self.root.mainloop()

mainApp = MainApplication()