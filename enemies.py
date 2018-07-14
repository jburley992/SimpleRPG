import NPC
import HelperFunctions as HF

spider = NPC.Enemy("sprites/spider",5,20)
spider.rect.centerx = HF.WINDOWWIDTH/3
spider.rect.centery = HF.WINDOWHEIGHT/1.33

spider2 = NPC.Enemy("sprites/spider",5,20)
spider2.rect.centerx = HF.WINDOWWIDTH/2.5
spider2.rect.centery = HF.WINDOWHEIGHT/1.67