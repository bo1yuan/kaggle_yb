#encoding=utf8
import magpie
from magpie import MagpieModel
label_list = ['toxic','severe_toxic','obscene','threat','insult','identity_hate']
magpie = MagpieModel()
"""
magpie.init_word_vectors('../../../kaggle_data/toxic_comment_classify/data/train_data/magpie_data/', vec_dim=300)
magpie.train('../../../kaggle_data/toxic_comment_classify/data/train_data/magpie_data/',label_list,nb_epochs=6)
magpie.save_word2vec_model('./magpie/embeddings/here',overwrite=True)
magpie.save_scaler('./magpie/scaler/here', overwrite=True)
magpie.save_model('./magpie/model/best_label.h5')
"""

magpie = MagpieModel(
        keras_model='./magpie/model/best_label.h5',
        word2vec_model='./magpie/embeddings/here',
        scaler='./magpie/scaler/here',
        labels=label_list
        )
print magpie.predict_from_text('User talk:121.214.58.105 - (Contributions)')
print magpie.predict_from_text("""And news of the Shaikh reached the emir of al-Ahsa and its dependencies from Bani Khalid, Sulaiman ibn 'Uray;ir al-Khaldi,        and it came to his knowledge that he called to God, and that he brought down the domes, and that he instituted the hudud [pun       ishments], and so the matter of the Shaikh disturbed this bedouin, for it is the habit of the bedouin - except those whom God        has guided - to rush to commit injustice, bloodshed, expropriation, and violation of prohibitions, so he feared that the power        of this Shaikh may increase and do away with the power of the bedouin prince.  And so he wrote to Uthman, threatening him, an       d ordered him that he must kill this mutawwa that is with him at 'Uyayna, and said: 'this mutawwa that is with you, such and s       uch has come to our knowledge about him!!  Either you kill him, or we cut off the dividend that you have with us', for the emi       r Uthman had [an annual] dividend of gold in the custody of [al-Khaldi].""")
