from chardet import detect
import codecs
import sys

def detect_file_encoding(file_path):
    f = open(file_path, 'rb')
    data = f.read(1024)
    f.close()
    predict = detect(data)
    return predict['encoding']

def convert_file_encoding(source_file_path, target_file_path, target_encoding, chunk_size=1024*1024):
    source_file_encoding = detect_file_encoding(source_file_path)
    if (source_file_encoding != target_encoding):
        f = open(source_file_path, 'rb')
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            content = data.decode(source_file_encoding, 'ignore')
            codecs.open(target_file_path, 'a+', encoding=target_encoding).write(content)
        f.close()


if __name__ == '__main__':
    if (4 == len(sys.argv)):
        source_file_path = sys.argv[1]
        target_file_path = sys.argv[2]
        charset = sys.argv[3]
        convert_file_encoding(source_file_path, target_file_path, charset)
        print('Charset convert success !')
    else:
        print('''Usage: Python filetranscode.py source_file_path target_file_path charset
Example: Python filetranscode.py c:/source.txt c:/target.txt utf-8''')