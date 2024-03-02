import numpy as np
import gym

# Mapping VARK preferences to actions
VARK_mapping = {
    0: 'Visual',
    1: 'Aural',
    2: 'Read/write',
    3: 'Kinesthetic'
}

# Instantiate the VARKLearning environment
class VARKLearningEnvironment:
    def _init_(self):
        self.observation_space = gym.spaces.Discrete(4)  # 4 VARK states
        self.action_space = gym.spaces.Discrete(len(VARK_mapping))
        self.current_state = 0

    def step(self, action, grade):
        # Update Q-value using the Q-learning iteration
        Q_table[self.current_state, action] = (1 - alpha) * Q_table[self.current_state, action] + alpha * (
                grade + gamma * np.max(Q_table[self.current_state, :]))

        # Transition to the next state (VARK preference)
        self.current_state = (self.current_state + 1) % 4

        # The environment is considered done when the student achieves a grade of 1/1
        done = (self.current_state == 0)

        return self.current_state, done

    def reset(self):
        self.current_state = 0
        return self.current_state

# Initialize the VARKLearning environment
env = VARKLearningEnvironment()
n_observations = env.observation_space.n
n_actions = env.action_space.n

# Initialize the Q-table to 0
Q_table = np.zeros((n_observations, n_actions))

# Define parameters and hyperparameters
alpha = 0.1            # Learning rate
gamma = 0.99           # Discount factor
epsilon = 1.0          # Exploration-exploitation trade-off
epsilon_decay = 0.002  # Decay constant for exploration

# Initialize variable to store final output
final_output = None

# Initialize cumulative Q-values
cumulative_Q_values = np.zeros((n_observations, n_actions))

# Main loop with an indefinite number of iterations
iteration = 0
while True:
    state = env.reset()
    done = False
    total_reward = 0

    # Training loop with a maximum of 10 episodes or until approximately 10 inputs are received
    episode = 0
    while not done and episode < 10:
        # Exploration-exploitation trade-off
        if np.random.rand() < epsilon:
            # Explore - randomly select a VARK preference as action
            action = np.random.choice(list(VARK_mapping.keys()))
        else:
            # Exploit - select the VARK preference with the highest Q-value
            action = np.argmax(cumulative_Q_values[state, :])

        # Display iteration and episode information
        print(f"Iteration: {iteration + 1}, Episode: {episode + 1}, Testing: {VARK_mapping[action]}")

        # Input grade from the user
        grade = float(input("Enter grade (between 0 and 1): "))

        # Taking the chosen action and observing the new state
        new_state, done = env.step(action, grade)

        # Update cumulative Q-values
        cumulative_Q_values[state, action] = (1 - alpha) * cumulative_Q_values[state, action] + alpha * (
                grade + gamma * np.max(cumulative_Q_values[new_state, :]))

        # Updating state and total reward
        state = new_state
        episode += 1

    # Decay exploration-exploitation trade-off
    epsilon = epsilon * np.exp(-epsilon_decay * episode)

    # Evaluate the agent (only once at the end of training)
    test_total_rewards = []
    test_episode = 0

    # Testing loop until approximately 10 inputs are received
    while not done and test_episode < 10:
        # Exploit - select the VARK preference with the highest Q-value
        action = np.argmax(cumulative_Q_values[state, :])

        # Display iteration and testing episode information
        print(f"Iteration: {iteration + 1}, Testing Episode: {test_episode + 1}, Testing: {VARK_mapping[action]}")

        # Input grade from the user during evaluation
        grade = float(input("Enter grade (between 0 and 1): "))

        new_state, done = env.step(action, grade)
        state = new_state
        total_reward += grade
        test_episode += 1

    # Handle the case where no testing episodes are completed
    avg_test_reward = total_reward / test_episode if test_episode > 0 else 0
    print(f"Iteration: {iteration + 1}, Average Test Reward: {avg_test_reward}")

    # Select the most suitable VARK method based on the cumulative Q-values for all iterations
    most_suitable_method = VARK_mapping[np.argmax(np.mean(cumulative_Q_values, axis=0))]
    print(f"Most Suitable VARK Method (Cumulative): {most_suitable_method}")

    # Adjust suitable content percentage based on Q-learning results
    if final_output == most_suitable_method:
        suitable_content_percentage = min(70, suitable_content_percentage + 10)
    else:
        suitable_content_percentage = max(0, suitable_content_percentage - 10)

    # Update final output
    final_output = most_suitable_method

    # Increment iteration counter
    iteration += 1