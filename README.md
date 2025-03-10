# Adding Robustness and Confidence to Your Code through Automated Testing

## Setup

Set up your conda environment:

```
conda env create -f environment.yml -p ./venv
```

Activate the Environment and Finish Setting Up the Internal Tools

```
conda activate ./venv
python -m ipykernel install --name testing
pip install -e .
```

Check that the Pytest Runner is Working:

```
pytest
```


## Exercise 1: Test our Spike Math utilities

**Instructions:**  The `spike_math.py` module has some functions that seem to work, but don't seem very clear.  Working in the `test_spike_utils.py` module function-by-function, add pytest tests that check the function's behavior with test data.
  - Note: The module is written to be compatible with VSCode's Interactive mode.  Feel free to run individual blocks to get a sense of how they work!



## Exercise 2: Improving the Code through Debugging and Tests

**Instructions**:  Improve the function's behavior, using the python debugger and PyTest functions!

