import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        #model = load_model(os.path.join("artifacts", "training", "model.h5"))
        #do this when u deployment
        model = load_model(os.path.join("model", "model.h5"))

        # Load and preprocess image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0  # Normalize, since your generator used rescale=1./255

        # Predict
        result = model.predict(test_image)
        print("Raw prediction vector:", result)
        result_class = np.argmax(result, axis=1)
        print("Predicted class index:", result_class)

        # Match class mapping {'adenocarcinoma': 0, 'normal': 1}
        if result_class[0] == 0:
            prediction = 'Adenocarcinoma Cancer'
        else:
            prediction = 'Normal'

        return [{"image": prediction}]
