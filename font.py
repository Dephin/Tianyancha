# coding: utf-8

from fontTools.ttLib import TTFont


fonts = TTFont('fonts.woff')

temp = [i for i in range(0, 10)]
dict = []
for glyph_id in range(2, 11):
	glyph_name = fonts.getGlyphName(glyph_id)
	dict.append([glyph_id, int(glyph_name)])
	temp.remove(int(glyph_name))

x = temp[0]

for d in dict:
	if d[0] >= x:
		d[0] += 1

dict.append([x, x])


print(dict)

# 
# print(uni_list)
# onlineFonts.saveXML('test.xml')