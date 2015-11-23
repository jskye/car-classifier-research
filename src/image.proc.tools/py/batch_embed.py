from PIL import Image
import glob

# img = Image.open('test.png', 'r')
# img_w, img_h = img.size
# background = Image.new('RGBA', (200, 200), (255, 255, 255, 255))
# bg_w, bg_h = background.size
# offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
# background.paste(img, offset)
# background.save('out.png')


files=glob.glob("*.jpg")
for file in files:
	f=open(file)
	filename=f.name
	image = Image.open(file)
	img_w, img_h = image.size
	background=Image.new('RGBA',(110, 110),(255, 255, 255, 255))
	bg_w, bg_h=background.size
	offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
	background.paste(image, offset)
	background.save('embedded.'+filename + '.jpg', 'JPEG', quality=100)
	f.close()
