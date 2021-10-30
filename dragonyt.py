
from pathlib import Path
from pytube import YouTube
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk

class dragonytapp(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.geometry('300x230')
		self.resizable(False, False)
		self.title("DragonYT")
		imgfile = PhotoImage('dragonicon.png')
		self.iconphoto

		#self.selectionlabel = tk.Label(self, text='File Type', background="#a01010")
		#self.selection = tk.Listbox(self, justify="center", height=2, width=5)
		#self.selection.insert(1, "mp4")
		#self.selection.insert(2, "mp3")
		self.lelabel = tk.Label(self, text='Link Entry', background="#a01010")
		self.linkentry = tk.Entry(self, width=30)

		self.button = tk.Button(self, text="Download Video", command=self.on_button, background="#a01010")
		self.dirlabe = tk.Label(self, text="Download Directory", background="#a01010")
		
		self.direntry = tk.Entry(self, width=30)
		self.direntry.insert(END, str(Path.home())+'/Downloads')
		self.upbutton = tk.Button(self, text='Select Download Directory', command=self.UploadAction)

		#self.selectionlabel.pack()
		#self.selection.pack()
		self.lelabel.pack()
		self.linkentry.pack()
		self.button.pack()
		self.dirlabe.pack()
		self.direntry.pack()
		self.upbutton.pack()

	def on_button(self):
		#print(self.importtype)
		#video = YouTube(self.linkentry.get())
		#print(self.selection.curselection())
		#if self.selection.curselection() == 0:
		#	video_streams = video.streams.filter(file_extension=self.importtype).get_by_itag(22)
		#	video_streams.download(self.direntry.get())
		#elif self.selection.curselection() == 1:
		#	video_streams = video.streams.filter(file_extension=self.importtype).get_by_itag(22)
		#	video_streams.download(self.direntry.get())
		video = YouTube(self.linkentry.get())
		video_streams = video.streams.filter(file_extension=self.importtype).get_by_itag(22)
		video_streams.download(self.direntry.get())
	
	def UploadAction(self):
		self.filename = str(filedialog.askdirectory())
		self.direntry.delete(1, END)
		self.direntry.insert(END, self.filename[1:])

app = dragonytapp()
app['background'] = '#a01010'
app.mainloop()