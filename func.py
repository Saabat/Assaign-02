import requests
def list_html_list(any_list):
    start = '<!-- wp:list --><ul>'
    for element in any_list:
        start += f'<!-- wp:list-item --><li>{element}</li><!-- /wp:list-item -->'
    end = '</ul><!-- /wp:list -->'
    code = start + end
    return code

def headers(username, password):
    import base64
    credential = f'{username}:{password}'
    token = base64.b64encode(credential.encode())
    code = {'Authorization': f'Basic {token.decode("utf-8")}'}
    return code


def dict_list(dicts):
    start = '<!-- wp:list --><ul>'
    for key, value in dicts.items():
        start += f'<!-- wp:list-item --><li><strong>{key.title()}</strong> : {value}</li><!-- /wp:list-item -->'
    end = '</ul><!-- /wp:list -->'
    code = start + end
    return code


def image_url(src, name):
    first_line = '<!-- wp:image {"align":"center","sizeSlug":"large"} -->'
    second_line = f'<figure class="wp-block-image aligncenter size-large"><img src="{src}" alt="{name}"/><'
    last_line = f'figcaption class="wp-element-caption">{name}</figcaption></figure><!-- /wp:image -->'
    code = f'{first_line}{second_line}{last_line}'
    return code

def wph2(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code

def yt(src):
    code = f'<!-- wp:embed {"url":"{src}","type":"video","providerNameSlug":"youtube","responsive":true,"className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"} --><figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">{src}</div></figure><!-- /wp:embed -->'
    return code

def oai(prompt):
    import os
    from dotenv import load_dotenv
    import openai
    load_dotenv()

    openai.api_key = os.getenv('api_key')

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    data = response.get('choices')[0].get('text').strip()
    code = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
    return code

def slugify(name):
    slug = name.strip().replace(' ','-')
    return slug

# def pixabay_api(text):
#     api_key = '31975017-73de05c5882dc41d86cb4e2c4'
#     query = f'{text}'
#     url = f"https://pixabay.com/api/?key={api_key}&q={query}"
#     r = requests.get(url)
#     api_data = r.json().get('hits')
#     image_url = []
#     for data in api_data:
#        image_url.append('webformatURL')
#     return image_url