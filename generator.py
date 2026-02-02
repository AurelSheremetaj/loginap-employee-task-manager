from datetime import datetime

class UniqueIdGenerator:
    
    @staticmethod
    def generate_id():
        now = datetime.now()
        unique_id = int(now.strftime("%S%f")[:15])
        return unique_id