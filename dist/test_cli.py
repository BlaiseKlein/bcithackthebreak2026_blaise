#!/usr/bin/env python3
# nettool.py
import sys

def main():
    print("Welcome to APPNAMEWOW.")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "ping":
            host = input("Enter host to ping: ").strip()
            print(f"erm. . . fake pinging to ping {host}...")
        elif cmd in ("exit", "quit"):
            print("Exiting NetTool.")
            sys.exit(0)
        else:
            print("Unknown command. Available: ping")

if __name__ == "__main__":
    main()