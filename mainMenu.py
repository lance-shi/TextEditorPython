from tkinter import *
from tkinter import filedialog

class MainMenuPanel:
	def __init__(self, root, txtEdit):
		self.root = root
		self.txtEdit = txtEdit
		self.mainMenu = Menu()
		self.root.config(menu=self.mainMenu)

		fileMenu = Menu()
		self.mainMenu.add_cascade(label="File", menu=fileMenu)
		fileMenu.add_command(label="New", command=self.onNew)
		fileMenu.add_command(label="Open", command=self.onOpen)
		fileMenu.add_command(label="Save", command=self.onSave)
		fileMenu.add_command(label="Save As...", command=self.onSaveAs)
		fileMenu.add_separator()
		fileMenu.add_command(label="Exit", command=self.root.quit)

	def onNew(self):
		self.txtEdit.delete(1.0, END)
		self.root.title("Simple Text Editor")
		self.currentFilePath = ""

	def onOpen(self):
		filepath = filedialog.askopenfilename(
			filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
		)
		if not filepath:
			return
		self.txtEdit.delete(1.0, END)
		with open(filepath, "r") as inputFile:
			text = inputFile.read()
			self.txtEdit.insert(END, text)
		self.root.title(f"Simple Text Editor - {filepath}")
		self.currentFilePath = filepath
		print(self.currentFilePath)

	def onSave(self):
		print("Hello")
		print(self.currentFilePath)
		if self.currentFilePath != "":
			with open(self.currentFilePath, "w") as outputFile:
				text = self.txtEdit.get(1.0, END)
				outputFile.write(text)
		else:
			onSaveAs()

	def onSaveAs(self):
		filepath = filedialog.asksaveasfilename(
			defaultextension="txt",
			filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
		)
		if not filepath:
			return
		with open(filepath, "w") as outputFile:
			text = self.txtEdit.get(1.0, END)
			outputFile.write(text)
		root.title(f"Simple Text Editor - {filepath}")
		self.currentFilePath = filepath