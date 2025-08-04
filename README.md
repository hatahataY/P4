# P4 Testbed
This repository provides a learning environment to deepen your understanding of P4-related tools through hands-on execution.

**Containerlab** is leveraged for data plane construction, enabling verification across various network topologies. This testbed supports two primary modes:

* **Developer Mode**: An environment for building tools from source code, particularly those requiring compilation.
* **Experiment Mode**: An environment for network setup and experimentation using Containerlab.

---

## Getting Started
```bash
git clone --recursive https://github.com/hatahataY/P4.git
```

---

## Developer Mode
This mode is designed for building and developing P4-related tools directly from source.
### Starting the Container
```bash
docker compose dev up -d
```
### Connecting to the Console
```bash
docker compose exec dev /bin/bash
```
### Stopping the Container
```bash
docker compose dev down
```
To remove the image as well, use the `--rmi all` option:
```bash
docker compose dev down --rmi all
```

---

## Experiment Mode
In Experiment Mode, you can build arbitrary networks using the tools compiled in Developer Mode. Network construction is facilitated by Containerlab, with topologies and execution commands defined in `topo-clab.yml`.
### Starting the Container
```bash
docker compose up -d
```
### Connecting to the Console
```bash
docker compose exec containerlab /bin/bash
```
### Stopping the Container
```bash
docker compose down
```
To remove the image as well, use the `--rmi all` option:
```bash
docker compose down --rmi all
```