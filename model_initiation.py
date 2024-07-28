from transformers import DistilBertTokenizer
from transformers import TFDistilBertForSequenceClassification
import tensorflow as tf
import os
os.environ["TF_USE_LEGACY_KERAS"] = '0'

save_directory = "content\Multitext_Classification_colab"
loaded_tokenizer = DistilBertTokenizer.from_pretrained(save_directory)
loaded_model = TFDistilBertForSequenceClassification.from_pretrained(save_directory)

def prediction_get(pred):
  result = {
      0:"Negative",
      1:"Netral",
      2:"Positve"
  }
  return result.get(pred)


def predict(text):
  predict_input = loaded_tokenizer.encode(text,
  truncation=True,
  padding=True,
  return_tensors="tf")

  output = loaded_model(predict_input)[0]

  prediction_value = tf.argmax(output, axis=1).numpy()[0]
  return prediction_get(prediction_value)

# print(predict("i love pretty soft shirt falls well want wear everyday"))