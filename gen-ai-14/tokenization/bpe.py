# BPE
from transformers import GPT2Tokenizer
# imports the GPT2Tokenizer class from the transformers module
# GPT-2 uses the byte pair encoding tokenizer algorithm

text = "NLP preprocessing transformers unstructured textual data effectively"
gpt2_tok = GPT2Tokenizer.from_pretrained("gpt2")
# pretrained GPT-2 model
gpt2_tokens = gpt2_tok.tokenize(text)
print('\n GPT-2 toTokens:', gpt2_tokens)
print('GPT Ids:', gpt2_tok.encode(text))
print('vocab sizes of gpt2:', gpt2_tok.vocab_size)