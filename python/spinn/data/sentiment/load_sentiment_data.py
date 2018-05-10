from spinn import util

NUM_CLASSES = 2

SENTENCE_PAIR_DATA = False
FIXED_VOCABULARY = None

LABEL_MAP = {
    "0": 0,
    "1": 1,
}

def convert_binary_bracketed_data(filename):
    examples = []
    with open(filename, 'r') as f:
        for line in f:
            example = {}
            line = line.strip()
            tab_split = line.split('\t')
            example["label"] = tab_split[0]
            example["sentence"] = tab_split[1]
            example["tokens"] = []
            example["transitions"] = []

            for word in example["sentence"].split(' '):
                if word != "(":
                    if word != ")":
                        example["tokens"].append(word)
                    example["transitions"].append(1 if word == ")" else 0)

            example["example_id"] = str(len(examples))

            examples.append(example)
    return examples

def load_data(path,
        vocabulary=None,
        seq_length=None,
        batch_size=32,
        eval_mode=False,
        logger=None):
    dataset = convert_binary_bracketed_data(path)
    return dataset


if __name__ == "__main__":
    # Demo:
    examples = convert_binary_bracketed_data('bl-data/bl_dev.tsv')
    print(examples[0])
