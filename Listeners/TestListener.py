import os.path
import tempfile
from datetime import datetime


class TestListener:

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, filename=f'Validation and Verification Report {datetime.now().strftime("%d_%m_%Y")}.txt'):
        # outpath = os.path.join(os.getcwd(), 'Reports\\', filename)
        outpath = os.path.join('/opt/robotframework/reports', filename)  # <--- this save the val / ver report with other reports when using the docker image
        self.outfile = open(outpath, 'w')

    def start_suite(self, name, attrs):
        if name == attrs['longname']:
            self.outfile.write('------------------------------------------ \n')
            self.outfile.write(f'               {name.upper()}             \n')
            self.outfile.write('------------------------------------------ \n\n')
        else:
            self.outfile.write('------------------------------------------ \n')
            self.outfile.write(f'                   {name.upper()}         \n')
            self.outfile.write('------------------------------------------ \n')

    def start_test(self, name, attrs):
        return

    def end_test(self, name, attrs):
        for VER in attrs['originalname'].replace(", ", " ").split():
            self.outfile.write(f'- {VER}    ')
            self.outfile.write(f'{attrs["status"]} at: {datetime.now().strftime("%d/%m/%Y, %H:%M:%S%p" )}\n')

    def end_suite(self, name, attrs):
        if name == attrs['longname']:
            self.outfile.write(f'------------------------------------------                                     \n')
            self.outfile.write(f' {name.upper()} {attrs["status"]} at: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n')
            self.outfile.write(f'------------------------------------------                                   \n\n')
        else:
            self.outfile.write(f'------------------------------------------                                     \n')
            self.outfile.write(f'     {name.upper()} {attrs["status"]} at: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n')
            self.outfile.write(f'------------------------------------------                                   \n\n')

    def close(self):
        self.outfile.close()
