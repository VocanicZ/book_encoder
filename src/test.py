import subprocess

def generate_story_with_ollama(nouns: list[str]) -> str:
    prompt = (
        "\
            Create a single surreal, poetic, yet coherent paragraph using the following list of nouns in the exact order they appear.\n\
            You must use each noun only once, and in the given order.\n\
            Do not add any nouns not in the list. You may use verbs, adjectives, and prepositions freely.\n\
            Each noun must be part of a grammatically correct sentence. The resulting paragraph should feel like a strange, literary narrative or academic prose.\n\
            Nouns (in order):\n\n"
            + ", ".join(nouns) + "\n\nBegin your paragraph now:"
    )
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

nouns = [
    "extension", "Monthly amount", "Kyrgyzstan", "orthopsychopedia", "migration flows", "air layer", 
    "polysulfones", "miersite", "consumption", "divestment", "Boilers", "Received", "relapsing", 
    "badger", "rasades", "tif", "melanodermite", "enterovirus", "Catholics", "colopexia", "shekels", 
    "spart", "accordors", "Summer scarf", "paleophytogeography", "pick", "Khasis", "panosse", 
    "placoderms", "watt hour", "Sirupous voice", "psychosurgery", "Ecolaters", "supervised child", 
    "laying", "avalanche bitch", "nemopode", "Oxanes", "clitics", "Clubist"
]

print(generate_story_with_ollama(nouns))