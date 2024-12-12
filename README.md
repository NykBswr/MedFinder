# MedFinder

## Description

**MedFinder** is an intuitive and efficient web-based application designed to help users find relevant medication based on their symptoms. The system utilizes both **semantic search** and **lexical search** models to process user queries and recommend medications with detailed information such as usage instructions, price range, dosage, and side effects. Built using **Flask** as the web framework and **Tailwind CSS** for responsive design, MedFinder provides a seamless user experience, making it easier for healthcare professionals and patients to access medication-related information.

The application processes queries using two models combined into one hybrid model:

1. **Lexical Search** : Uses keyword matching and term frequency models like **BM25L** to retrieve relevant documents based on exact keyword matches.
2. **Semantic Search** : Utilizes advanced transformer-based models, such as  **MPNet** , to understand the context of the user query and return more relevant results even when queries are ambiguous or imprecise.
3. **Hybrid Search** : The results from both models are fused using **Reciprocal Rank Fusion** to enhance the accuracy and reliability of the recommendations.

This application is ideal for anyone looking for accurate and fast information regarding medications, whether for personal use or professional purposes in healthcare.

## Run this code to start the website after installing env and tailwind CSS

To run the **MedFinder** website on your local machine, follow these detailed steps after setting up the development environment:

### 1. **Activate Virtual Environment**

Before starting the website, you need to activate your virtual environment where all dependencies are installed.

For  **Windows (PowerShell)** :

```
\env\Scripts\activate
```

For  **macOS/Linux** :

```
source env/bin/activate
```

This will activate the virtual environment, and you should see `(env)` in your terminal prompt, indicating the environment is active.

### 2. **Set Flask App Environment Variable**

Set the **Flask** application environment variable to tell Flask which file to run. This tells Flask to use **`app.py`** as the entry point for the application.

For  **Windows (PowerShell)** :

```
$env:FLASK_APP="app.py"
```

For  **macOS/Linux** :

```
export FLASK_APP=app.py
```

### 3. **Enable Flask Debug Mode**

To enable debugging mode and get real-time error reporting, set the **FLASK_DEBUG** environment variable to  **1** .

For  **Windows (PowerShell)** :

```
$env:FLASK_DEBUG=1
```

For  **macOS/Linux** :

```
export FLASK_DEBUG=1
```

This will allow automatic reloading of the server when you make changes to the code.

### 4. **Run Flask Development Server**

Start the **Flask** development server by running the following command:

```
flask run
```

After this, Flask will start serving the app locally on your machine at `http://127.0.0.1:5000` (or a similar URL displayed in the terminal).

### 5. **Compile Tailwind CSS**

To apply the styles using  **Tailwind CSS** , you need to compile the **CSS** file. Run the following command to start watching for any changes in the source CSS file and generate the final output:

```
npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```

This command takes the **`input.css`** file from the **`static/src`** directory and compiles it into **`output.css`** in the **`static/css`** directory. The **`--watch`** flag ensures that any changes made to **`input.css`** will automatically reflect in **`output.css`** without needing to run the command again.
