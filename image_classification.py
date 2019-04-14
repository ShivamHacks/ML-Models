"""

To download images:

mkdir class_name
googleimagesdownload --keywords "starbucks cup" --limit 100 --output_directory /home/sagrawa2/ML/ML_Models/images/class_name --nodirectory

"""




from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K

base_model = InceptionV3(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)
model = Model(inputs=base_model.input, outputs=predictions)

for layer in base_model.layers:
	layer.trainable = False

img_dir = '../ML_Models/images/starbucks cup'

image_generator = image_datagen.flow_from_directory(
	'images',
	classes = None,
	class_mode = 'binary'
)

print(next(image_generator))