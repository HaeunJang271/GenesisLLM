from transformers import AutoTokenizer
from dataset import TextDataset

tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen2.5-0.5B"
)

dataset = TextDataset(
    tokenizer,
    BASE_DIR / "data" / "train.txt",
    block_size=128
)

print(len(dataset))

sample = dataset[0]

print(sample["input_ids"].shape)