import random

# Example dataset generation
data = [
    "Artificial Intelligence in Healthcare is revolutionizing patient care",
    "Machine learning algorithms are being used to analyze medical data",
    "Social media platforms use AI to personalize user experience",
    "Video content creation is being automated by neural networks",
    "Natural Language Processing (NLP) enables chatbots to understand human language"
]

# Generate more synthetic data for training
for _ in range(20):
    sentence = random.choice(data)
    new_sentence = sentence.lower() + " " + " ".join(random.sample(sentence.split(), random.randint(2, 5)))
    data.append(new_sentence)

# Save dataset to a file
with open('training_data.txt', 'w') as f:
    for sentence in data:
        f.write(sentence + '\n')

print("Dataset created and saved as 'training_data.txt'.")
