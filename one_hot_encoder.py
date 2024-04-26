import numpy as np

def onehote(seq):
    encoding = []
    mapping = {"A": [1, 0, 0, 0], "C": [0, 1, 0, 0], "G": [0, 0, 1, 0], "T": [0, 0, 0, 1]}
    for base in seq:
        encoding.append(mapping.get(base, [0, 0, 0, 0]))
    return np.array(encoding)


with open("validation_file.txt", "r") as input_file:
    encoded_sequences = []  
    
    for line in input_file:
        sequence = line.strip()  
        oneHotEncodedSequence = onehote(sequence)
        encoded_sequences.append(oneHotEncodedSequence)


encoded_sequences_array = np.array(encoded_sequences)


np.save("validationout.npy", encoded_sequences_array)

