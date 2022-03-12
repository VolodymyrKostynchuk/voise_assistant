import os 
import random
import speech_recognition 
import webbrowser as wb
#--------------------------------------------------------------
# dict command 
command_dict = {
	'commands': {

		'open_browzer': { # url address in values
			'open google': 'https://www.google.com.ua/', 
			'open youtube': 'https://www.youtube.com/',
			'open telegram': 'https://web.telegram.org/k/',
			'open instagram': 'https://www.instagram.com/',
			},

		'open_program': { # path in the system to shortcuts in values
			'open steam': 'C:\\Program Files (x86)\\Steam\\steam.exe', 
			'open cs go': 'steam://rungameid/730',
			'open sublime': 'C:\\Program Files\\Sublime Text\\sublime_text.exe',
			'open discord': 'D:\\program\\Discord'
			},

		'system_command': { # this is just cmd commands in values
			'end system': 'shutdown -s -t 0',
			'reboot system': 'shutdown -r -t 0',
			'how time': 'time /t',
			},

		'play_music': { # path in the system to forder with music in values
			'play music': 'D:\\music',
			},

		},
	'turn_on': ['hello', 'turn on']
	}
#--------------------------------------------------------------
# functions for iterable
def play_music(forder):
	musics = os.listdir(forder)
	random_music = f'{forder}\\{random.choice(musics)}'
	os.system(random_music)

def open_browzer(url):
	wb.open(url, new=2)

def open_program(path):
	os.startfile(fr'{path}')

def sys_command(command):
	os.system(command)
#--------------------------------------------------------------
# voice processing
def get_command():
	while True:
		try: 
			with speech_recognition.Microphone() as mic:
				sr.adjust_for_ambient_noise(source=mic, duration=0.5)
				audio = sr.listen(source=mic)
				command = sr.recognize_google(audio_data=audio).lower()
			return command
		except speech_recognition.UnknownValueError:
			print("[-] I'm sorry but I couldn't recognize your beautiful voice")
			print('[+] Try again')

def turn_on():
	command = get_command()
	for k, v in command_dict['commands'].items():
		if command in v:
			print(f'[+] {command}')
			return globals()[k](command_dict['commands'][k].get(command))

def main():
	while True:
		on_phrase = get_command()
		if on_phrase in command_dict['turn_on']:
			print("[+] I'm drying you")
			turn_on()
#--------------------------------------------------------------


if __name__ == '__main__':
	sr = speech_recognition.Recognizer()
	sr.pause_threshold = 0.5
	main()