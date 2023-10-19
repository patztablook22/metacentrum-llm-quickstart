import sys
import numpy as np
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel



def main(args):
    project = args[1]
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2-xl")
    model = GPT2LMHeadModel.from_pretrained("gpt2-xl")

    prompt = "Never gonna give you up, never gonna let you down, never gonna run around and"

    inputs = tokenizer([prompt], return_tensors='pt')
    output_ids = model.generate(**inputs)
    response = tokenizer.decode(output_ids[0])
    print(response)


if __name__ == '__main__':
    main(sys.argv)
