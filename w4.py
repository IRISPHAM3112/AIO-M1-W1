import streamlit as st

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

def levenshtein_distance(token1, token2):
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                distances[t1][t2] = min(a, b, c) + 1

    return distances[len(token1)][len(token2)]

def main():
    st.title("Word Correction using Levenshtein Distance")
    
    # Load vocab
    vocabs = load_vocab(file_path='E:/AIO/hehehe/w1/aio-MD2-w1/w4/vocab.txt')


    
    word = st.text_input('Enter word to correct:')
    
    if st.button("Compute"):
        # Calculate levenshtein distances
        leven_distances = {vocab: levenshtein_distance(word, vocab) for vocab in vocabs}
        
        # Sort by distance
        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        
        # Display results
        st.write(f"Correct word: {correct_word}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write('Vocabulary:')
            st.write(vocabs)
        
        with col2:
            st.write('Distances:')
            st.write(sorted_distances)

if __name__ == "__main__":
    main()
