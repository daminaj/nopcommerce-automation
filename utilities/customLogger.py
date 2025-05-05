import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_path = "./Logs"
        os.makedirs(log_path, exist_ok=True)  # Ensure the directory exists

        logger = logging.getLogger("automationLogger")
        logger.setLevel(logging.INFO)

        # Prevent adding handlers multiple times
        if not logger.handlers:
            file_handler = logging.FileHandler(f"{log_path}/automation.log", mode='a')
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger







# import logging #python default package
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename="./Logs/automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger