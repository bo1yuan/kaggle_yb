#encoding=utf8
import magpie
from magpie import MagpieModel
label_list = ['toxic','severe_toxic','obscene','threat','insult','identity_hate']
magpie = MagpieModel()
magpie.init_word_vectors('../../../kaggle_data/toxic_comment_classify/data/train_data/magpie_data/', vec_dim=300)
magpie.train('../../../kaggle_data/toxic_comment_classify/data/train_data/magpie_data/',label_list,nb_epochs=6)
magpie.predict_from_text('')
