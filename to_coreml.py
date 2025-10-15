from rfdetr import RFDETRSegPreview


if __name__ == "__main__":
    model = RFDETRSegPreview()
    model.export_coreml(output_dir="output")
