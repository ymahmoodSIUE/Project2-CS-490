import numpy as np

def onehote(seq):
    encoding = []
    mapping = {"A": [1, 0, 0, 0], "C": [0, 1, 0, 0], "G": [0, 0, 1, 0], "T": [0, 0, 0, 1]}
    for base in seq:
        encoding.append(mapping.get(base, [0, 0, 0, 0]))
    return np.array(encoding)

# Open the input file
with open("validation_file.txt", "r") as input_file:
    encoded_sequences = []  # List to store the encoded sequences
    # Loop through each line (sequence) in the input file
    for line in input_file:
        sequence = line.strip()  # Remove leading/trailing whitespace, including newline
        oneHotEncodedSequence = onehote(sequence)
        encoded_sequences.append(oneHotEncodedSequence)

# Convert the list of encoded sequences to a numpy array
encoded_sequences_array = np.array(encoded_sequences)

# Save the numpy array to a .npy file
np.save("validationout.npy", encoded_sequences_array)

