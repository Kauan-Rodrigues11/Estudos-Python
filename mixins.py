from pathlib import Path

class Log():
    def _log(self, msg):
        raise NotImplementedError('implemente o metodo log')
    
    def log_error(self, msg):
        return self._log(f'error: {msg}')
    
    def log_succes(self, msg):
        return self._log(f'succes: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        file_path = Path(__file__).parent / 'logfile.txt'
        msg_formatada = f'{msg}'
        with open(file_path, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)

lp = LogPrintMixin()
lp.log_succes('logado com sucesso.')

lf = LogFileMixin()
lf.log_succes('logado com sucesso.')

