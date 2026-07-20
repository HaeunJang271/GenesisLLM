
from transformers import AutoTokenizer


def get_tokenizer(
    model_name="gpt2"
):

    tokenizer = AutoTokenizer.from_pretrained(
        model_name
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    return tokenizer
