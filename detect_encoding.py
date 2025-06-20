import chardet

file_name = "input.txt"

# with open(file_name, "rb") as f:
#     rawdata = f.read()

# print(
#     chardet.detect(rawdata)
# )

# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}


"change encoding"
change_filename = "output.txt"
with open(file_name, "r", encoding="EUC-KR") as f:
    content = f.read()
# utf-8, utf-8-sig, euc-kr, ascii, latin1

with open(change_filename, "w", encoding="utf-8") as f:
    f.write(content)