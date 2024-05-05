import threading
import time

class Participant:
    def __init__(self, name):
        self.name = name
        self.prepared = False

    def prepare(self, transaction_id):
        print(f"{self.name}: Prepared for transaction {transaction_id}")
        self.prepared = True

    def commit(self, transaction_id):
        print(f"{self.name}: Committed transaction {transaction_id}")

    def abort(self, transaction_id):
        print(f"{self.name}: Aborted transaction {transaction_id}")

class TwoPhaseCommitCoordinator:
    def __init__(self, participants):
        self.participants = participants

    def start_transaction(self, transaction_id):
        for participant in self.participants:
            participant.prepare(transaction_id)

        for participant in self.participants:
            if participant.prepared:
                participant.commit(transaction_id)
            else:
                participant.abort(transaction_id)

if __name__ == "__main__":
    participant1 = Participant("Participant 1")
    participant2 = Participant("Participant 2")
    participant3 = Participant("Participant 3")
    coordinator = TwoPhaseCommitCoordinator([participant1, participant2, participant3])
    transaction_id = "12345"
    threading.Thread(target=coordinator.start_transaction, args=(transaction_id,)).start()
    time.sleep(2)