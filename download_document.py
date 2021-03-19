import os
import time
import json
import codecs
import argparse
import requests
from bs4 import BeautifulSoup


def get_163_content(html_obj):

    content_body = html_obj.find("div", attrs={"class": "post_body"})
    if content_body is None:
        text = ""
    else:
        all_p_block = content_body.find_all("p")
        text = "\n".join([item.text for item in all_p_block])

    title_body = html_obj.find("h1", attrs={"class": "post_title"})
    if title_body is None:
        title = ""
    else:
        title = title_body.text

    return text, title


def get_ithome_content(html_obj):

    content_body = html_obj.find("div", attrs={"class": "post_content", "id": "paragraph"})
    if content_body is None:
        text = ""
    else:
        all_p_block = content_body.find_all("p")
        text = "\n".join([item.text for item in all_p_block])

    title_body = html_obj.find("h1")
    if title_body is None:
        title = ""
    else:
        title = title_body.text

    return text, title


def get_content(input_url):

    text = ''
    title = ''
    try:
        response = requests.get(input_url)

        if response:
            html_obj = BeautifulSoup(response.text, 'lxml')
            if '163.com' in input_url:
                text, title = get_163_content(html_obj)
            elif 'ithome.com' in input_url:
                text, title = get_ithome_content(html_obj)

        time.sleep(30)

    except:
        time.sleep(300)

    return text, title


def main(args):

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    if os.path.exists(args.doc_url_json):
        doc_url_list = json.loads(codecs.open(args.doc_url_json, 'r', 'utf-8').read())
        for doc in doc_url_list:
            url = doc['url']
            doc_id = doc['document_id']

            print(doc_id, url)
            text, title = get_content(url)
            content = {'title': title, 'text': text}

            outfile = codecs.open(os.path.join(args.output_dir, doc_id+'.json'), 'w', 'utf-8')
            outfile.write(json.dumps(content))
            outfile.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc_url_json', '-i', type=str, default='document_url_release.json')
    parser.add_argument('--output_dir', '-o', type=str, default='output')
    args = parser.parse_args()

    main(args)
