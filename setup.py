from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "book_recomendation_system"
AUTHOR_USER_NAME = "Theshika"
SRC_REPO = "src"
def new_func():
    return 'streamlit', 'numpy'

LIST_OF_REQUIREMENTS = [new_func()]


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A Book Recommender System using machine learning KNN Algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=[SRC_REPO],
    python_requires=">=3.11",
    install_requires=LIST_OF_REQUIREMENTS
)