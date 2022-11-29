#!/usr/bin/python3
import os, re
from subprocess import check_output, STDOUT

compressors = [
    # Command, extra prefix, levels, output suffix
    ("gzip",   "-k -",      (1,  9), ".gz"),
    ("brotli", "-q ",       (0, 11), ".br"),
    ("zstd",   "--ultra -", (1, 22), ".zst") ]

def calc_compression_table(infile):
    print("Checking compression for file '%s'" % infile)
    print(check_output(["xxd", "-l", "64", infile]).decode("ascii"))
    insz = os.path.getsize(infile)
    for cmd, prefix, levels, suffix in compressors:
        (fastest, best) = levels
        for lvl in range(fastest, best + 1):
            tmpname = "%s.%s-%d" % (infile, cmd, lvl)
            outname = tmpname + suffix
            if os.path.isfile(outname):
                os.unlink(outname)
            os.rename(infile, tmpname)
            compress_cmd = "%s %s%s %s" % (cmd, prefix, lvl, tmpname)
            time_cmd = "/usr/bin/time -f '%%U' %s" % compress_cmd
            user_elapsed = float(check_output(time_cmd, shell=True, stderr=STDOUT))
            outsz = os.path.getsize(outname)
            compname = "%s-%d" % (cmd, lvl)
            ratio = (outsz / insz * 100.0)
            print("%-9s %6.2fs %10d %6.2f%%" % (compname, user_elapsed, outsz, ratio))
            os.rename(tmpname, infile)

def check_version(cmd):
    out = check_output([cmd, "--version"])
    ver = re.findall(br"([ vV]([\d]+\.[\d]+(\.[\d]+)?))", out)[0][1]
    return cmd + " " + ver.decode("ascii")

print("Versions: %s" % ", ".join([check_version(comp[0]) for comp in compressors]))
print("")
calc_compression_table("testfloat.dat")
print("")
calc_compression_table("testint.dat")
