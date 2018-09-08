class UIBasic:
	def __init__(self):
		return True
	def Frame(self, x, y, x2, y2,BG):
		pygame.draw.rect(display,BG,[[x,y,x2,y2],0)
class UIText:
	def __init__(self):
		self.color = (255,0,255)
		self.text = 'If you are seeing this than im too lazy to simply call SetText()!'
		pygame.font.init()
		self.font = pygame.font.SysFont('Comic Sans MS', 10)
		return True
	def GetFont(self,font,fontSize,color):
		self.font = pygame.font.SysFont(font, fontSize)
		self.color = color
	def SetText(self,text):
		self.text = text
	def PushText(self,x,y):
		TextSurface = myfont.render(self.text, False, self.color)
		display.blit(TextSurface,(x,y))
class GamePlay:
	def __init__(self):
		return True
	def DialogMenu_Talk(self, text, name):
		
