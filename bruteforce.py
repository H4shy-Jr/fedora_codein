from zipfile import ZipFile

f = ZipFile('my_zip.zip','r')



def check(f,passwd):
	try:
		f.extractall(pwd =passwd)
	except RuntimeError :
		return 1;
	else:
		return 0;

wordlist = ["code","google",'fedora','zip','codein']

for i in wordlist:
	password = bytes(i,'utf-8')
	res = (check(f,password))
	if res == 0:
		print("You got the password,password:",i)
		break
