import re
import sys

def markdown_to_html(file):
    with open(file, 'r') as f:
        html_text = f.read()


    ## Lists
    exp_lista = r'((?:^\d+\.\s+.+(?:\n|$))+)'

    def found_list(match):
        itens = match.group(0).strip().split('\n')
        list_html = '<ol>\n'
        for item in itens:
            item_content = re.sub(r'^\d+\.\s+', '', item)
            list_html += f"<li>{item_content}</li>\n"
        list_html += "</ol>"
        return list_html
    
    html_text = re.sub(exp_lista, found_list, html_text, flags=re.MULTILINE)


    ## Headers
    html_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_text, flags=re.MULTILINE)
    html_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_text, flags=re.MULTILINE)
    html_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_text, flags=re.MULTILINE)

    ## Bold Text
    html_text = re.sub(r'\*{2}(.+?)\*{2}', r'<b>\1</b>', html_text) # '?' torna a pesquisa non-greedy

    ## Italic Text
    html_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', html_text)

    ## Image
    html_text = re.sub(r'\!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1" style="width:512px;height:341.5px;"/>', html_text, flags=re.MULTILINE)

    ## Link
    html_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html_text)

    ## New Line
    html_text = re.sub(r'\ {2}', "<br>", html_text, flags=re.MULTILINE)


    html_filename = file.replace(".md", ".html")
    with open(html_filename, 'w') as f:
        f.write(html_text)






def main():
    filename = sys.argv[1]

    try:
        markdown_to_html(filename)
    except FileNotFoundError:
        print("Erro ao encontrar o arquivo")

if __name__ == "__main__":
    main()