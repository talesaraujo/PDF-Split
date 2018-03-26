from PyPDF2 import PdfFileReader, PdfFileWriter

class SplitPDF:

    def __init__(self, file_name, file_path, option):
        self.file_name = file_name
        self.file_path = file_path
        self.file = PdfFileReader(self.file_path, 'r')
        self.dimensions = self.scale()
        self.new_file_name = self.file_name[:-4] + '_split.pdf'
        self.option = option

    def scale(self):
        """
        Returns a tuple with the PDF dimensions (coordinates with size of the document).
        """
        page = self.file.getPage(1)
        return page.cropBox.getUpperRight()
    
    def splitInFour(self):
        """ 
        This method gets the page dimensions, find the vertical/horizontal middles
        and for each page, sets the appropiate coordinates. Each page is added to 
        returning object newFile which represents the divided pdf file.
        """
        half_x = (self.dimensions[0])/2
        half_y = (self.dimensions[1])/2

        newFile = PdfFileWriter()

        for n in range(self.file.getNumPages()):

            page1n = self.file.getPage(n)
            page1n.cropBox.setLowerLeft((0, half_y))
            page1n.cropBox.setUpperRight((half_x, self.dimensions[1]))
            newFile.addPage(page1n)

            page2n = self.file.getPage(n)
            page2n.cropBox.setLowerLeft((half_x, half_y))
            page2n.cropBox.setUpperRight((self.dimensions[0], self.dimensions[1]))
            newFile.addPage(page2n)

            page3n = self.file.getPage(n)
            page3n.cropBox.setLowerLeft((0, 0))
            page3n.cropBox.setUpperRight((half_x, half_y))
            newFile.addPage(page3n)

            page4n = self.file.getPage(n)
            page4n.cropBox.setLowerLeft((half_x, 0))
            page4n.cropBox.setUpperRight((self.dimensions[0], half_y))
            newFile.addPage(page4n)

        return newFile

    def writeFile(self):
        if self.option == 4:
            newFile = self.splitInFour()

            path = 'output/' + self.new_file_name
            outstream = open(path, 'wb')

            newFile.write(outstream)
            outstream.close()
            print("PDF successfully splitted.")

        else:
            print("Other split methods not implemented yet. Only 4-split avaliable.")


