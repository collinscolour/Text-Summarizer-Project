import setuptools

with open(r"C:\Users\ha\p_r_o_j_e_c_t\Text-Summarizer-Project\README.md", "r", encoding="utf_8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "P_R_O_J-E_C_T"
AUTHOR_USER_NAME = "collinscolour"
SRC_REPO = "collins_text_summarizer"
AUTHOR_EMAIL ="collinscolour121@yahoo.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=" Collins Text app",
    long_description=long_description,
    long_description_content= "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
        "bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages= setuptools.find_packages(where="src")

)

