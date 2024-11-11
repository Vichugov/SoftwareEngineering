import ollama
import os

dirPath = 'C:\\Users\\Test\\Desktop\\Учёба\\ПрограммнаяИнженерия\\L1\\ГОСТ\\'

for inFileName in os.listdir(dirPath):
	with open(dirPath + inFileName, "r", encoding='ANSI') as inFile:

		content = inFile.read()

		print (content) # !!!

		question = "Проанализируй текст и напиши по нему краткую инструкцию по проектированию и разработке программного обеспечения: " + content
		response = ollama.chat(model='qwen2.5:7b', messages=[{'role': 'user', 'content': question,},])
		
		print(response['message']['content']) # !!!

		with open(dirPath + "Answer.md", "a", encoding='ANSI') as outFile:
			outFile.write('\n' + response['message']['content'])
			print(inFileName + " done.")