import os
from langchain_community.document_loaders import ConfluenceLoader

token = os.getenv("CONFLUENCE_TOKEN", " ")
space_key = os.getenv("CONFLUENCE_SPACE_KEY", " ")

loader = ConfluenceLoader(
    url="http://confluence.localhost",
    token=token,
    space_key=space_key,
    include_attachments=True,
    limit=50,
    max_pages=50,
)
documents = loader.load()