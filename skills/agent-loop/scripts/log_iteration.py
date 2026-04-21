#!/usr/bin/env python3
import argparse
import os
from datetime import datetime

def log_iteration(iteration, message, log_file="AGENT_LOOP_LOG.md"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"## Iteration {iteration} - {timestamp}\n"
    
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("# Agent Loop Log\n\n")
            f.write("This file tracks the progress of the agent loop.\n\n")

    with open(log_file, "a") as f:
        f.write(header)
        f.write(f"{message}\n\n")
        f.write("---\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log an agent loop iteration.")
    parser.add_argument("--iteration", required=True, help="Iteration number or ID")
    parser.add_argument("--msg", required=True, help="Message describing what was done")
    parser.add_argument("--file", default="AGENT_LOOP_LOG.md", help="Path to the log file")
    
    args = parser.parse_args()
    log_iteration(args.iteration, args.msg, args.file)
    print(f"Logged iteration {args.iteration} to {args.file}")
