from processor import DataPreprocessor

processor = DataPreprocessor("data/sample_input.txt")
processor.process()

users, avg_clicks = processor.summarize()
processor.save_output("data/clean_output.txt")

print(f"Users: {users}, Avg Clicks: {avg_clicks}")

