from os import listdir
import json
from features import ImageFeatures

image_features = ImageFeatures.ImageFeatures()

data = {}

for f in listdir('images'):
    data[f] = image_features.detect_image_text('images/'+f)

with open('data.json', 'w') as fp:
    json.dump(data, fp)
