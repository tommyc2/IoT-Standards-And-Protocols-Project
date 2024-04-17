#!/bin/bash
# Cron job executes executes Twilio whatsapp notification script
# 10 15 */7 * * --> Every week at 3:10 on any day

import subprocess

output = subprocess.run("python3 twilio_whatsapp.py", shell=True, capture_output=True)

print(output.stdout)