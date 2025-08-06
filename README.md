# P4 Testbed
This repository provides a learning environment to deepen your understanding of P4-related tools through hands-on execution.

**Containerlab** is leveraged for data plane construction, enabling verification across various network topologies.


## Getting Started
```bash
git clone --recursive https://github.com/hatahataY/P4.git
```
After cloning, please apply the necessary patch. This step is crucial due to the use of an Alpine-based image.
```bash
patch -p1 < diff
```


## Using the Testbed
The testbed operates within a containerlab container, providing a custom clab command-line tool to manage your experiments.
### Starting the Containerlab Environment
First, bring up the Containerlab environment using Docker Compose.
```bash
docker compose dev up -d
```
### Connecting to the Console
```bash
docker compose exec containerlab /bin/bash
```
#### `clab` Command Usage
Once inside the containerlab console, you can use the clab command for various operations:
* `clab start`: Initiates the network experiment based on the topology defined in `topo.clab.yml`. This file specifies the network topology, and the necessary source code for experiment nodes is located in the repos directory. The build process for these nodes is described in `build_configs.py`.
* `clab stop`: Terminate the currently running network experiment.
* `clab image build`: Builds the container images required for the experiment nodes.
* `clab image rm`: Removes the container images associated with the experiment nodes.

### Stopping the Containerlab Environment
To stop the entire Containerlab environment:
```bash
docker compose dev down
```
To remove the images as well, use the `--rmi all` option:
```bash
docker compose dev down --rmi all
```