def value_iteration_step(values: list, transitions: list, rewards: list, gamma: float) -> list[float]:
    """
    Perform one value-iteration update for every state.
    """
    # Write code here
    num_states = len(values)
    new_values = [0.0] * num_states

    for s in range(num_states):
        num_actions = len(transitions[s])
        q_values = []

        for a in range(num_actions):
            r = rewards[s][a]

            expected_future_value = 0.0
            for s_next in range(num_states):
                prob = transitions[s][a][s_next]
                expected_future_value += prob * values[s_next]

            q_sa = r + gamma * expected_future_value
            q_values.append(q_sa)

        new_values[s] = max(q_values) if q_values else 0.0

    return new_values