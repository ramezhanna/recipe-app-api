from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def process_log_record(self, log_record):
        # Rename fields
        if 'levelname' in log_record:
            log_record['level'] = log_record.pop('levelname')
        if 'name' in log_record:
            log_record['app_module'] = log_record.pop('name')
        return super().process_log_record(log_record)
