import os
def showresults( queryimg, gtimg, dist):
	output_path = './results.html'
	with open(output_path, 'w') as v_html:
		v_html.write("<img src=\""+os.path.join('data/polyvore_outfits/images', queryimg+'.jpg') + "\">")
		v_html.write("<img src=\""+os.path.join('data/polyvore_outfits/images', gtimg+'.jpg') + "\">")
		for outid, img2, n in dist:
			v_html.write("<img src=\""+os.path.join('data/polyvore_outfits/images', img2+'.jpg') + "\">")

		v_html.write("<br>")


if __name__ == "__main__":
	q = '215683017'
	g = '215687824'
	dist = ([0, '215685929', 0], [0, '215685929', 0], [0, '215685929', 0])
	showresults(q, g, dist)
