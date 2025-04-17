import os
from dotenv import load_dotenv
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex

def main(url:str)-> None:
  documents= SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
  index= VectorStoreIndex.from_documents(documents=documents)
  query_engine= index.as_query_engine()
  responce = query_engine.query('What is llamiindex')
  print(responce)

if __name__ == '__main__':
  load_dotenv()

  main(url='https://medium.com/@siladityaghosh/understanding-llamaindex-an-in-depth-guide-bad4a751cb63')




