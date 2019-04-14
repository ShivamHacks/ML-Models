"""

To download images:

mkdir class_name
googleimagesdownload --keywords "starbucks cup" --limit 100 --output_directory /home/sagrawa2/ML/ML_Models/images/class_name --nodirectory

"""




from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K

"""
base_model = InceptionV3(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(1, activation='sigmoid')(x)
model = Model(inputs=base_model.input, outputs=predictions)

for layer in base_model.layers:
	layer.trainable = False

"""

img_dir = '../ML_Models/images/'

image_datagen = ImageDataGenerator(
	rescale=1./255
)

image_generator = image_datagen.flow_from_directory(
	img_dir,
	classes = None,
	class_mode = 'binary',
	batch_size = 8
)

x, y = next(image_generator)

print('-----------')
print('x')
print(x.shape)
print('y')
print(y.shape)