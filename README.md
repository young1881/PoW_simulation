# Proof of Work (PoW) Blockchain Simulation

This Python program simulates a PoW blockchain network with various nodes, measures the blockchain's growth rate, and evaluates the impact of malicious nodes and attacks on the network.

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [Parameters](#parameters)
- [Simulations](#simulations)
  - [1. Blockchain Growth Rate](#1-blockchain-growth-rate)
  - [2. Malicious Node Fork Attacks](#2-malicious-node-fork-attacks)
  - [3. Selfish Mining Revenue](#3-selfish-mining-revenue)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a Python simulation program to model a PoW blockchain network. It allows you to customize the number of nodes, the success rate of block generation, and the presence of malicious nodes. You can use this simulation to study the growth rate of the blockchain and assess the impact of malicious nodes, including fork attacks and selfish mining.

## Usage
To run the PoW blockchain simulation, execute the main script:

```python .\main.py```

The mining process and result will be output in `\log`

## Parameters
You can customize the following parameters in the main.py script:

 - Number of nodes
 - Number of malicious nodes
 - Success rate of block generation (defined as the leading zeros of block hash value)

## Simulations
### 1. Blockchain Growth Rate
This simulation measures the growth rate of the blockchain based on the specified parameters.

### 2. Malicious Node Fork Attacks
This simulation introduces a certain number of malicious nodes and measures the length of successful fork attacks. Run the simulation for different proportions of malicious nodes (e.g., 10%-40%) to assess their impact on the network.

### 3. Selfish Mining Revenue
Evaluate the proportion of revenue gained from selfish mining under different proportions of malicious nodes.

## Contributing
Contributions to this project are welcome. If you have suggestions, bug reports, or would like to add new features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.