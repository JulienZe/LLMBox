from .multiple_choice_dataset import MultipleChoiceDataset


class Anli(MultipleChoiceDataset):
    """The dataset of ANLI

    The Adversarial Natural Language Inference (ANLI,Nie Yixin,2020) is a new large-scale NLI benchmark dataset.

    Example:
        hypothesis: "Idris Sultan was born in the first month of the year preceding 1994.",
        label: 0,
        premise: "\"Idris Sultan (born January 1993) is a Tanzanian Actor and comedian, actor and radio host who won the Big Brother Africa-Hotshot...",
    """

    instruction = ""
    evaluation_set = "dev_r2"
    example_set = "train_r2"
    load_args = ("anli",)

    def format_instance(self, instance):
        source = (
            instance["premise"] + "\nQuestion: " + instance["hypothesis"] + " True, False, or Neither?"
        )

        label2text = {0: " True", 1: " Neither", 2: " False"}

        options = [label2text[option] for option in [0, 1, 2]]
        return dict(
            source=source,
            source_postfix="\nAnswer:",
            target_idx=instance["label"],
            options=options,
        )

    @property
    def references(self):
        return [instance["label"] for instance in self.evaluation_data]
