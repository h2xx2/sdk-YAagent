from setuptools import setup, find_packages

setup(
<<<<<<< HEAD
    name="ya-agent-sdk",
    version="0.1.0",
    description="Python SDK для YA Agent API",
    author="Твоё Имя",
    author_email="you@example.com",
    packages=find_packages(),
    install_requires=["requests>=2.20.0"],
    python_requires=">=3.7",
=======
    name="yaagent",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.30.0"
    ],
    python_requires=">=3.9",
    description="Python SDK to interact with YAAgent chatbot API",
    author="Your Name",
    url="https://github.com/yourusername/sdk-YAagent",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
>>>>>>> 1761eda (test2)
)
