import urllib2

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from sys import argv

def post(targetImage, targetHost = "http://68.149.110.188/images/upload_image.php" ):
	# Register the streaming http handlers with urllib2
	register_openers()

	# Start the multipart/form-data encoding of the file "DSC0001.jpg"
	# "image1" is the name of the parameter, which is normally set
	# via the "name" parameter of the HTML <input> tag.

	# headers contains the necessary Content-Type and Content-Length
	# datagen is a generator object that yields the encoded parameters
	datagen, headers = multipart_encode({"image": open(targetImage, "rb")})

	# Create the Request object
	request = urllib2.Request(targetHost, datagen, headers)
	# Actually do the request, and get the response
	ans = urllib2.urlopen(request).read()
	if targetHost.count('68.149.110.188') == 0:
		print(ans)

if __name__ == '__main__':
	if len(argv) > 2:
		post( argv[1], argv[2] )
	else:
		post( argv[1] )
