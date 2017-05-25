import cve_exploitdb_dict
import commands
import sys

if len(sys.argv) < 2:
    print "Usage: python cve_searchsploit.py <cve>"
    print
    sys.exit(1)

cve_map = cve_exploitdb_dict.get_cve_map()

cve = sys.argv[1]

if not cve in cve_map:
    print "CVE not found."
    print
else:
    cmd = "searchsploit " + cve_map[cve]
    print commands.getstatusoutput(cmd)[1]


