# fillthetank
A two-player strategic flow allocation game designed for researchers and engineers to explore decision-making under shared resource constraints.

# Fill the Tank: A Strategic Flow Allocation Game

**Fill the Tank** is a discrete-time, two-player strategy game where players aim to fill their tanks to predefined target volumes using shared flow resources. Players act simultaneously at each time step, adjusting their tap levels while adhering to individual and global flow constraints. The game invites the study of decentralized control, resource competition, and game-theoretic strategy design.

## 🎯 Objective
Each player tries to reach their target volume in the minimum number of steps, without exceeding shared flow capacity. The game ends in success if both targets are exactly met, or failure if either player overshoots.

## 🧠 Research Focus
This game serves as a testbed for:
- Developing and benchmarking decision strategies
- Game-theoretic analysis of competitive/cooperative resource use
- Studying adaptive behavior under limited information

## 📦 Contents
- `game.py`: Core game logic and simulation environment
- `strategies/`: Baseline and user-submitted strategies
- `benchmark.py`: Script to compute cumulative scores over a grid of target values
- `README.md`: Description and instructions

## 🚀 How to Use
Run simulations with different strategies or modify the game logic for your research:

```bash
python game.py
