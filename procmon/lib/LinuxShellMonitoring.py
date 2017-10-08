# Project : ProcMon - Process Monitoring
# Platform : Linux
# Developer : Giri
# Version : 0.0.1
# Python 2.7.13
# Dependency psutil, mysqldb

import os
import curses
import ProcessMonitoringFetcher
import prettytable
import time
import signal

def refresh_monitoring():
    # Tuple Order
    # 0. Parent Process ID
    # 1. Username
    # 2. Process Name
    # 3. Process Base-command
    # 4. Process Other-command(s)
    # 5. CPU Percentage
    # 6. Create Time
    # 7. Monitoring Instance Date
    # 8. Monitoring Instance Time
    # 9. Parent/Descendants Count
    # 10. Read Count
    # 11. Read Bytes
    # 12. Write Count
    # 13. Write Bytes
    # 14. Memory Percentage
    # 15. CTX Switch Voluntary
    # 16. CTX Switch Involuntary
    # 17. Threads
    # 18. File descriptor
    # 19. Open Files
    # 20. Status
    # 21. Connections

    make_base_calls()
    proc_mon_fetch = ProcessMonitoringFetcher.ProcessMonitoringFetcher()
    process_query_dict = proc_mon_fetch.fetch_process_info()
    if curses.can_change_color():
        column_length = curses.tigetnum("cols")
        row_length = curses.tigetnum("lines")
        windowsize = column_length / 10
        t = prettytable.PrettyTable(['PID', 'USER', 'COMMAND', 'TIME', 'RD/WR', 'FILES', 'STATUS', 'NET'])
        for pidn in process_query_dict.keys():
            t.add_row([str(pidn), str(process_query_dict[pidn][1]), str(
                process_query_dict[pidn][2]), str(process_query_dict[pidn][6]), str("WR" if int(
                process_query_dict[pidn][11]) < int(process_query_dict[pidn][13]) else "RD"), str(len(
                process_query_dict[pidn][19])), str(process_query_dict[pidn][20]), str(
                len(process_query_dict[pidn][21]))])
        print t

def make_base_calls():
    curses.initscr()
    curses.endwin()
    curses.setupterm()


# Debug code
refresh_monitoring()
