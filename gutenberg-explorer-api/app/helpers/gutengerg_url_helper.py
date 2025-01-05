from app.models.constants import \
    GUTENBERG_BASE_URL, GUTENBERG_BOOK_ID_PATH, GUTENBERG_BOOK_METADATA_PATH

def create_gutenberg_content_url(book_id: str) -> str:
    '''
    Helper function to create content url for book in gutenberg
    '''
    return f"{GUTENBERG_BASE_URL}/{GUTENBERG_BOOK_ID_PATH}/{book_id}/{book_id}-0.txt"

def create_gutenberg_metadata_url(book_id: str) -> str:
    '''
    Helper function to create metadata url for book in gutenberg
    '''
    return f"{GUTENBERG_BASE_URL}/{GUTENBERG_BOOK_METADATA_PATH}/{book_id}"
