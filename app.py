import sys
import requests

def main():
	enaAccessionsFile = open("accessions.txt")
	fileOutput = open("testoutput.txt", "w+")
	fileOutput.write("Nr.\t enaAccession\t publication_count\n\n")
	
	print("processing ...")
	for index, enaAccession in enumerate(enaAccessionsFile):
		url = "https://app.dimensions.ai/discover/publication?search_text=" + enaAccession

		response = requests.get(url)

		pub_document = ''

		if response.status_code == 200:
			lines = str(response.content).split('\\n')
			for i,j in enumerate(lines):
				if 'count' in j:
					pub_document = j.split()[3:25]		
		#print (enaAccession, '::: publications_count', pub_document[21][:len(pub_document[21])-1])
		fileOutput.write(str(index+1) + '\t' + enaAccession.strip()  + '\t' + pub_document[21][:len(pub_document[21])-1] + '\n')
	print("processing finished.")
	enaAccessionsFile.close()
	fileOutput.close()
	
if __name__ == "__main__":
    main()