# 🦜🔗 **LangChain Document Loading**

## 📖 **Overview**

This section of the project focuses on **document loading** as part of a Retrieval-Augmented Generation (RAG) pipeline using LangChain. Document loading is the first step in building an information retrieval system that enables a Language Model (LLM) to retrieve relevant content for answering queries.

The image below provides an **overview of the process**, showing how documents are loaded, split into smaller chunks, stored in a vector database, and later retrieved when needed.

![Document Loading Overview](images/document_loading.png)

In this section, we will explore various **document loading techniques**, including:

- **Loading PDFs** using `PyPDFLoader`
- **Extracting transcriptions from YouTube videos** using `YoutubeAudioLoader` and `OpenAIWhisperParser`
- **Scraping content from web pages** using `WebBaseLoader`

These techniques will allow us to preprocess data efficiently before storing it in a vector database for later retrieval.

## 📂 **Files**

1. **`document_loader.py`**  
   Demonstrates how to load documents from multiple sources, including PDFs, YouTube transcripts, and web pages.

## 🛠 **Functionality**
### **Key Features**

- **Suppresses deprecation warnings** for a cleaner console output.
- **Sets up the OpenAI API** by loading environment variables.
- **Loads documents** from various sources (PDFs, YouTube videos, and web pages).
- **Displays extracted content** for verification.

### **High-Level Flow**

1. **Document Loading**  
   - Loads PDF files and extracts text.
   - Downloads and transcribes audio from YouTube videos.
   - Scrapes web pages for relevant content.

2. **Splitting & Storage (Next Steps in the RAG Pipeline)**  
   - Once documents are loaded, they are split into smaller chunks.
   - The processed chunks are stored in a vector database for retrieval.

## 📝 **Example Outputs**

Below are **sample console outputs**, formatted to resemble a terminal display:

<details>
<summary>📄 PDF Loading Example</summary>

```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()
print(f"Loaded {len(pages)} pages from PDF.")
print("Sample page content:")
print(pages[0].page_content[:500])
print("Metadata:", pages[0].metadata)
```

```plaintext
Loaded 22 pages from PDF.
Sample page content:
MachineLearning-Lecture01
Instructor (Andrew Ng): Okay. Good morning. Welcome to CS229, the machine learning class. 
So what I wanna do today is just spend a little time going over the logistics...

Metadata: {'source': 'docs/cs229_lectures/MachineLearning-Lecture01.pdf', 'page': 0}
```
</details>

<details>
<summary>🎥 YouTube Video Transcription Example</summary>

```python
from langchain.document_loaders import GenericLoader
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser

url = "https://www.youtube.com/watch?v=jGwO_UgTS7I"
save_dir = "documents/youtube/"
loader = GenericLoader(
    YoutubeAudioLoader([url], save_dir),  # Fetch from YouTube
    OpenAIWhisperParser()
)
docs = loader.load()
print("Sample transcribed content:")
print(docs[0].page_content[:500])
```

```plaintext
Fetching video from YouTube: https://www.youtube.com/watch?v=jGwO_UgTS7I
Transcribing audio...

Sample transcribed content:
"Welcome to CS229 Machine Learning. Uh, some of you know that this is a class that's taught at Stanford for a long time..."
```
</details>

<details>
<summary>🌐 Web Page Content Extraction Example</summary>

```python
from langchain.document_loaders import WebBaseLoader

url = "https://github.com/basecamp/handbook/blob/master/titles-for-programmers.md"
loader = WebBaseLoader(url)
docs = loader.load()
print("Sample webpage content:")
print(docs[0].page_content[:500])
```

```plaintext
Fetching webpage content from: https://github.com/basecamp/handbook/blob/master/titles-for-programmers.md

Sample extracted content:
"Titles for Programmers
Programmer titles should be simple, clear, and descriptive. Here’s a list of titles used at Basecamp..."
```
</details>

## 🚀 **Conclusion**

This section demonstrates how to efficiently load documents from different sources, which is an essential step in setting up a **retrieval-augmented system**. The next steps will involve splitting the documents into smaller chunks, storing them in a **vector database**, and enabling retrieval for intelligent question-answering workflows.

Stay tuned for the next part, where we dive into **text chunking and storage**!

