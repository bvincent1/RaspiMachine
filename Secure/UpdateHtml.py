from sys import argv
import SendMessage
import PostImage

def update( targetFile, outputFile, changeText, placeholder = "$$$" ):
	# get text from target file
	textFile = open( targetFile, 'r' )
	textplain = textFile.read()
	textFile.close()
	
	# replace placeholder with target text
	newtext = textplain.replace( placeholder, changeText)

	# write changes to target file
	fileChanged = open( outputFile, 'w' )
	fileChanged.write( newtext )
	fileChanged.close()

if __name__ == "__main__":
	PostImage.post( argv[3] )
	update( argv[1], argv[2], argv[3] )
	SendMessage.sendMessage( argv[2] )
