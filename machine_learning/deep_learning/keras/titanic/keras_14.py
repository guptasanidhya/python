from keras.models import load_model
my_model = load_model('model_file.h5')
predictions = my_model.predict([[2.      ,  34.      ,   0.      ,   0.      ,  13.      ,
          1.      ,   0.     ,   0.      ,   0.      ,   1.    ]])
probability_true = predictions[:,1]
print(probability_true)