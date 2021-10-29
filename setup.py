
import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "na"

setuptools.setup(
    name='Ahmadsfunktioner',
    version='0.0.2',
    author='Ahmad Zarzar',
    author_email='ahmadzrzr97@gmail.com',
    description='Good to have things',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ahmad223455322/goodtohavefunktioner',
    project_urls = {
        "Bug Tracker": "https://github.com/Ahmad223455322/goodtohavefunktioner/issues"
    },
    license='MIT',
    packages=['Ahmadsfunktioner'],
    install_requires=['requests']
)