# CMPM_Project3: Pokemon Trading Card Generator

This project focuses on creating Pokemon trading cards using machine learning and neural networks.

## Python files  
The python files in the main directory are used to download images and card text from the PokemonTCG API.

Use CardReader to download images and CardCropper to crop them down to just the card art, AttackReader to download attack text and both NameReader files to download Pokemon names in the necessary format.

You can run the necessary files by running `python [filename].py`.

## Generators  
Use the char-rnn-tensorflow programs to train and generate card attacks and Pokemon names. Navigate to the relevant folder and run `python sample.py`.

[insert GAN stuff here]

## Classifiers  
The SimpleImageClassifier is trained on existing Pokemon card images, and can be used to classify generated images.

NameClassifier and AttackClassifier are used to classify text. They take in a CSV of names and attacks and can be used to classify generated names and attacks. 

## Results
