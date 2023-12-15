import deepl
import re
import sys
from fpdf import FPDF
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

input_text = sys.argv[1]
out_filename = sys.argv[2]
auth_key = "<your deepl api key>"
traslator = deepl.Translator(auth_key)
output_directory = '.'

original = ''
translated = ''
with open(input_text, 'r') as f:
    original = f.read()

original_sentences = sent_tokenize(original)

pdf = FPDF()
pdf.add_font("NotoSansKR", "", "NotoSansKR-Regular.ttf", uni=True)
pdf.set_font("NotoSansKR", size=10)
pdf.add_page()

result_text = ''
for ori_sen in original_sentences:
    if ori_sen.strip():
        translated = str(traslator.translate_text(ori_sen, target_lang="KO"))
        result_text += ori_sen
        result_text += '\n'
        result_text += translated 
        result_text += '\n'

with open('temp_result.txt', 'w', encoding='utf-8') as f:
    f.write(result_text)

pdf.multi_cell(0,8,result_text)
pdf.output(f'{output_directory}/{out_filename}')
