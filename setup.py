from setuptools import setup, find_packages

setup(
    name="ya-agent-sdk",
    version="0.1.0",
    description="Python SDK для YA Agent API",
    author="Твоё Имя",
    author_email="you@example.com",
    packages=find_packages(),
    install_requires=["requests>=2.20.0"],
    python_requires=">=3.7",
)
