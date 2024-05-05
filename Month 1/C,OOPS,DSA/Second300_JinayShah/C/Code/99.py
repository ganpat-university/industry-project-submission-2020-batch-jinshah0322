def viterbi(observations, states, initial_probs, transition_probs, emission_probs):
    num_states = len(states)
    seq_len = len(observations)

    viterbi_matrix = [[0.0] * num_states for _ in range(seq_len)]
    backpointer_matrix = [[0] * num_states for _ in range(seq_len)]

    for i in range(num_states):
        viterbi_matrix[0][i] = initial_probs[i] * emission_probs[i][observations[0]]
        backpointer_matrix[0][i] = 0

    for t in range(1, seq_len):
        for j in range(num_states):
            max_prob = 0.0
            max_state = 0

            for i in range(num_states):
                prob = viterbi_matrix[t - 1][i] * transition_probs[i][j]
                if prob > max_prob:
                    max_prob = prob
                    max_state = i

            viterbi_matrix[t][j] = max_prob * emission_probs[j][observations[t]]
            backpointer_matrix[t][j] = max_state

    best_last_state = max(range(num_states), key=lambda i: viterbi_matrix[seq_len - 1][i])

    best_path = [best_last_state]
    for t in range(seq_len - 1, 0, -1):
        best_last_state = backpointer_matrix[t][best_last_state]
        best_path.insert(0, best_last_state)

    return best_path

states = [0, 1]  
observations = [0, 1, 2, 1, 0]  

initial_probs = [0.5, 0.5]  
transition_probs = [[0.7, 0.3], [0.4, 0.6]]  
emission_probs = [[0.2, 0.4, 0.4], [0.5, 0.4, 0.1]]  
best_path = viterbi(observations, states, initial_probs, transition_probs, emission_probs)
print("Best path:", best_path)
