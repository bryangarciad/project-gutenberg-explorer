from json import dumps

from app.repositories.user_book_repository import UserBookRepository
from app.util.http_util import throw_book_not_found, ok, generic_error
from fastapi import Response, Request, HTTPException, status
from app.models.constants import GUTENBERG_BASE_URL, GUTENBERG_BOOK_ID_PATH, GUTENBERG_BOOK_METADATA_PATH
import requests
from bs4 import BeautifulSoup


class BookController:
    def __init__(self, user_book_repository: UserBookRepository):
        self.__user_book_repository = UserBookRepository

    def get_book_meta(self, book_id: str, request: Request):
        url = f"{GUTENBERG_BASE_URL}/{GUTENBERG_BOOK_METADATA_PATH}/{book_id}"
        response = requests.get(url, timeout=10000)

        if response.status_code == 200:
            data_dict = {}
            document = BeautifulSoup(response.content, "html.parser")
            table = document.find('table', class_='bibrec')
            image_tag = document.find('img', class_='cover-art')
            image_url = image_tag['src'] if image_tag else None

            if image_url: data_dict.image_url = image_url

            for row in table.find_all('tr'):
                th = row.find('th')
                td = row.find('td')
                if th and td:
                    data_dict[th.text.strip()] = td.text.strip()

            return {"data": dumps(data_dict)}
        elif response.status_code == 404:
            return throw_book_not_found
        else:
            return generic_error()


    def get_reading_list(self, request: Request):
        pass

    def get_book_text(self, book_id: str):
        pass
