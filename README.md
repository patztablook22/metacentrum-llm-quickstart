# A quickstart LLM project for Metacentrum

Minimal project structure to get LLMs running on Metacentrum.

## Usage
1. Clone the repository in any Metacentrum frontend.
2. Change the `PROJECT` variable in `pbs/batch` **!!!**
3. Modify the source under `src`.
4. Submit the job using `bin/run-batch` (or manually using `qsub pbs/batch` with adequate parameters).
5. Configure the resources requested by modifying `bin/run-batch`. E.g. you may need to increase `gpu_mem`.

## Notes
- `requirements.txt` contains the necessary dependencies to run Huggingface models with accelerated Torch (in my experience, Tensorflow is incomparably more painful to work with). You will probably need more things (`sklearn`, ...), feel free to add them here.
- Do not change the PBS modules included in `pbs/batch` unless you want to experience existential dread.
- Metacentrum often has technical errors which are not your fault. First [check](https://docs.e-infra.cz/compute/grid/) you are not doing something stupid, then contact the [support](mailto:meta@cesnet.cz). They are quick to respond, don't worry.

## Example src

The example `src/main.py` uses GPT2 to rickroll you (prompt in italics):

> _Never gonna give you up, never gonna let you down, never gonna run around and_ \
> **desert you.**
