from split import SplitPDF

def main():
    file_name = 'old.pdf'
    file_path = 'input/' + file_name

    split = SplitPDF(file_name, file_path, 4)

    split.writeFile()

if __name__ == '__main__':
    main()