# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from Gif import *
import speech_recognition as sr

pathsBad = ['Imagenes/bad00.gif','Imagenes/bad01.gif','Imagenes/bad02.gif','Imagenes/bad03.gif','Imagenes/bad04.gif','Imagenes/bad05.gif','Imagenes/bad06.gif','Imagenes/bad07.gif','Imagenes/bad08.gif','Imagenes/bad09.gif','Imagenes/bad10.gif','Imagenes/bad11.gif','Imagenes/bad12.gif','Imagenes/bad13.gif','Imagenes/bad14.gif']
pathsHello = ['Imagenes/Hello00.gif','Imagenes/Hello01.gif','Imagenes/Hello02.gif','Imagenes/Hello03.gif','Imagenes/Hello04.gif','Imagenes/Hello05.gif','Imagenes/Hello06.gif','Imagenes/Hello07.gif','Imagenes/Hello08.gif','Imagenes/Hello09.gif','Imagenes/Hello10.gif','Imagenes/Hello11.gif','Imagenes/Hello12.gif','Imagenes/Hello13.gif','Imagenes/Hello14.gif']
pathsGoodMorning = ['Imagenes/good morning00.gif','Imagenes/good morning01.gif','Imagenes/good morning02.gif','Imagenes/good morning03.gif','Imagenes/good morning04.gif','Imagenes/good morning05.gif','Imagenes/good morning06.gif','Imagenes/good morning07.gif','Imagenes/good morning08.gif','Imagenes/good morning09.gif','Imagenes/good morning10.gif','Imagenes/good morning11.gif','Imagenes/good morning12.gif','Imagenes/good morning13.gif','Imagenes/good morning14.gif']
pathsGoodAfternoon = ['Imagenes/good afternoon00.gif','Imagenes/good afternoon01.gif','Imagenes/good afternoon02.gif','Imagenes/good afternoon03.gif','Imagenes/good afternoon04.gif','Imagenes/good afternoon05.gif','Imagenes/good afternoon06.gif','Imagenes/good afternoon07.gif','Imagenes/good afternoon08.gif','Imagenes/good afternoon09.gif','Imagenes/good afternoon10.gif','Imagenes/good afternoon11.gif','Imagenes/good afternoon12.gif','Imagenes/good afternoon13.gif','Imagenes/good afternoon14.gif']
pathsGoodEvening = ['Imagenes/good evening00.gif','Imagenes/good evening01.gif','Imagenes/good evening02.gif','Imagenes/good evening03.gif','Imagenes/good evening04.gif','Imagenes/good evening05.gif','Imagenes/good evening06.gif','Imagenes/good evening07.gif','Imagenes/good evening08.gif','Imagenes/good evening09.gif','Imagenes/good evening10.gif','Imagenes/good evening11.gif','Imagenes/good evening12.gif','Imagenes/good evening13.gif','Imagenes/good evening14.gif']
pathsGood = ['Imagenes/good00.gif','Imagenes/good01.gif','Imagenes/good02.gif','Imagenes/good03.gif','Imagenes/good04.gif','Imagenes/good05.gif','Imagenes/good06.gif','Imagenes/good07.gif','Imagenes/good08.gif','Imagenes/good09.gif','Imagenes/good10.gif','Imagenes/good11.gif','Imagenes/good12.gif','Imagenes/good13.gif','Imagenes/good14.gif']
pathsIDontLikeIt = ["Imagenes/I don't like it00.gif","Imagenes/I don't like it01.gif","Imagenes/I don't like it02.gif","Imagenes/I don't like it03.gif","Imagenes/I don't like it04.gif","Imagenes/I don't like it05.gif","Imagenes/I don't like it06.gif","Imagenes/I don't like it07.gif","Imagenes/I don't like it08.gif","Imagenes/I don't like it09.gif","Imagenes/I don't like it10.gif","Imagenes/I don't like it11.gif","Imagenes/I don't like it12.gif","Imagenes/I don't like it13.gif","Imagenes/I don't like it14.gif"]
pathsILikeIt = ['Imagenes/I like it00.gif','Imagenes/I like it01.gif','Imagenes/I like it02.gif','Imagenes/I like it03.gif','Imagenes/I like it04.gif','Imagenes/I like it05.gif','Imagenes/I like it06.gif','Imagenes/I like it07.gif','Imagenes/I like it08.gif','Imagenes/I like it09.gif','Imagenes/I like it10.gif','Imagenes/I like it11.gif','Imagenes/I like it12.gif','Imagenes/I like it13.gif','Imagenes/I like it14.gif']
pathsNiceToMeetYou = ['Imagenes/nice to meet you00.gif','Imagenes/nice to meet you01.gif','Imagenes/nice to meet you02.gif','Imagenes/nice to meet you03.gif','Imagenes/nice to meet you04.gif','Imagenes/nice to meet you05.gif','Imagenes/nice to meet you06.gif','Imagenes/nice to meet you07.gif','Imagenes/nice to meet you08.gif','Imagenes/nice to meet you09.gif','Imagenes/nice to meet you10.gif','Imagenes/nice to meet you11.gif','Imagenes/nice to meet you12.gif','Imagenes/nice to meet you13.gif','Imagenes/nice to meet you14.gif']
pathsPlease = ['Imagenes/please00.gif','Imagenes/please01.gif','Imagenes/please02.gif','Imagenes/please03.gif','Imagenes/please04.gif','Imagenes/please05.gif','Imagenes/please06.gif','Imagenes/please07.gif','Imagenes/please08.gif','Imagenes/please09.gif','Imagenes/please10.gif','Imagenes/please11.gif','Imagenes/please12.gif','Imagenes/please13.gif','Imagenes/please14.gif']
pathsThankYou = ['Imagenes/thank you00.gif','Imagenes/thank you01.gif','Imagenes/thank you02.gif','Imagenes/thank you03.gif','Imagenes/thank you04.gif','Imagenes/thank you05.gif','Imagenes/thank you06.gif','Imagenes/thank you07.gif','Imagenes/thank you08.gif','Imagenes/thank you09.gif','Imagenes/thank you10.gif','Imagenes/thank you11.gif','Imagenes/thank you12.gif','Imagenes/thank you13.gif','Imagenes/thank you14.gif']
pathsYouRWelcome = ['Imagenes/your welcome00.gif','Imagenes/your welcome01.gif','Imagenes/your welcome02.gif','Imagenes/your welcome03.gif','Imagenes/your welcome04.gif','Imagenes/your welcome05.gif','Imagenes/your welcome06.gif','Imagenes/your welcome07.gif','Imagenes/your welcome08.gif','Imagenes/your welcome09.gif','Imagenes/your welcome10.gif','Imagenes/your welcome11.gif','Imagenes/your welcome12.gif','Imagenes/your welcome13.gif','Imagenes/your welcome14.gif']

while True:
	# obtain audio from the microphone
	pass
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
	    print("Say something!")
	    audio = r.listen(source)
	# recognize speech using Google Speech Recognition
	try:
	    frase = r.recognize_google(audio)
	    print("You said " + frase)
	    if frase == "hello":
	    	showGif(pathsHello)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "good morning":
	    	showGif(pathsGoodMorning)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "bad":
	    	showGif(pathsBad)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "good afternoon":
	    	showGif(pathsGoodAfternoon)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "good evening":
	    	showGif(pathsGoodEvening)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "good":
	    	showGif(pathsGood)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "please":
	    	showGif(pathsPlease)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "thank you":
	    	showGif(pathsThankYou)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "nice to meet you":
	    	showGif(pathsNiceToMeetYou)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "I like it":
	    	showGif(pathsILikeIt)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "I don't like it":
	    	showGif(pathsIDontLikeIt)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "you're welcome":
	    	showGif(pathsYouRWelcome)
	    	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	    elif frase == "exit":
	    	exit()
	    else:
	    	print("That word or phrase is not in the diccionary\n\nTry with:\nI like it\nHello\nPlease\nThank you\nGood\nGood Afternoon\n\n")
	except sr.UnknownValueError:
	    print("I could not understand what you said")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))



