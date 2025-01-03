# FinChat: Earnings Report Analysis Chatbot

**FinChat** is an interactive chatbot application designed to process and analyze uploaded PDF files of earnings reports. Using a **Retrieval-Augmented Generation (RAG)** approach, the app integrates with **Llama 3.2** for enhanced document processing and user interaction.

## Key Features:
- **File Upload Handling**: Users can upload PDF files of earnings reports (max 10 MB). The chatbot will analyze the document and add it to the knowledge database for further use.
- **Multi-file Upload**: Once a file is uploaded, users are prompted to upload additional files by typing "upload the next file". This allows users to add multiple earnings reports for analysis.
- **Dynamic Chat Responses**: The bot processes user input and provides responses based on the uploaded data. Users can ask questions related to the uploaded reports, and the chatbot will fetch relevant information from the knowledge base.
- **Session Management**: The app retains session data, so users can interact continuously with the uploaded files without needing to re-upload them.
- **RAG-powered Analysis**: The app leverages **Retrieval-Augmented Generation (RAG)** to fetch information from the uploaded documents, combining it with the generative capabilities of **Llama 3.2** for intelligent responses.

## Technologies Used:
- **Chainlit**: Used to create an interactive chat interface for seamless communication between the user and the application.
- **Embedchain**: Integrated for document processing and knowledge management to efficiently store and retrieve the data from uploaded PDF files.
- **ChromaDB**: Used as a vector storage for efficiently storing and retrieving the PDF content in the knowledge base.
- **RAG (Retrieval-Augmented Generation)**: Powers the application by retrieving relevant information from documents to generate responses.
- **Llama 3.2**: A powerful language model that is used to understand and generate human-like responses to the user’s queries, integrated with **Ollama** for optimized performance.
- **Python**: The entire app is developed in Python, leveraging Chainlit and Embedchain libraries for functionality.

## Prerequisites:
Before running the app, ensure you have the following:

1. **Python**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. **Python Package Manager**: You can use `pip` (default package manager) or `conda` (if you're using Anaconda) to manage dependencies.
3. **Code Editor**: Use any code editor like Visual Studio Code, PyCharm, or Sublime Text to edit the files.
4. **Ollama**: Download and install Ollama to set up **Llama 3.2** and **all-minilm** models. You can get the instructions for installation [here](https://ollama.com).
   - To install **Llama 3.2**, run the following command after installing Ollama:
     ```
     ollama run llama3.2
     ```
   - Ensure that **Ollama** is running before starting the app. To check if Ollama is running, open a terminal and use the following command:
     ```
     ollama status
     ```
     If the server is running, you should see an output indicating that Ollama is active.
   - **Screenshot Placeholder**: Add a screenshot here showing the Ollama terminal output with the status `running`.
5. **Install Chainlit**: Install the **Chainlit** library using `pip`:
     ```
     pip install chainlit
     ```
     - After installation, ensure that Chainlit is added to your environment.
6. **Install Dependencies**: 
- Install necessary dependencies using the `requirements.txt` file provided in the repository. You can do this by running:
  ```
  pip install -r requirements.txt
  ```
7. **Llama 3.2 & all-minilm Models**: Ensure that you have **Llama 3.2** and **all-minilm** models installed through Ollama to ensure the chatbot performs optimally.
8. **Visual Studio**: You must have the **Desktop Development with C++** workload installed in Visual Studio. This is required for building and running some dependencies.

## How to Run the App:
1. **Clone the Repository**:
- Clone the repository to your local machine using:
  ```
  git clone https://github.com/mehmoodulhaq570/FinChat.git
  ```
2. **Install Dependencies**:
- Open a terminal/command prompt in the project directory.
- Install the required dependencies:
  ```
  pip install -r requirements.txt
  ```
3. **Configure Embedchain**:
- Update the `config.yml` file in the root directory with your specific configuration for Embedchain.
4. **Install Chainlit**:
- Install Chainlit using `pip`:
  ```
  pip install chainlit
  ```
5. **Ensure Ollama is Running**:
- Before starting the app, ensure Ollama is running by executing the following:
  ```
  ollama status
  ```
- **Screenshot Placeholder**: Add a screenshot here showing the Ollama terminal output with the status `running`.
6. **Navigate to the App Directory**:
- Navigate to the project directory `chat-with-financial-reports`:
  ```
  cd chat-with-financial-reports
  ```
7. **Run the Application**:
- Open a terminal in the project directory and run the app with the following command:
  ```
  chainlit run app.py
  ```
8. **Interact with the Chatbot**:
- Once the app is running, open your browser and interact with the chatbot by uploading your earnings report PDFs and asking questions based on the uploaded data.

## Video Demo:
- **[Add a link to a demo video of running the app here]**: The video demonstrates the step-by-step process of uploading the PDF and interacting with the FinChat bot.

## Future Improvements:
- **Support for more file formats**: Extend the application to support other document formats such as Word and Excel.
- **Enhanced query handling**: Implement more advanced natural language processing for improved query responses.
- **Authentication**: Add user authentication to ensure secure file handling.

---

Feel free to contribute to the project or suggest any improvements!
