# -*- encoding: utf-8 -*-
''' tk_animate_GIF_sequence.py
play a sequence of gifs to create an animation effect
the gif sequence was create with PIL_animatedGif_frames.py
note:  Tkinter cannot display animated gifs directly
(dns)
'''

import itertools as it
import tkinter as tk
def showGif(paths):
	def quit():
		root.destroy()
	def animate():
	    """ cycle through """
	    img = next(pictures)
	    label["image"] = img
	    root.after(delay, animate)


	root = tk.Tk()

	label = tk.Label(root)
	label.pack(padx=10, pady=10)

	fname_list = paths
	# store as tk img_objects
	pictures = it.cycle(tk.PhotoImage(file=img_name) for img_name in fname_list)

	# milliseconds
	delay = 75
	root.after(5000,quit)
	animate()

	root.mainloop()
	

	