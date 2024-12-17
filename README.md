# python-rest-demo
python-rest-demo

### Step 1: 
#### Set Up Your Python Environment
* Install Python: Ensure Python 3.x is installed on your system. 
* Verify with:
```python
python3 --version
```

#### Create a Virtual Environment: Set up an isolated Python environment for your project:

```python
python3 -m venv myapi-env
cd myapi-env
source bin/activate  # On Windows: myapi-env\Scripts\activate

```
#### Install Flask: Install Flask using pip:
```python
pip install flask
```

### Step 2: Create a Basic Flask Application

#### Set Up the Project Directory: Create a directory structure for your project:
```python
myapi/
├── app.py         # Main API file
├── requirements.txt  # Dependencies file

```

#### Write the API Code in app.py:

### Step 3: Save Dependencies

#### Save the installed dependencies to a file for reproducibility:
```python
pip freeze > requirements.txt

```

### Step 4: Start the Flask Server

#### Navigate to the project directory:
```python
cd path/to/myapi/
```
#### Start the server
```python
python app.py
```
#### Output: You should see something like:
```python
* Running on http://127.0.0.1:5000
```
