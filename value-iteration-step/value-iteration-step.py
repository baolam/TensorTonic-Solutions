def value_iteration_step(values: list, transitions: list, rewards: list, gamma: float) -> list[float]:
    """
    Perform one value-iteration update for every state.
    """
    # Write code here
    num_states = len(transitions)
    
    new_values = [0.0] * num_states
    
    for s in range(num_states):
        num_actions = len(transitions[s])
        q_values = []
        
        for a in range(num_actions):
            reward = rewards[s][a]

            expected_future_value = 0
            for s_next in range(num_states):
                expected_future_value += transitions[s][a][s_next] * values[s_next]

            q_values.append(reward + gamma * expected_future_value)
        

        new_values[s] = max(q_values) if q_values else 0.0
        
    return new_values