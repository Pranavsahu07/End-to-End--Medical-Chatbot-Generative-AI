from setuptools import find_packages, setup

setup(
    name='generative_ai_project',  # 💡 Use lowercase & underscores, not spaces
    version='0.0.1',
    author='Pranav Sahu',
    author_email='vanshsahu35@gmail.com',
    packages=find_packages(),
    install_requires=[],  # Add package dependencies here
    include_package_data=True,
    description='End-to-End Medical Chatbot using Generative AI',
    long_description='A Python package for an end-to-end generative AI medical chatbot.',
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust if needed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
