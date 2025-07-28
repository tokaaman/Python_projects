h=int(input("write what you want"))
w=int(input("write what you want"))
c=5
def paint_calc(height, width, cover):
	whole=round((height*width)/cover)
	print("what you have to paint is" whole)
paint_calc(h,w,c)	