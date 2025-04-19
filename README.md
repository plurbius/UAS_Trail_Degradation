# UAS_Trail_Degradation
This repository houses the data and workflow for the drone collected trail degradation model used for John Lesko Master thesis. The thesis, and its methodology, can be access [here](....)

## Models
In the Models repository you will find the python scripts used to measure each trail degradation characteristic (width, incision, grade, and rugosity), and the eventual trail degradation models. The background behind these analyses are explained in the methodology section of the thesis linked above. 

## Project Data
Due to file size limitations, the data for this data is not stored in this repository. Instead, the orthomosaic, Digital Surface Model, Study areas, trail tread areas, as well as the model outputs for all of the trail degradation characteristics and trail degradation models can be accessed [here](https://drive.google.com/drive/folders/17ck0FtimM4gk1I6M4aG2rjHi9b23HaQh?usp=sharing) via a shared folder on google drive. The data is stored by trail as features classes in file geodatabases.

For the models to run, users will either have to use the parameter inputs to load their own data, or to use the data provided in the data linked above. The essential data inputs include a study area, trail tread area, digital surface model, and orthomosaic imagery for the trail you are surveying.

## Flight Plans
Flight plans are available upon request via drone deploy, although flight parameters are noted in the methodology portion of the thesis linked above. Please reach out to the author at john.lesko@gwmail.gwu.edu
