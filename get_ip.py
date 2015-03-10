#-*-coding:utf-8-*-
import sys,re
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i","--input",dest="input",help="please press the input file",metavar="input")
parser.add_option("-o","--output",dest="output",default='ips.txt',help="please press the output file")
(options,args) = parser.parse_args()
inFile = options.input
output = options.output

if not inFile:
    print '请输入正确文件路径'
    exit()

fp = open(inFile)
lines = fp.read()
ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}',lines)
ips = set(ips)
fp.close()

for ip in ips:
    w = open(output,'a')
    w.write(ip+'\n')
    w.close()
else:
    print 'all done'