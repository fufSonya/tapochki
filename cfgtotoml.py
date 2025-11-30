import argparse
from src.parser import Parser
import toml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True, help='Путь для TOML')
    args = parser.parse_args()

    text = input()
    value = Parser(text).parse()

    with open(args.out, 'w', encoding='utf-8') as f:
        toml.dump({'root': value}, f)

if __name__ == "__main__":
    main()
