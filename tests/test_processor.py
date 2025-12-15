from src.processor import DataPreprocessor

def test_valid_record_processing(tmp_path):
    # create temporary input file
    input_file = tmp_path / "input.txt"
    input_file.write_text("u1,25,India,10\nu2,30,USA,20")

    processor = DataPreprocessor(str(input_file))
    processor.process()

    assert len(processor.cleaned_data) == 2
    assert processor.cleaned_data[0]["age"] == 25

def test_invalid_record_skipped(tmp_path):
    input_file = tmp_path / "input.txt"
    input_file.write_text("u1,abc,India,10")

    processor = DataPreprocessor(str(input_file))
    processor.process()

    assert len(processor.cleaned_data) == 0

