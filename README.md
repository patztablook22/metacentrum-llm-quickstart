# A quickstart LLM project for Metacentrum

Minimal project structure to get LLMs runnign on Metacentrum.

## Usage
1. clone the repository in any Metacentrum frontend
2. change the `PROJECT` variable in `pbs/batch` **!!!**
3. modify the source under `/src`
4. `qsub` the `pbs/batch` file manually or automatically using `bin/run-batch`

## Notes
- `requirements.txt` contains the necessary dependencies to run Huggingface models with accelerated Torch (in my experience, Tensorflow is incomparably more painful to work with). You will probably need more things (`sklearn`, ...), feel free to add them here.
- Do not change the PBS modules included in `pbs/batch` unless you want to experience existential dread.
- Metacentrum often has technical errors which are not your fault. First [check](https://docs.e-infra.cz/compute/grid/) you are not doing something stupid, then contact the [support](mailto:meta@cesnet.cz). They are quick to respond, don't worry.

## Example src

The example `src/main.py` uses GPT2 to rickroll you (prompt in italics):

> _Never gonna give you up, never gonna let you down, never gonna run around and_ \
> **desert you.**
