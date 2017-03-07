import subprocess
import logging

log = logging.getLogger(__name__)

class XtraBackupBackup(object):
    command = "xtrabackup"

    def __init__(self, args, extra):
        self.args = args
        self.extra = extra

    @classmethod
    def parse_args(cls, subparsers):
        xtrabackup_parser = subparsers.add_parser(cls.command, description=cls.__doc__)

    def backup(self):
        log.info("starting XtraBackup backup...")

        cmd = ["xtrabackup", "--backup"] + self.extra

        try:
            self.result = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            log.info("output:\n\n\t%s", "\n\t".join(self.result.split("\n")))
            log.info("backup complete")

        except subprocess.CalledProcessError as e:
            self.result = e.output
            log.error("failed to back up XtraBackup database")
            log.error("return code was %s", e.returncode)
            log.error("output:\n\n\t%s", "\n\t".join(self.result.split("\n")))
            log.error("backup process failed")
            raise e
