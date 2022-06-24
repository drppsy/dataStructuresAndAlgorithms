import os


many_texts_dir = './docs/many_texts'

content = []

for file in os.listdir(many_texts_dir):
    file_path = f"{many_texts_dir}/{file}"
    if os.path.isfile(file_path) and file.endswith('.txt'):
        with open(file_path) as fp:
            text = fp.read()
            content.append(text)

final_content = '\n'.join(content)

with open('./docs/many_texts.txt', 'w') as fp:
    fp.write(final_content)