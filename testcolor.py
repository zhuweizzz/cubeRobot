from colordetect import getfacecolor

filename='screen'

colorlist=getfacecolor(filename)
color=''.join(colorlist)

print(color)
