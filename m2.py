import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

def speech():
    try:
        print("A moment of silence, please...")
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Analysing what you said...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                #bvalue = unicode(value,"utf-8")
                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes: 
                    print("{}".format(value).encode("utf-8"))
                    return("{}".format(value).encode("utf-8"))
                else:
                    print(u"You said {}".format(value))
                    return(u"You said {}".format(value))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")#checks for unknown values
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results; {0}".format(e))
    except KeyboardInterrupt:
        pass

def get_words(text):
    return text.split()

    # MAIN e
text = str(speech())
words = get_words(text)
len1 = len(words)
x = []
for i in range (len1) :
    if words[i] == 'is' :
        x.append(words[i-1])
        x.append('=')
    elif words[i].lower() == 'print' or words[i] == 'display' :
        x.append('print(')
        x.append(words[i+1])
        x.append(')')
    elif words[i].lower() == 'plus' or words[i] == '+' :
        x.append(words[i-1])
        x.append('+')
        x.append(words[i+1])
    elif words[i] == 'minus' or words[i] == '-' :
        x.append(words[i-1])
        x.append('-')
        x.append(words[i+1])
    elif words[i] == 'multiplied' :
        x.append(words[i-1])
        x.append('*')
        x.append(words[i+1])
    elif words[i] == 'divided' :
        x.append(words[i-1])
        x.appbend('/')
        x.append(words[i+1])
    elif words[i] == 'raised' :
        x.append(words[i-1])
        x.append('**')  
        x.append(words[i+1])
    elif words[i].lower() == 'input' :
        x.append(words[i+1])
        x.append('=')
        x.append('int(input())')
    elif words[i].lower() == 'next' :
        x.append('\n')
    elif words[i].lower() == 'stop' :
        break   

        
len2=len(x)
s=''
for i in range(len2):
    s= s + x[i]
print("\n")
print('The Code for what you said is:')
print('\n')
print(s)
print('\n')
#import os
#f=open("speech.py","w")
#f.write(s)
#f.close()
#exec(open("speech.py").read())
