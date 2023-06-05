import datetime

def write_log(log_message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {log_message}"
    print(log_entry)

def transfer_funds(sender, recipient, amount):
    # Perform the funds transfer
    # ...

    log_message = {
        "action" : "transfer",
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    write_log(log_message)

# Usage:
sender = "user123"
recipient = "user456"
amount = 100.0
transfer_funds(sender, recipient, amount)
