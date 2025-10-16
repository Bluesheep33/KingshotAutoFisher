# Kingshot Fishing Event Automation Script
### This script automates fishing attempts in the Kingshot fishing event by dodging obstacles, registering catches, and optimizing the catch based on user priorities.
<br>

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install required libraries:
    ```bash
    pip install
    ```
3. Download the script and save it to your desired directory.
4. Run the script using:
    ```bash
    python src/main.py
    ```
<br>

## Configuration
- Open `user_config.env` to set your stats and preferences for the fishing event.


## Usage
Follow the prompts in the terminal to start an automated fishing attempt. The script will handle the rest, including dodging obstacles and optimizing catches.

## (Will be implemented) Features
- **Obstacle Dodging**: The script intelligently navigates around obstacles to reach maximum depth.
- **Catch Registration**: All fishes, mermaids, chests, and items are registered during descent.
- **Optimal Catch Calculation**: Based on user-defined priorities, the script calculates the best items
- **Catch Execution**: The script catches the optimal items while avoiding unwanted ones during ascent.
- **Pause Functionality**: If an unwanted item is caught, if the ascent begins prematurely, or if no new mermaids are found while the new mermaid priority is selected then the script will pause the attempt.

## (Could be implemented) Additional Features
- **Guidebook Tracking**: Automatically monitor and log progress of the fishing guidebook.
- **Multiple Attempt Handling**: Manage multiple fishing attempts in a single session.
- **Graphical User Interface (GUI)**: A user-friendly interface for easier configuration and control.
- **Improved Algorithms**: Enhanced algorithms for better obstacle avoidance and catch optimization.