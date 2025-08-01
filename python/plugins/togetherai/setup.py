"""
Setup configuration for Composio Together AI plugin.
"""

from pathlib import Path

from setuptools import setup


setup(
    name="composio_togetherai",
    version="0.7.20",
    author="Composio",
    author_email="tech@composio.dev",
    description="Use Composio to get an array of tools with your Together AI Function Call.",
    long_description=(Path(__file__).parent / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/ComposioHQ/composio",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9,<4",
    install_requires=[
        "composio_core>=0.7.0,<0.8.0",
        "together",
        "openai",
    ],
    include_package_data=True,
)
