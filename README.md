# Project Foxtrot
***
## Installation
___
## Setting Up Virtual Environment
1. ### Using Venv
    You can install venv to your host Python by running this command in your terminal:
    ```shell
    $ pip install virtual env
    ```
   To use venv in your project, in your terminal, create a new project folder, cd to the project folder in your terminal, and run the following command:
    ```shell
    $ python<version> -m venv <virtual-environment-name>
    ```
   Now that you have created the virtual environment, you will need to activate it before you can use it in project. 
   To do that:

   ```shell
   $ source env/bin/activate
   ```
   
   
2. ### Using Conda
   `Recommended:` If you don't have conda you can download it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).   
   `Note:` If you are using homebrew on mac, you can install conda by running command below.
   ```shell
   $ brew install --cask anaconda
   ```
   To **Create** virtual environment :
   ```shell
   $ conda create -n <env-name>
   ```
   To **Activate** virtual environment : 
   ```shell
   $ conda activate <env-name>
   ```

___
```shell
$ pip install git+https://github.com/idoshr/flask-mongoengine.git@1.0.1
```