from moonrush.scanner import Scanner


def main() -> None:
    source = 'cat "hello world"'
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    print(tokens)


if __name__ == "__main__":
    main()
