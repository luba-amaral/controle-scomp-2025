from backend.excel_handler import ExcelProcessor
from backend.data_processing import process_data # type: ignore
from backend.validations import validate_dates


def main():
    file_path = "2025 - PLANILHA CONTROLE SCOMP-2025.xlsx"

    # processamento de dados
    processor = ExcelProcessor(file_path)
    df = processor.calculate_days()
    df = validate_dates(df)
    df = process_data(df)

    # atualizar a planilha
    processor.add_data_validations()
    processor.update_fechamento_sheet(df)
    processor.save()

    print("Planilha atualizada!")


if __name__ == "__main__":
    main()
