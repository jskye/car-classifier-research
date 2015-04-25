from PIL import Image
import glob, os

# ==============================
target_size = 300, 175
doLog = False
# ==============================

def log(m):
	if doLog:
		print m

def ratio(size):
	return float(size[0]) / float(size[1])

def scaleImg(img, factor):
	return img.resize((int(img.size[0]*factor), int(img.size[1]*factor)), Image.ANTIALIAS)



files = [os.path.join(root, name)
				for root, dirs, files in os.walk(os.getcwd())
				for name in files
				if name.endswith((".jpg"))]
target_ratio = ratio(target_size)

# files = [os.path.join(os.getcwd(), "abel_tasman.jpg")]

for infile in files:
	im = Image.open(infile)
	source_size = im.size
	source_ratio = ratio(source_size)
	log("source ratio: "+str(source_ratio)+", target ratio: "+str(target_ratio))
	if source_ratio>target_ratio:
		log("source is too wide")
		factor = float(target_size[1]) / float(source_size[1])
		im = scaleImg(im, factor)
		crop_amount = im.size[0]-target_size[0]
		im = im.crop((
			crop_amount/2,
			0,
			target_size[0]+crop_amount/2,
			target_size[1]))
	else:
		log("source is too narrow")
		factor = float(target_size[0]) / float(source_size[0])
		im = scaleImg(im, factor)
		crop_amount = im.size[1]-target_size[1]
		im = im.crop((
			0,
			crop_amount/2,
			target_size[0],
			target_size[1]+crop_amount/2))
	f = os.path.split(infile)
	filename = os.path.join(f[0], "thumb_"+f[1])
	log("saving to "+filename)
	im.save(filename, "JPEG")
