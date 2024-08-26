import logging,time,re
from colorama import init,Fore,Style
init(autoreset=True)
class ColoredFormatter(logging.Formatter):
	def format(E,record):
		A=record;D=super().format(A)
		if A.levelno==logging.INFO:B=Fore.GREEN;C='Успех ✓'
		elif A.levelno==logging.WARNING:B=Fore.YELLOW;C='Предупреждение ⚠'
		elif A.levelno==logging.ERROR:B=Fore.RED;C='Ошибка 𐄂'
		else:B=Fore.WHITE;C='Лог'
		D=E.highlight_paths(D);F=time.time()-A.created;G=f"[{B}{C}{Style.RESET_ALL} | {F:.2f} секунд] | {D}";return G
	@staticmethod
	def highlight_paths(message):A=re.compile('([A-Za-z]:\\\\(?:[^\\\\/:*?"<>|\\r\\n]+\\\\)*[^\\\\/:*?"<>|\\r\\n]*)|(/(?:[^/ ]*/)*[^/ ]*)');return A.sub(lambda match:Fore.YELLOW+match.group(0)+Style.RESET_ALL,message)
def setuplogger(name):A=logging.getLogger(name);A.setLevel(logging.DEBUG);B=logging.StreamHandler();B.setLevel(logging.DEBUG);C=ColoredFormatter('%(message)s');B.setFormatter(C);A.addHandler(B);return A