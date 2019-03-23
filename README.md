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

Combing various results from text generation (RNNS) and image generation (GANS) and classifying them we had a somewhat cohesive overall look. While not perfect, there is a general shape, text and color structure that we think fits with the type of classified cards. 

the images below was classified as a fighting/ground  type based on the classifier, the input image was from the wgan, poke-card version, both the name, text and HP are also generated using the text generation NNs

worsola and Gordele cards:


<p float="left">
    <img src="https://github.com/rj-90/CMPM_Project3/blob/master/worsola.jpg" height="300" width="200" /> 

  <img src="https://github.com/rj-90/CMPM_Project3/blob/master/g.jpg" height="300" width="200" />

</p>



the WGAN, pokemon sprite version generated this image, the pokemon was classified as a ghost or psychic type with a hp of 100 and a costly type move, the color pallet, and shape in our opinion matches the nature of the card. What differentiates this card is a more defined outline 

Lsmilea 

  <img src="https://github.com/rj-90/CMPM_Project3/blob/master/ls.jpg" height="300" width="200" /> 

all images, have been passed through the pix-to-pix model to get a more defined shape and outline. 




















# credits: 

kindly note the original credit of work and specific readme(s  )belongs to the authors,   the varied readme's within each folder 

### data sorces: 

Card data set credit: https://pokemontcg.io/

pokemon images data sets:  https://www.kaggle.com/kvpratama/pokemon-images-dataset

### github code sources: 

Siraj's youtube explanation and link to github:  https://www.youtube.com/watch?v=yz6dNf7X7SA https://github.com/llSourcell/Pokemon_GAN

Pix to Pix: https://github.com/affinelayer/pix2pix-tensorflow

Char rnn: https://github.com/sherjilozair/char-rnn-tensorflow

char-rnn:  https://github.com/karpathy/char-rnn

text classification: https://github.com/jiegzhan/multi-class-text-classification-cnn

 Manu Mathew Thomas. original Gan and Simple classifier


