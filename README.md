# CMPM_Project3: Pokemon Trading Card Generator

This project focuses on creating Pokemon trading cards using machine learning and neural networks. each folder has a read me atatched for 

## Python files  
The python files located in the helper directory are used to download images and card text from the PokemonTCG API.

Use CardReader to download images and CardCropper to crop them down to just the card art, AttackReader to download attack text and both NameReader files to download Pokemon names in the necessary format.

You can run the necessary files by running `python [filename].py`.

## Generators  
Use the char-rnn-tensorflow programs under the text generation directory to train and generate card attacks and Pokemon names. Navigate to the relevant folder and run `python sample.py`.

Navigate to the image generation directory to generate images, for a new set of images navigate to pokeganSprites or pokeganCards and run `test.py`

our workflow involved generating images and passing the results to pix to pix, the output is the final image, to run it on a sample navigate to the folder and type `.`


## Classifiers  
The SimpleImageClassifier is trained on existing Pokemon card images, and can be used to classify generated images.

NameClassifier and AttackClassifier are used to classify text. They take in a CSV of names and attacks and can be used to classify generated names and attacks. 

## Results

