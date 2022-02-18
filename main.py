import os
import shutil


print("Укажите путь до папки с логами: ")
path = input()
count = 0
main_path = os.path.dirname(os.path.abspath(__file__))
for f in os.listdir(path):
	if os.path.isdir(os.path.join(path, f)):
		count += 1
try:
	os.mkdir("cookies")
except:
	pass
print(f"Загружено {count} логов. Нажмите ENTER чтобы продолжить")
input()
print("Достаем куки...")
cookie = 0
logs = 0
for f in os.listdir(path):
	if os.path.isdir(os.path.join(path, f)):
		pathcook = path + "/" + f + "/Cookies"
		try:
			for c in os.listdir(pathcook):
				if os.path.isfile(os.path.join(pathcook, c)):
					cookie += 1
					pcook = pathcook + "/" + c
					copyto = main_path + f"/cookies/Cookie {cookie}.txt"
					print(f"Cookie {cookie}")
					shutil.copyfile(pcook, copyto)
			print(f"Лог {f} обработан")
			logs += 1
		except:
			print("Папка cookies не найдена")

print(f"Добавлено {cookie} куков")
print(f"{logs} логов обработано")
input()