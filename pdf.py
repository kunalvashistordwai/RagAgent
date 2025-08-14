import os
from llama_index.core import StorageContext,VectorStoreIndex, SimpleDirectoryReader, load_index_from_storage
from llama_index.readers.file import (
    PDFReader
)

def getindex(data, index_name):
    index = None
    if not os.path.exists(index_name):
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=index_name)
        index = load_index_from_storage(storage_context)

    return index


pdf_path = os.path.join('data', 'Metadata.pdf')
metadata_pdf = PDFReader().load_data(file=pdf_path)
metadata_index = getindex(metadata_pdf, 'metadata_index')

metadata_engine = metadata_index.as_query_engine(
    similarity_top_k=3,
    response_mode="tree_summarize",
    verbose=True,
)