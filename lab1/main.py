import requests
import re
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from mdutils import MdUtils

PAGE_URL = 'https://www.aiplusinfo.com/blog/top-20-machine-learning-algorithms-explained/'
BOUND = 10


def generate_main_page(soup):
    main_page_md = MdUtils(file_name='main_page')
    main_page_md.new_header(level=1, title='Machine Learning Algorithms')

    h2_header = soup.find('h2')
    first_paragraph = h2_header.find_next_sibling('p')
    second_paragraph = h2_header.find_next_sibling('p').find_next_sibling('p')

    introduction_text = f"{first_paragraph.text}\n{second_paragraph.text}"

    main_page_md.new_header(level=2, title='Introduction')
    main_page_md.new_paragraph(text=introduction_text)

    main_page_md.new_header(level=2, title='List of algorithms')
    list_page_link = main_page_md.new_inline_link(link='list_page.md', text='Here is a list of ML algos.')
    main_page_md.new_paragraph(text=list_page_link)

    main_page_md.create_md_file()


def generate_list_page(soup):
    list_page_file = MdUtils(file_name='list_page')
    list_page_file.new_header(level=1, title='List of Machine Learning Algorithms')
    list_page_file.new_header(level=2, title='List of algorithms')

    ml_algorithms = []
    for link in soup.findAll('a'):
        if link.get_attribute_list('data-level')[0] == '3':
            ml_algorithms.append(link.text)

    headers = soup.find_all('h3')

    algorithm_descriptions = {}

    for ml_algorithm in ml_algorithms:
        for header in headers:
            if header.text == ml_algorithm:
                ml_paragraph = header.find_next_sibling('p')
                algorithm_descriptions[ml_algorithm] = ml_paragraph.text

    for algorithm in ml_algorithms:
        algorithm_id = algorithm.replace(' ', '_').lower().replace('(', '').replace(')', '')
        algorithm_page_link = list_page_file.new_inline_link(link=f'{algorithm_id}.md', text='link to duck response')

        list_page_file.new_header(level=3, title=f"{algorithm} {algorithm_page_link}")
        list_page_file.new_paragraph(text=f"{algorithm_descriptions[algorithm]}\n")

    list_page_file.create_md_file()

    return ml_algorithms, algorithm_descriptions


def generate_algorithm_page(ml_algorithm, algorithm_descriptions):
    cleaned_algorithm = ml_algorithm.replace(' ', '_').lower().replace('(', '').replace(')', '')

    algorithm_page_file = MdUtils(file_name=f"{cleaned_algorithm}")
    algorithm_page_file.new_header(level=1, title=f'{ml_algorithm}')

    algorithm_page_file.new_header(level=2, title='Description')
    algorithm_page_file.new_paragraph(text=f"{algorithm_descriptions[ml_algorithm]}\n")

    algorithm_page_file.new_header(level=2, title='Duck response')

    search_prompt = 'wikipedia ' + ml_algorithm
    search_result = DDGS().text(search_prompt, max_results=1)[0]
    result_link = search_result['href']

    algorithm_page_link = algorithm_page_file.new_inline_link(link=f"{result_link}", text='link to wikipedia')
    algorithm_page_file.new_header(level=3, title=f"{search_result['title']} {algorithm_page_link}")

    wiki_page = requests.get(result_link)
    wiki_soup = BeautifulSoup(wiki_page.content, 'html.parser')
    main_introduction = wiki_soup.find('div', class_='shortdescription nomobile noexcerpt noprint searchaux')

    try:
        count = 1
        paragraph = main_introduction.find_next_sibling('p')

        while len(paragraph.text) < BOUND and count < BOUND:
            paragraph = paragraph.find_next_sibling('p')
            count += 1

        cleaned_text = re.sub(r'\[\d+\]', '', paragraph.text)

        algorithm_page_file.new_header(level=3, title=f"Wikipedia description")
        algorithm_page_file.new_paragraph(text=cleaned_text)
    except ValueError:
        print('An error occurred!')

    image = DDGS().images(
        keywords=search_prompt,
        region="wt-wt",
        safesearch="off",
        max_results=1,
    )[0]

    algorithm_page_file.new_header(level=3, title=f"Wikipedia image")
    algorithm_page_file_image = algorithm_page_file.new_inline_image(text='Image: ', path=image['thumbnail'])
    algorithm_page_file.new_paragraph(text=algorithm_page_file_image)

    algorithm_page_file.create_md_file()


def generate_md_files():
    page = requests.get(PAGE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    generate_main_page(soup)
    ml_algorithms, algorithm_descriptions = generate_list_page(soup)

    for ml_algorithm in ml_algorithms:
        generate_algorithm_page(ml_algorithm, algorithm_descriptions)


if __name__ == "__main__":
    generate_md_files()
