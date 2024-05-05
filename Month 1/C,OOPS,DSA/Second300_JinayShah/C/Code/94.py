import numpy as np

class SkipGram:
    def __init__(self, vocab_size, embedding_dim, learning_rate):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.learning_rate = learning_rate

        self.in_embeddings = np.random.randn(vocab_size, embedding_dim)
        self.out_embeddings = np.random.randn(vocab_size, embedding_dim)

    def forward(self, target_idx, context_idx):
        target_embed = self.in_embeddings[target_idx]
        context_embed = self.out_embeddings[context_idx]
        score = np.dot(target_embed, context_embed)
        return score

    def backward(self, target_idx, context_idx, score):
        target_embed = self.in_embeddings[target_idx]
        context_embed = self.out_embeddings[context_idx]

        grad_in_embed = np.outer(score, context_embed).flatten()
        grad_out_embed = np.outer(score, target_embed).flatten()

        # Update embeddings using gradient descent
        self.in_embeddings[target_idx] -= self.learning_rate * grad_in_embed
        self.out_embeddings[context_idx] -= self.learning_rate * grad_out_embed


corpus = [
    "I love natural language processing",
    "Word embeddings capture semantic meaning",
    "Skip-gram is an embedding model"
]

words = [word for sentence in corpus for word in sentence.split()]
vocab = list(set(words))
word_to_index = {word: idx for idx, word in enumerate(vocab)}
index_to_word = {idx: word for idx, word in enumerate(vocab)}

skip_grams = []
window_size = 2

for sentence in corpus:
    words = sentence.split()
    for target_idx, target_word in enumerate(words):
        for context_word in words[max(0, target_idx - window_size): target_idx] + words[target_idx + 1: min(target_idx + window_size + 1, len(words))]:
            skip_grams.append((word_to_index[target_word], word_to_index[context_word]))

vocab_size = len(vocab)
embedding_dim = 50
learning_rate = 0.01
skipgram_model = SkipGram(vocab_size, embedding_dim, learning_rate)

num_epochs = 1000

for epoch in range(num_epochs):
    total_loss = 0
    for target_idx, context_idx in skip_grams:
        score = skipgram_model.forward(target_idx, context_idx)
        loss = -np.log(1 / (1 + np.exp(-score)))  # Negative log likelihood loss (sigmoid cross entropy)
        total_loss += loss
        skipgram_model.backward(target_idx, context_idx, 1 / (1 + np.exp(-score)))

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss:.4f}')

word_embeddings = skipgram_model.in_embeddings

for idx, word in index_to_word.items():
    print(f'{word}: {word_embeddings[idx]}')
