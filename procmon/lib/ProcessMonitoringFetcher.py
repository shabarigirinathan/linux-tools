# Project : ProcMon - Process Monitoring
# Platform : Linux
# Developer : Giri
# Version : 0.0.1
# Python 2.7.13
# Dependency psutil, mysqldb

import psutil
import datetime


class ProcessMonitoringFetcher(object):

    _piddictlist = {}

    def q_fetch_process_info(self, pidn):
        # Tuple Order
        # 1. Parent Process ID
        # 2. Username
        # 3. Process Name
        # 4. Process Base-command
        # 5. Process Other-command(s)
        # 6. CPU Percentage
        # 7. Create Time
        # 8. Monitoring Instance Date
        # 9. Monitoring Instance Time
        # 10. Parent/Descendants Count
        # 11. Read Count
        # 12. Read Bytes
        # 13. Write Count
        # 14. Write Bytes
        # 15. Memory Percentage
        # 17. CTX Switch Voluntary
        # 18. CTX Switch Involuntary
        # 19. Threads
        # 20. File descriptor
        # 21. Open Files
        # 22. Status
        # 23. Connections

        self._piddictlist = {}
        proc = _proc_fetcher(pidn)
        piddetails = []
        piddetails.append(proc.get_proc_ppid())
        piddetails.append(proc.get_proc_username())
        piddetails.append(proc.get_proc_name())
        piddetails.append(proc.get_proc_basecmd())
        piddetails.append(proc.get_proc_othercmd())
        piddetails.append(proc.get_proc_cpu_percent())
        piddetails.append(proc.get_proc_create_time())
        piddetails.append(proc.get_proc_mon_time())
        piddetails.append(proc.get_proc_mon_date())
        piddetails.append(proc.get_proc_ppid_count())
        piddetails.append(proc.get_proc_read_count())
        piddetails.append(proc.get_proc_read_bytes())
        piddetails.append(proc.get_proc_write_count())
        piddetails.append(proc.get_proc_write_bytes())
        piddetails.append(proc.get_proc_memory_percent())
        piddetails.append(proc.get_proc_ctx_voluntary())
        piddetails.append(proc.get_proc_ctx_involuntary())
        piddetails.append(proc.get_proc_threads())
        piddetails.append(proc.get_proc_num_fds())
        piddetails.append(proc.get_proc_open_files())
        piddetails.append(proc.get_proc_status())
        piddetails.append(proc.get_proc_connections())
        self._piddictlist[pidn] = piddetails
        return self._piddictlist

    def fetch_process_info(self):
        self._piddictlist = {}
        pidlist = psutil.pids()
        for pidn in pidlist:
            proc = _proc_fetcher(pidn)
            piddetails = []
            piddetails.append(proc.get_proc_ppid())
            piddetails.append(proc.get_proc_username())
            piddetails.append(proc.get_proc_name())
            piddetails.append(proc.get_proc_basecmd())
            piddetails.append(proc.get_proc_othercmd())
            piddetails.append(proc.get_proc_cpu_percent())
            piddetails.append(proc.get_proc_create_time())
            piddetails.append(proc.get_proc_mon_date())
            piddetails.append(proc.get_proc_mon_time())
            piddetails.append(proc.get_proc_ppid_count())
            piddetails.append(proc.get_proc_read_count())
            piddetails.append(proc.get_proc_read_bytes())
            piddetails.append(proc.get_proc_write_count())
            piddetails.append(proc.get_proc_write_bytes())
            piddetails.append(proc.get_proc_memory_percent())
            piddetails.append(proc.get_proc_ctx_voluntary())
            piddetails.append(proc.get_proc_ctx_involuntary())
            piddetails.append(proc.get_proc_threads())
            piddetails.append(proc.get_proc_num_fds())
            piddetails.append(proc.get_proc_open_files())
            piddetails.append(proc.get_proc_status())
            piddetails.append(proc.get_proc_connections())
            self._piddictlist[pidn] = piddetails
        return self._piddictlist


