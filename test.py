# TF1 version
import tensorflow.compat.v1 as tf
import tensorflow_hub as hub
import tensorflow_text as tf_text

tf.compat.v1.disable_eager_execution()


text_generator = hub.Module('https://www.kaggle.com/models/google/bertseq2seq/TensorFlow1/roberta24-bbc/1')

input_text_bbc = """The Dung Beetle UK Mapping Project (Dump) is still in the early stages of its research work, which has included examining beetle sites in Scotland.
However, the team said it had already noted an "alarming trend" of decline of some species.
Dung beetles play key roles in improving soils and controlling pests.
Reasons for the decline in some beetle species include coming into contact with anthelmintics, a type of drug given to livestock to control intestinal worms that prevent the farm animals from thriving.
Dump involves Darren Mann, who is head of life collections at the Oxford University Museum of Natural History, Steve Lane, Ceri Watkins and Sally-Ann Spence.
The project is not funded and the team members have been doing their research in their spare time, while on family holidays and fitting it around their other work.
The scientists have been examining well-documented dung beetle sites, including locations in the Cairngorms, and have also been looking for the insects in previously unrecorded places.
They hope to enlist the help of organisations that record flora and fauna and also wildlife enthusiasts, whose attention is being drawn to Dump via social media. On Twitter the project has the hashtags #dungathon and #dungisfun.
Ms Spence said some of Dump's early results had given cause for concern.
She said: "Our results mapping the dung beetle species in the UK, although the project is in its youth, are already showing an alarming trend in species rarity and even extinction.
"The three main reasons behind this are considered to be the use of anthelmintics, soil disturbance and the disappearance of livestock from historic pastures due to a change in farming practices."
It has been suggested that dung beetles save the UK's cattle industry an estimated <C3><82><C2><A3>367m a year, Ms Spence said.
They do this by encouraging the growth of healthy grass through their burrowing in soil, which aerates it and allows rainwater and nutrients into the ground.
Dung beetles also eat animal droppings harbouring parasites harmful to livestock.
Ms Spence said: "We take the opportunity of our survey visits to make farmers and livestock keepers aware of their dung beetles, the latest research, their economic benefits and how they might implement simple workable measures ensure a healthy dung beetle population.
"We have received a fantastically positive response from all we have spoken to.
"Farmers are keen to preserve their dung beetles and we intend to gather more data about species and their population frequencies to enable more research into these incredibly important beetles."
As well as their importance to agriculture, the beetles and their grubs are food for wild birds and mammals.
Scotland has the UK strongholds for at least three species of dung beetle - Aphodius fasciatus, Aphodius lapponum and Aphodius nemoralis.
The Cairngorms and the Western Isles are among the best recorded areas for the creatures, but large parts of the rest of Scotland remain unrecorded.
Ms Spence said: "The project is vast.
"Different species live in, or under, different dung in different stages of decomposition on different soils at different altitudes at different times of the year.
"Dung quality is important too. We have become connoisseurs of fine dung. Not adverse to feeling the texture or giving it a good sniff - you can tell a lot about an animals health by its dung - we will examine it meticulously for beetles."
The end result will be a dataset of dung beetle information, including identification, distribution maps, ecology and species conservation status. This will be made available via The British Beetles website and will include an online recording system using Irecord."""

input_documents = [input_text_bbc]
output_summaries = text_generator(input_documents)

# Create a TensorFlow session
with tf.Session() as sess:
    # Initialize variables if the module has any (often needed for Hub modules)
    sess.run(tf.global_variables_initializer())
    sess.run(tf.tables_initializer()) # Also often needed for text/lookup tables

    # Run the tensor and fetch its value
    summaries = sess.run(output_summaries)

# --- End of new code ---

# Print the fetched summaries
print("Generated Summaries:")
for i, summary in enumerate(summaries):
    print(f"Document {i+1}: {summary.decode('utf-8')}") # Decode from bytes to string
