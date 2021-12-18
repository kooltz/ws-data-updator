from abc import ABCMeta, abstractmethod


class MessageHandler(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, message):
        pass

    @abstractmethod
    def post_process(self, process_result):
        pass

    def run(self, message):
        result = self.process(message)
        if result is not None:
            self.post_process(result)