class _proc_fetcher(object):


    _proc_ppid = []
    _proc_username = []
    _proc_name = []
    _proc_basecmd = []
    _proc_othercmd = []
    _proc_cpu_percent = []
    _proc_create_time = []
    _proc_mon_date = []
    _proc_mon_time = []
    _proc_ppid_count = []
    _proc_read_count = []
    _proc_read_bytes = []
    _proc_write_count = []
    _proc_write_bytes = []
    _proc_memory_percent = []
    _proc_ctx_voluntary = []
    _proc_ctx_involuntary = []
    _proc_threads = []
    _proc_num_fds = []
    _proc_open_files = []
    _proc_status = []
    _proc_connections = []
    _error_flag = "N"
    _error_code = 0

    def __init__(self, procid):
        self._proc_ppid = self._fetch_proc_ppid(procid)
        self._proc_username = self._fetch_proc_username(procid)
        self._proc_name =  self._fetch_proc_name(procid)
        self._proc_basecmd = self._fetch_proc_basecmd(procid)
        self._proc_othercmd = self._fetch_proc_othercmd(procid)
        self._proc_cpu_percent = self._fetch_proc_cpu_percent(procid)
        self._proc_create_time = self._fetch_proc_create_time(procid)
        mondtnow = datetime.datetime.now()
        self._proc_mon_date = mondtnow.date()
        self._proc_mon_time = mondtnow.time()
        self._proc_ppid_count = self._fetch_proc_ppid_count(procid)
        self._proc_read_count = self._fetch_proc_read_count(procid)
        self._proc_read_bytes = self._fetch_proc_read_bytes(procid)
        self._proc_write_count = self._fetch_proc_write_count(procid)
        self._proc_write_bytes = self._fetch_proc_write_bytes(procid)
        self._proc_memory_percent = self._fetch_proc_memory_percent(procid)
        self._proc_ctx_voluntary = self._fetch_proc_ctx_voluntary(procid)
        self._proc_ctx_involuntary = self._fetch_proc_ctx_involuntary(procid)
        self._proc_threads = self._fetch_proc_threads(procid)
        self._proc_num_fds = self._fetch_proc_num_fds(procid)
        self._proc_open_files = self._fetch_proc_open_files(procid)
        self._proc_status = self._fetch_proc_status(procid)
        self._proc_connections = self._fetch_proc_connections(procid)

    def _fetch_proc_ppid(self, procid):
        try:
            proc_ppid = psutil.Process(procid).ppid()
            return proc_ppid
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_username(self, procid):
        try:
            proc_username = psutil.Process(procid).username()
            return proc_username
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_name(self, procid):
        try:
            proc_name = psutil.Process(procid).name()
            return proc_name
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_basecmd(self, procid):
        try:
            if len(psutil.Process(procid).cmdline()) > 0:
                proc_basecmd = psutil.Process(procid).cmdline()[0]
            else:
                proc_basecmd = psutil.Process(procid).cmdline()
            return proc_basecmd
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_othercmd(self, procid):
        try:
            proc_othercmd = psutil.Process(procid).cmdline()[1:]
            return proc_othercmd
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_cpu_percent(self, procid):
        try:
            proc_cpu_percent = psutil.Process(procid).cpu_percent()
            return proc_cpu_percent
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_create_time(self, procid):
        try:
            proc_create_time = psutil.Process(procid).create_time()
            return proc_create_time
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_ppid_count(self, procid):
        try:
            proc_ppid_count = 0
            cpid = procid
            while True:
                if cpid != 0:
                    if psutil.Process(cpid).ppid() != 1 or psutil.Process(cpid).ppid() != 0:
                        proc_ppid_count = proc_ppid_count + 1
                        cpid = psutil.Process(cpid).ppid()
                    else:
                        break
                else:
                    break
            return proc_ppid_count
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_read_count(self, procid):
        try:
            proc_read_count = psutil.Process(procid).io_counters().read_count
            return proc_read_count
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_read_bytes(self, procid):
        try:
            proc_read_bytes = psutil.Process(procid).io_counters().read_bytes
            return proc_read_bytes
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_write_count(self, procid):
        try:
            proc_write_count = psutil.Process(procid).io_counters().write_count
            return proc_write_count
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []
    
    def _fetch_proc_write_bytes(self, procid):
        try:
            proc_write_bytes = psutil.Process(procid).io_counters().write_bytes
            return proc_write_bytes
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_memory_percent(self, procid):
        try:
            proc_memory_percent = psutil.Process(procid).memory_percent()
            return proc_memory_percent
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_ctx_voluntary(self, procid):
        try:
            proc_ctx_voluntary = psutil.Process(procid).num_ctx_switches().voluntary
            return proc_ctx_voluntary
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_ctx_involuntary(self, procid):
        try:
            proc_ctx_involuntary = psutil.Process(procid).num_ctx_switches().involuntary
            return proc_ctx_involuntary
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_threads(self, procid):
        try:
            proc_threads = psutil.Process(procid).threads()
            return proc_threads
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_num_fds(self, procid):
        try:
            proc_num_fds = psutil.Process(procid).num_fds()
            return proc_num_fds
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_open_files(self, procid):
        try:
            proc_open_files = psutil.Process(procid).open_files()
            return proc_open_files
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_status(self, procid):
        try:
            proc_status = psutil.Process(procid).status()
            return proc_status
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _fetch_proc_connections(self, procid):
        try:
            proc_connections = psutil.Process(procid).connections()
            return proc_connections
        except (EnvironmentError, psutil.Error) as err:
            self._set_error_flag("Y")
            self._set_error_code("1")
            if type(err) is psutil.AccessDenied:
                self._set_error_code("9")
        return []

    def _set_error_flag(self, flag):
        self._error_flag = flag
        
    def _set_error_code(self, code):
        self._error_code = code
        
    def get_proc_ppid(self):
        return self._proc_ppid

    def get_proc_username(self):
        return self._proc_username

    def get_proc_name(self):
        return self._proc_name

    def get_proc_basecmd(self):
        return self._proc_basecmd

    def get_proc_othercmd(self):
        return self._proc_othercmd

    def get_proc_cpu_percent(self):
        return self._proc_cpu_percent

    def get_proc_create_time(self):
        return self._proc_create_time

    def get_proc_mon_date(self):
        return self._proc_mon_date

    def get_proc_mon_time(self):
        return self._proc_mon_time

    def get_proc_ppid_count(self):
        return self._proc_ppid_count

    def get_proc_read_count(self):
        return self._proc_read_count

    def get_proc_read_bytes(self):
        return self._proc_read_bytes

    def get_proc_write_count(self):
        return self._proc_write_count

    def get_proc_write_bytes(self):
        return self._proc_write_bytes

    def get_proc_memory_percent(self):
        return self._proc_memory_percent

    def get_proc_ctx_voluntary(self):
        return self._proc_ctx_voluntary

    def get_proc_ctx_involuntary(self):
        return self._proc_ctx_involuntary

    def get_proc_threads(self):
        return self._proc_threads

    def get_proc_num_fds(self):
        return self._proc_num_fds

    def get_proc_open_files(self):
        return self._proc_open_files

    def get_proc_status(self):
        return self._proc_status

    def get_proc_connections(self):
        return self._proc_connections