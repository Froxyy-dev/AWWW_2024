import requests
from bs4 import BeautifulSoup
from googlesearch import search
from mdutils import MdUtils

page_url = 'https://www.aiplusinfo.com/blog/top-20-machine-learning-algorithms-explained/'
page = requests.get(page_url)

soup = BeautifulSoup(page.content, 'html.parser')

main_page_file = MdUtils(file_name='main_page')

second_header = soup.find('h2')
introduction = second_header.find_next_sibling('p').text +'\n'+ second_header.find_next_sibling('p').find_next_sibling('p').text
print(introduction)
print()

main_page_file.new_header(level=1, title='Machine Learning Algorithms')
main_page_file.new_header(level=2, title='Introduction')
main_page_file.new_paragraph(text=introduction)

main_page_file.new_header(level=2, title='List of algorithms')
list_page_link = main_page_file.new_inline_link(link='list_page.md', text='Here is a list of ML algos.')
main_page_file.new_paragraph(text=list_page_link)

main_page_file.create_md_file()

ml_algorithms = []
for link in soup.findAll('a'):
    if link.get_attribute_list('data-level')[0] == '3':
        ml_algorithms.append(link.text)

headers = soup.find_all('h3')

algorithm_descriptions = {}
algorithm_formal_description = {}

for ml_algorithm in ml_algorithms:
    header_id = 'h-' + ml_algorithm.replace(' ', '-').lower()

    for header in headers:
        if header.text == ml_algorithm:
            ml_paragraph = header.find_next_sibling('p')
            algorithm_descriptions[ml_algorithm] = ml_paragraph.text

for algorithm_description in algorithm_descriptions.keys():
    print(algorithm_description)
    print(algorithm_descriptions[algorithm_description])
    print()

list_page_file = MdUtils(file_name='list_page')
list_page_file.new_header(level=1, title='List of Machine Learning Algorithms')
list_page_file.new_header(level=2, title='List of algorithms')

for algorithm in ml_algorithms:
    algorithm_id = algorithm.replace(' ', '_').lower()
    algorithm_page_link = main_page_file.new_inline_link(link=f'{algorithm_id}.md', text='Link for wikipedia description')
    list_page_file.new_header(level=3, title=f"{algorithm} {algorithm_page_link}")
    list_page_file.new_paragraph(text=f"{algorithm_descriptions[algorithm]}\n")

list_page_file.create_md_file()


for ml_algorithm in ml_algorithms:
    search_prompt = ml_algorithm + 'Wikipedia algorithm'
    for url in search(search_prompt, stop=1):
        print(url)
        wiki_page = requests.get(url)
        wiki_soup = BeautifulSoup(wiki_page.content, 'html.parser')

        main_introduction = wiki_soup.find('div', class_='shortdescription nomobile noexcerpt noprint searchaux')
        paragraph = main_introduction.find_next_sibling('p')

        print(paragraph.text)
