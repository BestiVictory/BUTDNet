# BUTDNet
For image review techniques, the quality of the generated results depends on the quality of the dataset. But not all domains have high-quality datasets available. In this case, our pipeline can be used to build a data set by itself when there is a lack of high-quality data sets, and generate natural language results that meet a certain quality.
The following describes the filtering process of our self-built dataset as follows:
(1) Obtain a large enough data set with a large number of short sentences.
(2) Use some techniques of natural language processing to clean and organize the data.
(3) Determine a topic, such as photography, people, flowers, etc., and manually select a small number of sentences that match the selected topic for classification.
(4) Use these sentences to select the bag-of-words model as the word vector matrix of the corresponding corpus.
(5) Use this vector matrix to train a WMD model.
(6) Use the model trained by the above method to filter the remaining text in the text, calculate the cosine similarity between the text set and the multiple subject words obtained by the WMD topic calculation, and use it as a sentence whether it conforms to our selection. The sentence corresponds to the threshold of the topic model.
(7) Add sentences filtered by topic relevance, and then train a WMD model.
(8) Using this model, the remaining sentences in the text are judged and screened by cosine similarity.
(9) The sentences that have been screened three times in total by manual subjective selection, topic similarity detection and screening, and cosine similarity comparison sorting and screening are used as the determined and retained text data set.
Through the above method, we call the obtained dataset as "FAE-Captions" dataset with a volume of more than 100G.
