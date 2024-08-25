from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="vxapi",
    version="1.1",

    description="virus.exchange wrapper for python",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/clienthold/vxapi",
    author="Dmitry Kondrashov",

    packages=["vxapi"],
    python_requires=">=3.7, <4",
    install_requires=["requests"]
)
