import os
import textract
import pandas as pd

# full_path = os.path.abspath('img/test2.txt')
# full_path = os.path.abspath('img/test1.png')    # using tesseract module, installed separately
# full_path = os.path.abspath('img/test3.pdf')  # needs a compatible module to read pdf
# full_path = os.path.abspath('img/test4.docx')


def loop_input():
    data_list = []
    imgdir = os.listdir('img')
    for file in imgdir:
        data = {}
        fname = os.fsdecode(file)
        full_path = os.path.abspath('img/' + fname)
        data['filename'] = fname
        if fname.endswith('.pdf'):  # skip PDFs
            continue
        text = textract.process(full_path, encoding='utf_8')
        string = text.decode('utf-8')
        data['content'] = string.split('\r\n')
        data_list.append(data)

    df = pd.DataFrame(data_list)
    print()

    return df


if __name__ == '__main__':
    df = loop_input()
    df.to_csv('output/out.csv', index=False)
