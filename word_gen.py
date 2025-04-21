#!/usr/bin/env python3

import argparse
import string
import os
import sys

PATTERN_HELP = """
Доступные шаблоны:
  i.s   → a.ivanov
  i_s   → a_ivanov
  is    → aivanov
  si    → ivanova
  s_i   → ivanov_a
  s.i   → ivanov.a
  s     → ivanov
"""

AVAILABLE_PATTERNS = {
    "i.s": lambda ch, s: f"{ch}.{s}",
    "i_s": lambda ch, s: f"{ch}_{s}",
    "is":  lambda ch, s: f"{ch}{s}",
    "si":  lambda ch, s: f"{s}{ch}",
    "s_i": lambda ch, s: f"{s}_{ch}",
    "s.i": lambda ch, s: f"{s}.{ch}",
    "s":   lambda ch, s: s,
}

def generate_usernames(surnames: list, patterns: list) -> dict:
    alphabet = string.ascii_lowercase
    result = {}

    for surname in surnames:
        surname = surname.strip().lower()
        if not surname:
            continue

        usernames = set()
        for ch in alphabet:
            for pattern in patterns:
                if pattern == "s":
                    usernames.add(AVAILABLE_PATTERNS[pattern](ch, surname))
                else:
                    usernames.add(AVAILABLE_PATTERNS[pattern](ch, surname))

        result[surname] = sorted(usernames)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Генератор логинов из списка фамилий по настраиваемым шаблонам.",
        epilog="Пример: python3 genword.py wordlists.txt -p i.s,is,s"
    )

    parser.add_argument("input_file", help="Путь к файлу со списком фамилий (по одной на строку)")
    parser.add_argument("-o", "--output", help="Путь для сохранения результата (по умолчанию — stdout)")
    parser.add_argument("-p", "--patterns", help="Список шаблонов через запятую (например: i.s,is,s)", default="i.s,i_s,is,si,s_i,s.i,s")
    parser.add_argument("--list-patterns", action="store_true", help="Показать все доступные шаблоны и выйти")

    args = parser.parse_args()

    if args.list_patterns:
        print(PATTERN_HELP)
        sys.exit(0)

    pattern_list = args.patterns.split(",")
    for p in pattern_list:
        if p not in AVAILABLE_PATTERNS:
            print(f"❌ Неизвестный шаблон: {p}")
            print(PATTERN_HELP)
            sys.exit(1)

    if not os.path.isfile(args.input_file):
        print(f"❌ Файл не найден: {args.input_file}", file=sys.stderr)
        sys.exit(1)

    with open(args.input_file, "r", encoding="utf-8") as f:
        surnames = f.readlines()

    usernames_dict = generate_usernames(surnames, pattern_list)

    output_lines = []
    for usernames in usernames_dict.values():
        output_lines.extend(usernames)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            for line in sorted(output_lines):
                f.write(line + "\n")
        print(f"[+] Сгенерировано {len(output_lines)} логинов. Сохранено в: {args.output}")
    else:
        for line in sorted(output_lines):
            print(line)


if __name__ == "__main__":
    main()

