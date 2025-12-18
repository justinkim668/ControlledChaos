# ControlledChaos
Non-Newtonian Temporal Narratives in Media.

# Installation/Use
1. Clone the repository and navigate to the root directory.
2. Create a virtual environment: `python -m venv .venv`
3. Activate the environment:
   - macOS/Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Configure `wide_time_chaotic.py`: Update `clip` and `final_clip` paths.
6. Run the script: `python wide_time_chaotic.py`

# Technical Summary
This script implements a non-linear temporal remapping algorithm. It iterates through the Logistic Map $x_{n+1} = rx_n(1 - x_n)$ where: $x_n$ controls the magnitude of the time shift that can be applied to generate motion effects at a given time in the context of this work (0.0 to 1.0), and $r$ is the control parameter ($1.0 < r \leq 4.0$).  Each value is then mapped to the source video's frame index, creating a deterministic but high-entropy reordering of temporal data.

# Future Work
Future work will focus on the following:
1. Optimize Logistic Map code for $O(N)$ time.
2. Port this Python logic over to GLSL fragment shaders.
3. Extend this logic to higher-dimensional chaotic maps like the Lorenz System.
