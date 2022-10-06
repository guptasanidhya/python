from keras.models import load_model
my_model = load_model('/machine_learning/deep_learning/keras/model_file.h5')
predictions = my_model.predict([[1,38.0,1,0,71.2833,0,1,0,0]])
probability_true = predictions[:,1]
print(probability_true)