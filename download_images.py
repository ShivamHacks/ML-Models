from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

absolute_image_paths = response.download({
	'keywords': 'starbucks cup',
	'limit': 100,
	'output_directory': '/home/sagrawa2/ML/ML_Models/images/',
	'nodirectory': True
})