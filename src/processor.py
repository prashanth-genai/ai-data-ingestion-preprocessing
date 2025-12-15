import copy

class DataPreprocessor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.cleaned_data = []

    def read_data(self):
        try:
            with open(self.file_path, "r") as file:
                lines = file.readlines()
            return lines
        except FileNotFoundError:
            print("File not found")
            return []

    def clean_record(self, record):
        try:
            user_id, age, country, clicks = record.strip().split(",")

            age = int(age)
            clicks = int(clicks)

            return {
                "user_id": user_id.strip(),
                "age": age,
                "country": country.strip().lower(),
                "clicks": clicks
            }

        except ValueError:
            return None

    def process(self):
        records = self.read_data()

        for record in records:
            cleaned = self.clean_record(record)
            if cleaned:
                self.cleaned_data.append(cleaned)

    def summarize(self):
        total_users = len(self.cleaned_data)
        total_clicks = sum(user["clicks"] for user in self.cleaned_data)

        avg_clicks = total_clicks / total_users if total_users else 0

        return total_users, avg_clicks

    def save_output(self, output_file):
        with open(output_file, "w") as file:
            for user in self.cleaned_data:
                file.write(f"{user}\n")


# ===== EXECUTION =====

processor = DataPreprocessor("raw_data.txt")
processor.process()

users, avg_clicks = processor.summarize()
processor.save_output("clean_data.txt")

print(f"Users: {users}, Avg Clicks: {avg_clicks}")

