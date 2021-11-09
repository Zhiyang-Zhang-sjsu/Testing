import openpyxl

from web_keywords.web_UI_keywords import WebUIKeywords

class ExeclTestDataManagement:
    def run_test_data(self, file, log):
        driver = {}
        excel = openpyxl.load_workbook(file)
        try:
            for name in excel.sheetnames:
                sheet = excel[name]
                log.info(f"************{name}************")
                for values in sheet.values:
                    if type(values[0]) is int:
                        data = {}
                        data["by"] = values[2]
                        data["value"] = values[3]
                        data["text"] = values[4]

                        for key in list(data.keys()):
                            if data[key] is None:
                                del data[key]

                        log.info(f"Running: {values[5]}")
                        if values[1] == "open browser":
                            keywords = WebUIKeywords(data['text'], log)
                        else:
                            res = getattr(keywords, values[1])(**data)
                            if values[1] == "get_driver":
                                driver[name] = res
        except Exception as e:
            log.exception(f"Exception: {e}")
        finally:
            excel.close()

        return driver

